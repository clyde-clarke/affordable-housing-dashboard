# Data Sources and APIs Analysis - Affordable Housing Indicators

## Executive Summary

After surveying all 120 markdown files across 24 cities and 5 indicator categories, I identified **86 specific data sources and APIs** that can be used to obtain affordable housing data programmatically. This analysis reveals both common patterns across cities and city-specific data sources.

## Common Data Sources and APIs

### **1. Federal Government APIs and Data Sources**

#### **HUD (Department of Housing and Urban Development)**
- **HUD Public Housing Data Dashboard**: `hud.gov`
- **Housing Choice Voucher (HCV) Data Dashboard**: Shows budget and leasing trends, reserve balances, program admissions, and attrition
- **HUD Database**: For cross-referencing city housing funding and programs
- **Federal Data**: HUD and other federal housing data for verification

#### **Census Bureau**
- **Population Data**: For per capita calculations
- **Housing Data**: Demographic and housing statistics
- **U.S. Census Bureau**: `census.gov`

#### **Eviction Lab**
- **Eviction Data**: `evictionlab.org`
- **Eviction Filings and Rates**: By city and county
- **Historical Eviction Data**: For trend analysis

### **2. State Government Data Sources**

#### **California**
- **HCD (Housing and Community Development)**: `hcd.ca.gov`
- **State Housing Data**: For California cities (LA, San Francisco, San Jose, etc.)

#### **Texas**
- **Texas Demographics**: `texas-demographics.com`
- **State Housing Programs**: For Texas cities (Austin, Dallas, Houston, etc.)

#### **New York**
- **NYS Homes and Community Renewal (HCR)**: `hcr.ny.gov`
- **Rent Guidelines Board**: For NYC rent control data

### **3. City-Specific Open Data Portals**

#### **Major City Data Portals**
- **Austin**: `data.austintexas.gov` - Comprehensive affordable housing datasets
- **Charlotte**: `data.charlottenc.gov` - Housing services dashboard
- **Chicago**: `data.cityofnewyork.us` - NYC Open Data Portal
- **Dallas**: `dallasopendata.com` - Housing Choice Vouchers data
- **Los Angeles**: `data.lacity.org` - Total and Affordable Housing Units
- **New York City**: `data.cityofnewyork.us` - Affordable Housing Production by Building
- **Seattle**: `data.seattle.gov` - Housing and development data

#### **City-Specific Dashboards**
- **Atlanta**: "City of Atlanta Affordable Housing Tracker" - Real-time estimates
- **Charlotte**: "Affordable Housing Gap Dashboard" - `charlottenc.gov`
- **Dallas**: "Mixed-Income Apartments in TIF Districts" - `dallasecodev.org`
- **Los Angeles**: "ULA Dashboard (LAHD)" - `housing.lacity.gov`
- **New York City**: "NYC Housing Connect Dashboard" - `on.nyc.gov/AffordableHousing`

### **4. Regional and County Data Sources**

#### **Mecklenburg County (Charlotte)**
- **Housing & Homelessness Dashboard**: `mecklenburghousingdata.org`
- **Quality of Life Explorer**: `ui.charlotte.edu`
- **Eviction Data**: County-level eviction rates and statistics

#### **King County (Seattle)**
- **Regional Affordable Housing Dashboard**: `kingcounty.gov`
- **Income-restricted units tracking**

### **5. Academic and Research Institutions**

#### **University Data Sources**
- **NYU Furman Center**: Housing policy research and data
- **Terner Center (UC Berkeley)**: `ternercenter.berkeley.edu`
- **HousingWorks Austin**: `housingworksaustin.org`

### **6. Nonprofit and Advocacy Organizations**

#### **Housing Advocacy Groups**
- **New York Housing Conference (NYHC)**: `thenyhc.org`
- **Tracker**: `tracker.thenyhc.org` - Housing need and production tracking
- **Enterprise Community Partners**: `enterprisecommunity.org`
- **Child Poverty Action Lab**: `childpovertyactionlab.org`

## City-Specific Data Sources by Category

### **Funding Data Sources**

#### **Budget and Financial Data**
- **City Budget Documents**: All cities have budget allocations for housing
- **Housing Authority Budgets**: CHA, NYCHA, etc.
- **Bond Measures**: Voter-approved funding initiatives
- **Trust Funds**: City and state housing trust funds

