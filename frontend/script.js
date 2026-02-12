// API Base URL - update this if backend runs on different host/port
const API_BASE_URL = 'http://localhost:5000/api';

// DOM Elements
const step1 = document.getElementById('step1');
const step2 = document.getElementById('step2');
const form = document.getElementById('calculatorForm');
const recalculateBtn = document.getElementById('recalculateBtn');
const resultsDiv = document.getElementById('results');
const sourcesDiv = document.getElementById('sources');

// Dropdowns
const vehicleTypeSelect = document.getElementById('vehicleType');
const propulsionSelect = document.getElementById('propulsion');
const productionCountrySelect = document.getElementById('productionCountry');
const destinationCountrySelect = document.getElementById('destinationCountry');

// Initialize the application
async function init() {
    try {
        await loadDropdownData();
        setupEventListeners();
    } catch (error) {
        console.error('Initialization error:', error);
        showError('Failed to initialize application. Please refresh the page.');
    }
}

// Load data for all dropdowns
async function loadDropdownData() {
    try {
        const [vehicleTypes, propulsionTypes, productionCountries, destinationCountries] = await Promise.all([
            fetch(`${API_BASE_URL}/vehicle-types`).then(r => r.json()),
            fetch(`${API_BASE_URL}/propulsion-types`).then(r => r.json()),
            fetch(`${API_BASE_URL}/countries/production`).then(r => r.json()),
            fetch(`${API_BASE_URL}/countries/destination`).then(r => r.json())
        ]);

        populateDropdown(vehicleTypeSelect, vehicleTypes.types);
        populateDropdown(propulsionSelect, propulsionTypes.types);
        populateDropdown(productionCountrySelect, productionCountries.countries);
        populateDropdown(destinationCountrySelect, destinationCountries.countries);
    } catch (error) {
        console.error('Error loading dropdown data:', error);
        throw error;
    }
}

// Populate a dropdown with options
function populateDropdown(selectElement, options) {
    options.forEach(option => {
        const optionElement = document.createElement('option');
        optionElement.value = option;
        optionElement.textContent = option;
        selectElement.appendChild(optionElement);
    });
}

// Setup event listeners
function setupEventListeners() {
    form.addEventListener('submit', handleFormSubmit);
    recalculateBtn.addEventListener('click', showStep1);
}

// Handle form submission
async function handleFormSubmit(event) {
    event.preventDefault();

    const formData = {
        vehicle_type: document.getElementById('vehicleType').value,
        propulsion: document.getElementById('propulsion').value,
        fob_price: parseFloat(document.getElementById('fobPrice').value),
        target_margin: parseFloat(document.getElementById('targetMargin').value),
        production_country: document.getElementById('productionCountry').value,
        destination_country: document.getElementById('destinationCountry').value
    };

    try {
        // Show loading state
        const submitBtn = form.querySelector('button[type="submit"]');
        const originalText = submitBtn.textContent;
        submitBtn.innerHTML = '<span class="loading"></span> Calculating...';
        submitBtn.disabled = true;

        const response = await fetch(`${API_BASE_URL}/calculate`, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify(formData)
        });

        if (!response.ok) {
            const errorData = await response.json();
            throw new Error(errorData.error || 'Calculation failed');
        }

        const result = await response.json();
        displayResults(result, formData);
        showStep2();

        // Reset button
        submitBtn.textContent = originalText;
        submitBtn.disabled = false;
    } catch (error) {
        console.error('Calculation error:', error);
        showError(error.message);
        
        // Reset button
        const submitBtn = form.querySelector('button[type="submit"]');
        submitBtn.textContent = 'Calculate MSRP';
        submitBtn.disabled = false;
    }
}

