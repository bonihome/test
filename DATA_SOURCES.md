# Data Sources Documentation

This document lists all the official sources used for tariff and tax data in the Vehicle MSRP Calculator.

## Last Updated: 2024-01-01

---

## Tariff Sources

### International Organizations

#### World Trade Organization (WTO)
- **URL**: https://www.wto.org/
- **Use**: Default tariff rates for countries without specific FTA
- **Update Frequency**: Annual
- **Notes**: Provides Most Favored Nation (MFN) rates

### Regional Organizations

#### European Union - TARIC Database
- **URL**: https://ec.europa.eu/taxation_customs/dds2/taric/taric_consultation.jsp
- **Use**: EU import tariffs for all products
- **Update Frequency**: Continuous updates
- **Notes**: Official EU customs tariff database

#### United States International Trade Commission (USITC)
- **URL**: https://www.usitc.gov/
- **DataWeb**: https://dataweb.usitc.gov/
- **Use**: US import tariffs and trade statistics
- **Update Frequency**: Continuous updates
- **Notes**: Includes Section 301 tariffs

---

## Free Trade Agreements

### USMCA (United States-Mexico-Canada Agreement)
- **Official Site**: https://ustr.gov/trade-agreements/free-trade-agreements/united-states-mexico-canada-agreement
- **Effective**: July 1, 2020
- **Vehicle Tariffs**: 0% (with rules of origin requirements)
- **Countries**: USA, Mexico, Canada

### EU Internal Market
- **Official Site**: https://ec.europa.eu/taxation_customs/
- **Vehicle Tariffs**: 0% between EU member states
- **Countries**: All EU members (Germany, France, Italy, Spain, Belgium, Denmark, Sweden, etc.)

### EU-Japan Economic Partnership Agreement (EPA)
- **Official Site**: https://policy.trade.ec.europa.eu/eu-trade-relationships-country-and-region/countries-and-regions/japan/eu-japan-agreement_en
- **Effective**: February 1, 2019
- **Vehicle Tariffs**: 0% (phased elimination completed)
- **Countries**: EU ↔ Japan

### EU-Korea Free Trade Agreement
- **Official Site**: https://policy.trade.ec.europa.eu/eu-trade-relationships-country-and-region/countries-and-regions/south-korea/eu-south-korea-agreement_en
- **Effective**: July 1, 2011
- **Vehicle Tariffs**: 0% (phased elimination completed)
- **Countries**: EU ↔ South Korea

### UK-EU Trade and Cooperation Agreement (TCA)
- **Official Site**: https://www.gov.uk/government/publications/ukeu-and-eaec-trade-and-cooperation-agreement-ts-no82021
- **Effective**: January 1, 2021
- **Vehicle Tariffs**: 0% (with rules of origin)
- **Countries**: UK ↔ EU

### RCEP (Regional Comprehensive Economic Partnership)
- **Official Site**: https://www.mofa.go.jp/ecm/ie/page4e_001095.html
- **Effective**: January 1, 2022
- **Vehicle Tariffs**: Phased reductions (varies by country pair)
- **Countries**: ASEAN+5 (China, Japan, South Korea, Australia, New Zealand, ASEAN members)

### CPTPP (Comprehensive and Progressive Trans-Pacific Partnership)
- **Official Site**: https://www.mofa.go.jp/ecm/ie/page4e_000943.html
- **Effective**: December 30, 2018
- **Vehicle Tariffs**: 0% (phased elimination)
- **Countries**: Japan, Australia, Canada, Mexico, Vietnam, Singapore, Malaysia, Brunei, Chile, New Zealand, Peru

### EU-Turkey Customs Union
- **Official Site**: https://policy.trade.ec.europa.eu/eu-trade-relationships-country-and-region/countries-and-regions/turkey_en
- **Effective**: December 31, 1995
- **Vehicle Tariffs**: 0%
- **Countries**: EU ↔ Turkey

### MERCOSUR
- **Official Site**: https://www.mercosur.int/
- **Vehicle Tariffs**: 0% between members
- **Countries**: Brazil, Argentina, Paraguay, Uruguay

---

## Special Tariff Cases

### EU Anti-Subsidy Duties on Chinese BEVs
- **Source**: EU Commission Decision 2024
- **URL**: https://policy.trade.ec.europa.eu/enforcement-and-protection/taking-action-against-unfair-trading-practices/anti-subsidy-measures_en
- **Effective**: July 4, 2024
- **Rates**: 
  - BYD: 17.4%
  - Geely: 19.9%
  - SAIC: 37.6%
  - Other cooperating companies: 20.8%
  - Non-cooperating companies: 37.6%
  - Tesla (from China): 20.8%
