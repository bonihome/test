# API Documentation

## Base URL

```
http://localhost:5000/api
```

## Endpoints

### 1. Get Production Countries

Returns a list of all supported production countries.

**Endpoint**: `GET /api/countries/production`

**Response**:
```json
{
  "countries": [
    "China",
    "USA",
    "Germany",
    "UK",
    "France",
    "Italy",
    "Turkey",
    "Japan",
    "South Korea",
    "India",
    "Thailand",
    "Indonesia",
    "Mexico",
    "Brazil"
  ]
}
```

**Example**:
```bash
curl http://localhost:5000/api/countries/production
```

---

### 2. Get Destination Countries

Returns a list of all supported destination countries.

**Endpoint**: `GET /api/countries/destination`

**Response**:
```json
{
  "countries": [
    "China",
    "USA",
    "Germany",
    "France",
    "Italy",
    "Spain",
    "Sweden",
    "Norway",
    "Denmark",
    "Belgium",
    "Turkey",
    "UK",
    "Thailand",
    "Indonesia",
    "India",
    "Japan",
    "South Korea",
    "Singapore",
    "Vietnam",
    "Philippines",
    "Australia",
    "Canada",
    "Mexico",
    "Brazil",
    "Argentina"
  ]
}
```

**Example**:
```bash
curl http://localhost:5000/api/countries/destination
```

---

### 3. Get Vehicle Types

Returns a list of all supported vehicle types.

**Endpoint**: `GET /api/vehicle-types`

**Response**:
```json
{
  "types": [
    "Car",
    "SUV",
    "Pickup",
    "Van",
    "Truck"
  ]
}
```

**Example**:
```bash
curl http://localhost:5000/api/vehicle-types
```

---

### 4. Get Propulsion Types

Returns a list of all supported propulsion systems.

**Endpoint**: `GET /api/propulsion-types`

**Response**:
```json
{
  "types": [
    "Gasoline",
    "Diesel",
    "PHEV",
    "BEV",
    "HEV",
    "FCEV"
  ]
}
```

**Example**:
```bash
curl http://localhost:5000/api/propulsion-types
```

---

### 5. Calculate MSRP

Calculate the MSRP based on vehicle and export parameters.

**Endpoint**: `POST /api/calculate`

**Request Headers**:
```
Content-Type: application/json
```

**Request Body**:
```json
{
  "vehicle_type": "Car",
  "propulsion": "BEV",
  "fob_price": 25000,
  "target_margin": 15,
  "production_country": "China",
  "destination_country": "Germany"
}
```

**Request Parameters**:

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| vehicle_type | string | Yes | Type of vehicle (Car, SUV, Pickup, Van, Truck) |
| propulsion | string | Yes | Propulsion system (Gasoline, Diesel, PHEV, BEV, HEV, FCEV) |
| fob_price | number | Yes | FOB price in USD |
| target_margin | number | Yes | Target margin as percentage (0-100) |
| production_country | string | Yes | Country of production |
| destination_country | string | Yes | Destination country for export |

**Success Response** (200 OK):
```json
{
  "fob_price": 25000.0,
  "freight_cost": 1200.0,
  "insurance_cost": 250.0,
  "cif_value": 26450.0,
  "tariff_rate": 38.1,
  "tariff_amount": 10077.45,
  "taxes": [
    {
      "type": "VAT",
      "rate": 19.0,
      "amount": 6940.22,
      "source": "German Federal Ministry of Finance",
      "source_url": "https://www.bundesfinanzministerium.de/",
      "note": ""
    }
  ],
  "total_taxes": 6940.22,
  "margin_rate": 15.0,
  "margin_amount": 6520.15,
  "msrp": 49987.82,
  "sources": {
    "tariff": {
      "source": "EU Commission Anti-Subsidy Decision 2024",
      "url": "https://policy.trade.ec.europa.eu/enforcement-and-protection/taking-action-against-unfair-trading-practices/anti-subsidy-measures_en",
      "last_updated": "2024-07-04"
    },
    "freight": {
      "source": "Average Asia-Europe container shipping cost"
    },
    "taxes": [
      {
        "type": "VAT",
        "source": "German Federal Ministry of Finance",
        "url": "https://www.bundesfinanzministerium.de/"
      }
    ]
  }
}
```