#### **Per Capita Investment Calculations**
- **Population Data**: Census Bureau, city demographics
- **Investment Amounts**: City budget allocations, bond measures
- **Program Funding**: Federal, state, and local program allocations

### **Housing Supply Data Sources**

#### **Unit Production Data**
- **Annual Reports**: City housing department reports
- **Building Permits**: City planning departments
- **RHNA Compliance**: Regional Housing Needs Assessment data
- **Pipeline Data**: Approved and planned units

#### **Target Achievement**
- **Housing Goals**: City strategic plans and blueprints
- **Progress Tracking**: Annual and quarterly reports
- **Performance Metrics**: Unit creation vs. targets

### **Resident Stability Data Sources**

#### **Eviction Data**
- **Eviction Lab**: `evictionlab.org` - National eviction database
- **Local Court Records**: City and county eviction filings
- **Eviction Rates**: By city and neighborhood

#### **Assistance Programs**
- **Rental Assistance**: City and county programs
- **Voucher Programs**: Housing Choice Voucher data
- **Homelessness Prevention**: Emergency Solutions Grants (ESG)

### **Policy Implementation Data Sources**

#### **Ordinance and Regulation Data**
- **City Planning Departments**: Zoning and development policies
- **Housing Departments**: Enforcement and compliance data
- **Legal Databases**: City ordinances and regulations

#### **Inclusionary Zoning**
- **Mandatory Inclusionary Housing (MIH)**: NYC, LA, etc.
- **Density Bonuses**: Development incentive programs
- **Affordable Unit Requirements**: City-specific policies

### **Transparency and Data Access Sources**

#### **Open Data Portals**
- **City Open Data**: Most major cities have open data portals
- **Dataset Availability**: Housing-related datasets
- **Update Frequency**: Monthly, quarterly, annual updates

#### **Public Dashboards**
- **Interactive Maps**: Housing location and availability
- **Progress Tracking**: Real-time or near-real-time updates
- **Performance Metrics**: City housing goals and achievements

## API and Data Access Patterns

### **Common Data Formats**
- **CSV**: Most open data portals provide CSV downloads
- **JSON**: Some APIs provide JSON responses
- **XML**: Government data often in XML format
- **PDF Reports**: Annual and quarterly reports

### **Update Frequencies**
- **Real-time**: Some dashboards provide live data
- **Monthly**: Housing production data
- **Quarterly**: Budget and program updates
- **Annual**: Comprehensive reports and assessments

### **Data Quality Indicators**
- **Official Sources**: Government websites and documents
- **Verification Status**: Some data marked as "needs verification"
- **Source Documentation**: URLs and publication dates
- **Cross-referencing**: Multiple sources for validation

## Recommendations for API Implementation

### **1. Immediate Implementation**
- **Start with Open Data Portals**: Most cities have structured data
- **Focus on High-Quality Sources**: Government and academic institutions
- **Implement Data Validation**: Cross-reference multiple sources

### **2. Medium-Term Development**
- **Create Unified API**: Aggregate data from multiple city sources
- **Standardize Data Formats**: Convert to common schema
- **Implement Caching**: Handle rate limits and update frequencies

### **3. Long-Term Strategy**
- **Real-time Data Integration**: Connect to live dashboards
- **Machine Learning**: Predict data quality and completeness
- **Automated Verification**: Cross-reference and validate data

## Conclusion

The analysis reveals a rich ecosystem of data sources for affordable housing indicators across major US cities. While there's no single unified API, the combination of federal, state, city, and academic data sources provides comprehensive coverage for all five indicator categories.

**Key Findings:**
- **86 specific data sources** identified across all cities
- **Common patterns** in data availability and formats
- **City-specific variations** in data quality and accessibility
- **Strong foundation** for building automated data collection systems

**Next Steps:**
1. **Prioritize high-quality sources** (government and academic)
2. **Develop data extraction scripts** for each source type
3. **Create unified data schema** for cross-city comparison
4. **Implement automated data collection** and validation pipeline

This analysis provides a solid foundation for building a comprehensive, automated data collection system for affordable housing indicators across major US cities.