- **Notes**: Applied on top of base 10% EU tariff, total effective rate up to 47.6%
- **Calculator Uses**: 38.1% as average rate

### US Section 301 Tariffs on China
- **Source**: USTR Section 301 Investigation
- **URL**: https://ustr.gov/issue-areas/enforcement/section-301-investigations/section-301-china
- **Effective**: Various dates since 2018
- **Rate**: Additional 25% on many Chinese products including vehicles
- **Notes**: Combined with base 2.5% US tariff = 27.5% total

---

## Tax Sources by Country

### Europe

#### Germany
- **Tax Authority**: Bundesministerium der Finanzen
- **URL**: https://www.bundesfinanzministerium.de/
- **VAT Rate**: 19%
- **Tax Base**: CIF + Duty

#### France
- **Tax Authority**: Direction générale des Finances publiques
- **URL**: https://www.impots.gouv.fr/
- **VAT Rate**: 20%
- **Registration Tax**: Variable (0% for BEVs)
- **Tax Base**: CIF + Duty

#### Italy
- **Tax Authority**: Agenzia delle Entrate
- **URL**: https://www.agenziaentrate.gov.it/
- **VAT Rate**: 22%
- **Tax Base**: CIF + Duty

#### Spain
- **Tax Authority**: Agencia Tributaria
- **URL**: https://www.agenciatributaria.es/
- **VAT Rate**: 21%
- **Registration Tax**: Variable by CO2 emissions (0% for BEVs)
- **Tax Base**: CIF + Duty

#### Sweden
- **Tax Authority**: Skatteverket
- **URL**: https://www.skatteverket.se/
- **VAT Rate**: 25%
- **Tax Base**: CIF + Duty

#### Norway
- **Tax Authority**: Skatteetaten
- **URL**: https://www.skatteetaten.no/
- **VAT Rate**: 25%
- **Registration Tax**: Variable (0% for BEVs)
- **Tax Base**: CIF + Duty

#### Denmark
- **Tax Authority**: Skattestyrelsen
- **URL**: https://www.skat.dk/
- **VAT Rate**: 25%
- **Registration Tax**: 85-150% (reduced for BEVs)
- **Tax Base**: CIF + Duty

#### Belgium
- **Tax Authority**: SPF Finances
- **URL**: https://finances.belgium.be/
- **VAT Rate**: 21%
- **Tax Base**: CIF + Duty

#### United Kingdom
- **Tax Authority**: HM Revenue & Customs
- **URL**: https://www.gov.uk/government/organisations/hm-revenue-customs
- **VAT Rate**: 20%
- **Tax Base**: CIF + Duty

#### Turkey
- **Tax Authority**: Gelir İdaresi Başkanlığı
- **URL**: https://www.gib.gov.tr/
- **VAT Rate**: 20%
- **Special Consumption Tax (ÖTV)**: 45-220% by engine size
- **Tax Base**: CIF + Duty

### Americas

#### United States
- **Tax Authority**: State and local tax authorities
- **Sales Tax**: Varies by state (0-10.25%)
- **Calculator Uses**: 7.25% (California rate as example)
- **Notes**: No federal sales tax, rates vary significantly by state

#### Canada
- **Tax Authority**: Canada Revenue Agency
- **URL**: https://www.canada.ca/en/revenue-agency.html
- **GST Rate**: 5%
- **Provincial Tax**: Varies by province
- **Calculator Uses**: 7% average provincial rate
- **Tax Base**: CIF + Duty

#### Mexico
- **Tax Authority**: Servicio de Administración Tributaria (SAT)
- **URL**: https://www.sat.gob.mx/
- **VAT Rate**: 16%
- **ISAN (New Vehicle Tax)**: 3%
- **Tax Base**: CIF + Duty

#### Brazil
- **Tax Authority**: Receita Federal do Brasil
- **URL**: http://receita.economia.gov.br/
- **IPI Rate**: 7-25% (varies by engine size)
- **ICMS Rate**: 12-25% (varies by state, using 18% average)
- **PIS/COFINS**: 11.75%
- **Tax Base**: CIF + Duty

#### Argentina
- **Tax Authority**: AFIP
- **URL**: https://www.afip.gob.ar/
- **VAT Rate**: 21%
- **Internal Tax**: 20% (luxury tax)
- **Tax Base**: CIF + Duty

### Asia

#### China
- **Tax Authority**: State Taxation Administration
- **URL**: http://www.chinatax.gov.cn/eng/
- **VAT Rate**: 13%
- **Consumption Tax**: 1-40% (varies by engine displacement)
- **Calculator Uses**: 5% average
- **Tax Base**: CIF + Duty