**Response Fields**:

| Field | Type | Description |
|-------|------|-------------|
| fob_price | number | Free On Board price |
| freight_cost | number | Estimated freight/shipping cost |
| insurance_cost | number | Insurance cost (typically 1% of FOB) |
| cif_value | number | Cost, Insurance, and Freight value |
| tariff_rate | number | Effective tariff rate (%) |
| tariff_amount | number | Total tariff amount in USD |
| taxes | array | Array of tax objects with type, rate, and amount |
| total_taxes | number | Sum of all taxes |
| margin_rate | number | Target margin percentage |
| margin_amount | number | Margin amount in USD |
| msrp | number | Final Manufacturer's Suggested Retail Price |
| sources | object | Source attribution for all rates |

**Error Response** (400 Bad Request):
```json
{
  "error": "Missing required field: vehicle_type"
}
```

**Error Response** (500 Internal Server Error):
```json
{
  "error": "Calculation error: [error message]"
}
```

**Example**:
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

---

## Calculation Formula

The MSRP is calculated using the following formula:

```
1. CIF = FOB + Freight + Insurance
2. Duty = CIF × Tariff Rate
3. Tax Base = CIF + Duty (varies by country)
4. Total Taxes = Sum of all applicable taxes
5. MSRP = CIF + Duty + Total Taxes + Margin
```

### Insurance Calculation
- Fixed at 1% of FOB price

### Freight Estimation
- Based on origin-destination pairs
- Varies by route:
  - Regional: $300-800
  - Asia-Europe: $800-1,500
  - Asia-Americas: $1,000-2,000
  - Europe-Americas: $1,500-2,500

### Tax Base Variations
Different countries calculate taxes on different bases:
- **CIF**: Some countries apply taxes directly on CIF value
- **CIF + Duty**: Most countries (including EU) apply taxes on CIF + Duty
- **Cascading**: Some countries have progressive tax calculations

## Special Tariff Cases

### China BEV to EU
Chinese Battery Electric Vehicles exported to EU countries are subject to anti-subsidy duties:
- Base EU tariff: 10%
- Additional anti-subsidy duty: 17-38.1% (varies by manufacturer)
- Effective rate: 38.1% (used in this calculator)

### US Section 301 Tariffs
Vehicles from China to USA may be subject to additional Section 301 tariffs:
- Base US tariff: 2.5%
- Additional Section 301 tariff: 25%
- Effective rate: 27.5%

### Free Trade Agreements
When FTA applies, tariff rate is reduced to 0% or preferential rate:
- **USMCA**: US, Mexico, Canada
- **EU Internal Market**: All EU member states
- **EU-Japan EPA**: EU ↔ Japan
- **EU-Korea FTA**: EU ↔ South Korea
- **UK-EU TCA**: UK ↔ EU
- **RCEP**: Various Asia-Pacific countries
- **CPTPP**: Trans-Pacific Partnership members

## Rate Limiting

Currently, there is no rate limiting implemented. Use responsibly.

## Error Codes

| Code | Description |
|------|-------------|
| 200 | Success |
| 400 | Bad Request - Missing or invalid parameters |
| 500 | Internal Server Error - Calculation error |

## Data Sources

All tariff and tax rates are sourced from official government databases:

- **WTO Tariff Database**: https://www.wto.org/
- **EU TARIC**: https://ec.europa.eu/taxation_customs/dds2/taric/
- **USITC**: https://www.usitc.gov/
- Country-specific customs and tax authority websites

## CORS

Cross-Origin Resource Sharing (CORS) is enabled for all origins. The API can be called from any frontend application.

## Authentication

Currently, no authentication is required. This is a public API for calculation purposes.

## Versioning

This is version 1.0.0 of the API. Future versions may include:
- v2: Database backend instead of JSON files
- v3: Real-time tariff updates via external APIs
- v4: User accounts and saved calculations

## Support

For API issues or questions, please refer to the main README.md or open an issue on the repository.
