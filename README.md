# Vehicle MSRP Calculator for Vehicle Exporters

A comprehensive web-based application to calculate the Manufacturer's Suggested Retail Price (MSRP) for vehicles being exported internationally. The system accounts for all costs including tariffs, taxes, freight, insurance, and target margins across 350+ country pair combinations.

## Features

- 🌍 **Global Coverage**: 14 production countries × 25 destination countries
- 🚗 **Vehicle Types**: Car, SUV, Pickup, Van, Truck
- ⚡ **Propulsion Systems**: Gasoline, Diesel, PHEV, BEV, HEV, FCEV
- 📊 **Comprehensive Calculations**: FOB, Freight, Insurance, CIF, Tariffs, Taxes, Margins
- 🔍 **Source Attribution**: All tariff and tax rates linked to official sources
- 📱 **Responsive Design**: Works on desktop and mobile devices
- 🎯 **FTA Support**: Free Trade Agreement considerations (USMCA, EU, RCEP, etc.)

## Project Structure

```
vehicle-msrp-calculator/
├── backend/
│   ├── app.py                 # Flask API server
│   ├── calculator.py          # Core calculation engine
│   ├── models.py              # Data models
│   ├── tariff_data/           # (Reserved for future use)
│   └── tax_data/              # (Reserved for future use)
├── frontend/
│   ├── index.html             # Main HTML page
│   ├── styles.css             # Styling
│   └── script.js              # Frontend logic and API calls
├── data/
│   ├── tariffs.json           # Tariff data with FTA information
│   ├── taxes.json             # Tax rates by country
│   └── freight.json           # Freight cost estimates
├── requirements.txt           # Python dependencies
└── README.md                  # This file
```

## Installation

### Prerequisites

- Python 3.8 or higher
- pip (Python package manager)
- Modern web browser

### Setup Steps

1. **Clone the repository**
   ```bash
   git clone <repository-url>
   cd test
   ```

2. **Install Python dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Start the backend server**
   ```bash
   cd backend
   python app.py
   ```
   
   The server will start on `http://localhost:5000`

4. **Open the frontend**
   
   Open `frontend/index.html` in your web browser, or serve it using a simple HTTP server:
   
   ```bash
   cd frontend
   python -m http.server 8000
   ```
   
   Then visit `http://localhost:8000` in your browser.

## Usage

### Step 1: Input Vehicle and Export Information

1. Select the **Vehicle Type** (Car, SUV, Pickup, etc.)
2. Select the **Propulsion System** (Gasoline, BEV, etc.)
3. Enter the **FOB Price** in USD
4. Enter the **Target Margin** as a percentage
5. Select the **Production Country** (origin)
6. Select the **Destination Country** (export market)
7. Click **Calculate MSRP**

### Step 2: Review Results

The results page displays:

- **Price Structure Table**: Detailed breakdown of all costs
  - FOB Price
  - Freight Cost
  - Insurance Cost
  - CIF Value
  - Import Tariff (rate and amount)
  - All applicable taxes (VAT, GST, Excise, etc.)
  - Target Margin
  - **Final MSRP**

- **Source Attribution**: Links to official sources for all rates used

Click **Recalculate** to modify inputs and run a new calculation.

## Calculation Formula

```
CIF = FOB + Freight + Insurance
Duty = CIF × Tariff Rate
Tax Base = CIF + Duty (varies by country)
Total Taxes = Sum of all applicable taxes
MSRP = CIF + Duty + Total Taxes + Margin
```

## Data Sources

All tariff and tax data is sourced from official government and international trade databases:

### Tariffs
- **WTO Tariff Database**: https://www.wto.org/
- **EU TARIC**: https://ec.europa.eu/taxation_customs/dds2/taric/
- **USITC DataWeb**: https://www.usitc.gov/
- Individual country customs websites

### Free Trade Agreements
- **USMCA**: US-Mexico-Canada Agreement
- **EU Internal Market**: Zero tariffs between EU members
- **EU-Japan EPA**: Economic Partnership Agreement
- **EU-Korea FTA**: Free Trade Agreement
- **UK-EU TCA**: Trade and Cooperation Agreement
- **RCEP**: Regional Comprehensive Economic Partnership
- **CPTPP**: Comprehensive and Progressive Trans-Pacific Partnership

## Example Calculations

### Example 1: Chinese BEV to Germany
- **Input**: China → Germany, BEV, FOB $25,000, 15% margin
- **Tariff**: 38.1% (EU anti-subsidy duty)
- **Tax**: 19% VAT
- **Result**: MSRP ~$49,988

### Example 2: Japanese Car to USA
- **Input**: Japan → USA, Gasoline, FOB $30,000, 20% margin
- **Tariff**: 2.5% (standard US rate)
- **Tax**: 7.25% sales tax (California)
- **Result**: MSRP ~$41,500

### Example 3: Mexican Car to USA (USMCA)
- **Input**: Mexico → USA, Gasoline, FOB $20,000, 18% margin
- **Tariff**: 0% (USMCA FTA)
- **Tax**: 7.25% sales tax
- **Result**: MSRP ~$27,800

## API Endpoints

Full API documentation is available in the README.

## Contributing

To contribute to this project:

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Update documentation
5. Submit a pull request

---

**Note**: This calculator provides estimates based on publicly available data. Always verify calculations with official customs and tax authorities before making business decisions.