#### Japan
- **Tax Authority**: National Tax Agency
- **URL**: https://www.nta.go.jp/english/
- **Consumption Tax**: 10%
- **Tax Base**: CIF + Duty

#### South Korea
- **Tax Authority**: National Tax Service
- **URL**: https://www.nts.go.kr/english/
- **VAT Rate**: 10%
- **Individual Consumption Tax**: 5% (exempt for BEVs)
- **Tax Base**: CIF + Duty

#### Thailand
- **Tax Authority**: Revenue Department
- **URL**: https://www.rd.go.th/
- **VAT Rate**: 7%
- **Excise Tax**: 10-80% (varies by engine size, lower for BEVs)
- **Calculator Uses**: 35% average
- **Tax Base**: CIF for excise, CIF + Duty for VAT

#### Indonesia
- **Tax Authority**: Direktorat Jenderal Pajak
- **URL**: https://www.pajak.go.id/
- **VAT Rate**: 11%
- **Luxury Tax (PPnBM)**: 10-125% (varies)
- **Calculator Uses**: 40% average
- **Tax Base**: CIF + Duty

#### India
- **Tax Authority**: Central Board of Indirect Taxes and Customs
- **URL**: https://www.cbic.gov.in/
- **GST Rate**: 28%
- **Compensation Cess**: 1-22% (varies by vehicle length and type)
- **Calculator Uses**: 22% average
- **Tax Base**: CIF + Duty

#### Singapore
- **Tax Authority**: IRAS and LTA
- **URL**: https://www.iras.gov.sg/ and https://www.lta.gov.sg/
- **GST Rate**: 9%
- **Additional Registration Fee (ARF)**: Tiered, up to 320%
- **Calculator Uses**: 100% average
- **Tax Base**: CIF + Duty

#### Vietnam
- **Tax Authority**: General Department of Taxation
- **URL**: https://www.gdt.gov.vn/
- **VAT Rate**: 10%
- **Special Consumption Tax**: 10-150% (varies by engine size)
- **Calculator Uses**: 50% average
- **Tax Base**: CIF for SCT, CIF + Duty for VAT

#### Philippines
- **Tax Authority**: Bureau of Internal Revenue
- **URL**: https://www.bir.gov.ph/
- **VAT Rate**: 12%
- **Excise Tax**: Varies by engine displacement
- **Calculator Uses**: 10% average
- **Tax Base**: CIF + Duty

### Oceania

#### Australia
- **Tax Authority**: Australian Taxation Office
- **URL**: https://www.ato.gov.au/
- **GST Rate**: 10%
- **Luxury Car Tax**: 33% (above AUD 89,332 threshold)
- **Notes**: Higher threshold for fuel-efficient vehicles including BEVs
- **Tax Base**: CIF + Duty

---

## Freight Cost Sources

Freight costs are based on industry averages from:
- Container shipping market reports
- Major shipping line rate cards
- Freight forwarder quotations
- Industry publications (Journal of Commerce, Lloyd's List)

### Regional Estimates:
- **Regional (same continent)**: $300-800
- **Asia ↔ Europe**: $800-1,500
- **Asia ↔ Americas**: $1,000-2,000
- **Europe ↔ Americas**: $1,500-2,500

**Note**: Actual freight costs vary significantly based on:
- Fuel prices
- Seasonal demand
- Container availability
- Specific ports of origin and destination
- Shipping line
- Volume commitments

---

## Data Maintenance Schedule

### Weekly:
- Monitor for major policy announcements
- Check for emergency tariff changes

### Monthly:
- Review tax rate changes
- Update freight cost estimates

### Quarterly:
- Comprehensive review of all tariff rates
- Update FTA implementation status
- Review special duty cases

### Annually:
- Full audit of all data sources
- Update to latest WTO tariff schedules
- Review and update all tax rates

---

## Contributing Data Updates

When updating data:

1. **Verify the source**: Use only official government or international organization sources
2. **Document the source**: Include name, URL, and access date
3. **Update the JSON files**: Maintain the existing structure
4. **Test calculations**: Verify that calculations remain accurate
5. **Update this document**: Keep the data sources list current

---

## Disclaimer

All data is sourced from publicly available official sources. While every effort is made to ensure accuracy, users should verify rates with official customs and tax authorities before making business decisions. Tariffs and taxes change frequently, and this calculator may not reflect the most current rates.

---

**For questions about data sources or to report outdated information, please open an issue on the repository.**
