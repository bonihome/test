# Quick Start Guide

## Getting Started in 3 Steps

### Step 1: Install Dependencies

```bash
pip install -r requirements.txt
```

This installs Flask and Flask-CORS, the only dependencies needed.

### Step 2: Start the Server

```bash
cd backend
python app.py
```

The server will start on http://localhost:5000

### Step 3: Open the Application

Open your web browser and navigate to:
```
http://localhost:5000
```

## Using the Calculator

1. **Fill in the form**:
   - Select Vehicle Type (Car, SUV, Pickup, Van, or Truck)
   - Select Propulsion System (Gasoline, Diesel, PHEV, BEV, HEV, or FCEV)
   - Enter FOB Price in USD
   - Enter Target Margin as a percentage
   - Select Production Country (where the vehicle is made)
   - Select Destination Country (where it will be sold)

2. **Click "Calculate MSRP"**

3. **Review the results**:
   - Detailed price breakdown
   - All applicable taxes and tariffs
   - Source attribution for all rates
   - Final MSRP

## Example Scenarios

### Scenario 1: Chinese BEV to Europe
This calculation shows the impact of EU anti-subsidy duties on Chinese electric vehicles:

- Vehicle: Car (BEV)
- Route: China → Germany
- FOB: $25,000
- Margin: 15%
- **Result**: MSRP ~$49,988 (includes 38.1% special tariff + 19% VAT)

### Scenario 2: USMCA Trade
This shows the benefits of the US-Mexico-Canada free trade agreement:

- Vehicle: Car (Gasoline)
- Route: Mexico → USA
- FOB: $20,000
- Margin: 18%
- **Result**: MSRP ~$26,070 (0% tariff due to USMCA)

### Scenario 3: EU Internal Market
This demonstrates free movement within the EU:

- Vehicle: Car (BEV)
- Route: Germany → France
- FOB: $35,000
- Margin: 12%
- **Result**: MSRP ~$48,182 (0% tariff within EU)

## API Usage

If you want to use the API directly:

```bash
curl -X POST http://localhost:5000/api/calculate \
  -H "Content-Type: application/json" \
  -d '{
    "vehicle_type": "Car",
    "propulsion": "BEV",
    "fob_price": 25000,
    "target_margin": 15,
    "production_country": "China",
    "destination_country": "Germany"
  }'
```

## Data Updates

To update tariff or tax data:

1. Edit the JSON files in the `data/` directory:
   - `tariffs.json` - Import tariff rates
   - `taxes.json` - Tax rates by country
   - `freight.json` - Shipping cost estimates

2. Always include source attribution:
   - `source`: Name of the official source
   - `source_url`: Link to the official website
   - `last_updated`: Date when the data was verified

3. Restart the server to load the new data

## Supported Countries

**Production Countries (14)**: China, USA, Germany, UK, France, Italy, Turkey, Japan, South Korea, India, Thailand, Indonesia, Mexico, Brazil

**Destination Countries (25)**: China, USA, Germany, France, Italy, Spain, Sweden, Norway, Denmark, Belgium, Turkey, UK, Thailand, Indonesia, India, Japan, South Korea, Singapore, Vietnam, Philippines, Australia, Canada, Mexico, Brazil, Argentina

## Trade Agreements Implemented

- **USMCA**: US, Mexico, Canada (0% tariffs)
- **EU Internal Market**: All EU countries (0% tariffs)
- **EU-Japan EPA**: Japan ↔ EU (0% tariffs)
- **EU-Korea FTA**: South Korea ↔ EU (0% tariffs)
- **UK-EU TCA**: UK ↔ EU (0% tariffs)
- **RCEP**: Asia-Pacific countries (reduced tariffs)
- **CPTPP**: Trans-Pacific Partnership (0% tariffs)
- **EU-Turkey Customs Union**: Turkey ↔ EU (0% tariffs)
- **MERCOSUR**: Brazil ↔ Argentina (0% tariffs)

## Troubleshooting

**Problem**: Server won't start
- **Solution**: Make sure Flask is installed: `pip install flask flask-cors`

**Problem**: API returns errors
- **Solution**: Check that all required fields are provided in the request

**Problem**: Results seem incorrect
- **Solution**: Verify the data in `data/` directory against official sources

**Problem**: Can't access from other devices
- **Solution**: The server binds to 0.0.0.0, so it should be accessible on your network at `http://[your-ip]:5000`

## Notes

- All calculations are in USD
- Exchange rates are not included
- Freight costs are estimates and may vary
- Tax rates are simplified in some cases
- Always verify with official customs authorities for actual imports

## Support

For questions or issues, please refer to the main README.md file or open an issue on the repository.