// Display calculation results
function displayResults(result, formData) {
    // Build results table
    const resultsHTML = `
        <div class="results-summary">
            <p><strong>Vehicle:</strong> ${formData.vehicle_type} (${formData.propulsion})</p>
            <p><strong>Route:</strong> ${formData.production_country} → ${formData.destination_country}</p>
        </div>
        
        <table class="results-table">
            <thead>
                <tr>
                    <th>Cost Component</th>
                    <th>Rate</th>
                    <th>Amount (USD)</th>
                </tr>
            </thead>
            <tbody>
                <tr>
                    <td class="cost-label">FOB Price</td>
                    <td>-</td>
                    <td class="cost-value">$${formatNumber(result.fob_price)}</td>
                </tr>
                <tr>
                    <td class="cost-label">Freight Cost</td>
                    <td>-</td>
                    <td class="cost-value">$${formatNumber(result.freight_cost)}</td>
                </tr>
                <tr>
                    <td class="cost-label">Insurance Cost</td>
                    <td>~1%</td>
                    <td class="cost-value">$${formatNumber(result.insurance_cost)}</td>
                </tr>
                <tr style="background: #f8fafc; font-weight: 600;">
                    <td class="cost-label">CIF Value</td>
                    <td>-</td>
                    <td class="cost-value">$${formatNumber(result.cif_value)}</td>
                </tr>
                <tr>
                    <td class="cost-label">Import Tariff</td>
                    <td>${formatNumber(result.tariff_rate)}%</td>
                    <td class="cost-value">$${formatNumber(result.tariff_amount)}</td>
                </tr>
                ${result.taxes.map(tax => `
                    <tr>
                        <td class="cost-label tax-detail">${tax.type}${tax.note ? ' (' + tax.note + ')' : ''}</td>
                        <td>${formatNumber(tax.rate)}%</td>
                        <td class="cost-value">$${formatNumber(tax.amount)}</td>
                    </tr>
                `).join('')}
                <tr style="background: #f8fafc; font-weight: 600;">
                    <td class="cost-label">Total Taxes</td>
                    <td>-</td>
                    <td class="cost-value">$${formatNumber(result.total_taxes)}</td>
                </tr>
                <tr>
                    <td class="cost-label">Target Margin</td>
                    <td>${formatNumber(result.margin_rate)}%</td>
                    <td class="cost-value">$${formatNumber(result.margin_amount)}</td>
                </tr>
                <tr class="total-row">
                    <td colspan="2" class="cost-label">FINAL MSRP</td>
                    <td class="cost-value">$${formatNumber(result.msrp)}</td>
                </tr>
            </tbody>
        </table>
    `;

    resultsDiv.innerHTML = resultsHTML;

    // Build sources section
    const sourcesHTML = `
        <h3>📚 Data Sources</h3>
        
        <div class="source-item">
            <span class="source-label">Tariff Information:</span>
            <a href="${result.sources.tariff.url}" target="_blank" class="source-link">
                ${result.sources.tariff.source}
            </a>
            <span class="source-date">(Last updated: ${result.sources.tariff.last_updated})</span>
        </div>
        
        <div class="source-item">
            <span class="source-label">Freight Estimation:</span>
            <span>${result.sources.freight.source}</span>
        </div>
        
        ${result.sources.taxes.map(tax => `
            <div class="source-item">
                <span class="source-label">${tax.type}:</span>
                ${tax.url ? 
                    `<a href="${tax.url}" target="_blank" class="source-link">${tax.source}</a>` : 
                    `<span>${tax.source}</span>`
                }
            </div>
        `).join('')}
    `;

    sourcesDiv.innerHTML = sourcesHTML;
}

// Show step 1 (input form)
function showStep1() {
    step1.classList.add('active');
    step2.classList.remove('active');
}

// Show step 2 (results)
function showStep2() {
    step1.classList.remove('active');
    step2.classList.add('active');
}

// Format number with commas
function formatNumber(num) {
    return num.toFixed(2).replace(/\B(?=(\d{3})+(?!\d))/g, ',');
}

// Show error message
function showError(message) {
    const errorDiv = document.createElement('div');
    errorDiv.className = 'error';
    errorDiv.textContent = message;
    
    form.insertBefore(errorDiv, form.firstChild);
    
    setTimeout(() => {
        errorDiv.remove();
    }, 5000);
}

// Initialize when DOM is loaded
if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', init);
} else {
    init();
}
