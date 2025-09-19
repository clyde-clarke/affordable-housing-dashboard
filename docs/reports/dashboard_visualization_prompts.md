# Affordable Housing Dashboard Visualization Prompts

## Design Consistency Framework

### **Landscape Orientation Standard**
- **Aspect Ratio**: 16:9 (1920x1080px) for all visualizations
- **Layout**: Consistent 3-column grid system
- **Color Palette**: 
  - Primary: #2E86AB (Blue) for funding/financial data
  - Secondary: #A23B72 (Purple) for housing supply data
  - Tertiary: #F18F01 (Orange) for resident stability
  - Quaternary: #C73E1D (Red) for policy implementation
  - Quinary: #7209B7 (Violet) for transparency/data access
  - Neutral: #F5F5F5 (Light Gray) for backgrounds
  - Success: #28A745 (Green) for positive metrics
  - Warning: #FFC107 (Yellow) for caution metrics
  - Danger: #DC3545 (Red) for critical metrics

### **Typography Hierarchy**
- **Title**: 32px, Bold, #2C3E50
- **Subtitle**: 24px, SemiBold, #34495E
- **Body**: 16px, Regular, #2C3E50
- **Caption**: 12px, Regular, #7F8C8D
- **Data Labels**: 14px, Medium, #2C3E50

### **Common Data Elements**
- **Score Ranges**: 0-100 scale with consistent color gradients
- **Dollar Amounts**: Formatted with $ symbol and appropriate abbreviations (M, B, K)
- **Percentages**: Always shown with % symbol
- **Unit Counts**: Formatted with commas for thousands
- **Years**: Consistent 4-digit format
- **City Names**: Title case, consistent abbreviation handling

---

## Page 1: Executive Summary Dashboard

### **Visualization Prompt:**
```
Create a comprehensive executive summary dashboard in landscape orientation (16:9) showing:

**Top Section (Header):**
- Title: "Affordable Housing Performance Across Major US Cities"
- Subtitle: "Comprehensive Analysis of 24 Cities Across 5 Key Indicators"
- Date: "January 2025"

**Main Content (3-Column Grid):**

**Left Column - Overall Rankings:**
- Horizontal bar chart showing top 10 cities by overall score
- Color gradient from green (high) to red (low)
- Include city name and exact score value
- Title: "Top 10 Performing Cities"

**Center Column - Score Distribution:**
- Donut chart showing distribution of cities by performance tiers:
  - Excellent (80-100): Green
  - Good (60-79): Blue  
  - Fair (40-59): Yellow
  - Poor (0-39): Red
- Include count and percentage for each tier
- Title: "Performance Distribution"

**Right Column - Key Insights:**
- 3-4 bullet points highlighting major findings
- Include specific statistics (e.g., "NYC leads with $2B annual budget")
- Use icons for each insight
- Title: "Key Findings"

**Bottom Section - Quick Stats:**
- 4 metric cards showing:
  - Total Cities Analyzed: 24
  - Average Overall Score: [calculated]
  - Total Funding Identified: $[sum] billion
  - Cities with Complete Data: 24

**Design Elements:**
- Clean, professional layout with consistent spacing
- Use the defined color palette
- Include subtle shadows and borders
- Ensure all text is readable at dashboard size
```

---

## Page 2: Funding Analysis Dashboard

### **Visualization Prompt:**
```
Create a funding analysis dashboard in landscape orientation (16:9) focusing on financial commitments:

**Top Section:**
- Title: "Affordable Housing Funding Analysis"
- Subtitle: "Budget Allocations, Bond Measures, and Per Capita Investments"

**Main Content (3-Column Grid):**

**Left Column - Top Funders:**
- Horizontal bar chart of top 10 cities by funding score
- Include actual dollar amounts from markdown files
- Color: Primary blue (#2E86AB)
- Show both score and actual budget allocation
- Title: "Funding Score Rankings"

**Center Column - Budget Breakdown:**
- Stacked bar chart showing funding sources:
  - City Budget Allocations
  - Bond Measures
  - Federal Funding
  - Trust Funds
- Use different shades of blue
- Include total amounts
- Title: "Funding Sources by City"

**Right Column - Per Capita Analysis:**
- Scatter plot with:
  - X-axis: City Population
  - Y-axis: Per Capita Investment
  - Bubble size: Total Funding Amount
  - Color: Funding Score
- Include trend line
- Title: "Per Capita Investment vs Population"

**Bottom Section - Key Funding Highlights:**
- 3-4 cards showing:
  - Largest Single Allocation: NYC $2B
  - Highest Per Capita: [calculated]
  - Most Bond Measures: [calculated]
  - Total Identified Funding: $[sum] billion

**Data Integration:**
- Pull specific dollar amounts from markdown files
- Include verification status indicators
- Show data completeness for each city
```

---

## Page 3: Housing Supply Dashboard

### **Visualization Prompt:**
```
Create a housing supply dashboard in landscape orientation (16:9) focusing on unit production and pipeline:

**Top Section:**
- Title: "Housing Supply Analysis"
- Subtitle: "Unit Production, Pipeline, and Progress Toward Targets"

**Main Content (3-Column Grid):**

**Left Column - Unit Production Leaders:**
- Horizontal bar chart of top 10 cities by housing supply score
- Include actual unit counts from markdown files
- Color: Secondary purple (#A23B72)
- Show both score and units produced
- Title: "Housing Supply Score Rankings"

**Center Column - Production vs Pipeline:**
- Dual-axis chart showing:
  - Left axis: Units Produced (bars)
  - Right axis: Pipeline Units (line)
- Use purple for production, darker purple for pipeline
- Include target lines where available
- Title: "Production vs Pipeline Capacity"

**Right Column - Target Progress:**
- Progress bars showing percentage of housing targets achieved
- Include target numbers and current progress
- Color gradient from red (0%) to green (100%)
- Title: "Progress Toward Housing Targets"

**Bottom Section - Supply Highlights:**
- 4 cards showing:
  - Most Units Produced: [city] with [number] units
  - Largest Pipeline: [city] with [number] units
  - Target Achievement Rate: [percentage]
  - Total Units in Pipeline: [sum] units

**Data Integration:**
- Extract unit counts from markdown files
- Include year-specific data
- Show verification status for each claim
```

---

## Page 4: Resident Stability Dashboard

### **Visualization Prompt:**
```
Create a resident stability dashboard in landscape orientation (16:9) focusing on eviction rates and support services:

**Top Section:**
- Title: "Resident Stability Analysis"
- Subtitle: "Eviction Rates, Rental Assistance, and Homelessness Prevention"

**Main Content (3-Column Grid):**

**Left Column - Stability Rankings:**
- Horizontal bar chart of top 10 cities by resident stability score
- Include eviction rates and assistance spending
- Color: Tertiary orange (#F18F01)
- Show both score and key metrics
- Title: "Resident Stability Score Rankings"

**Center Column - Eviction vs Assistance:**
- Scatter plot showing:
  - X-axis: Eviction Rate (%)
  - Y-axis: Rental Assistance Spending ($M)
  - Bubble size: Population
  - Color: Stability Score
- Include trend line
- Title: "Eviction Rates vs Assistance Spending"

**Right Column - Support Services:**
- Stacked bar chart showing:
  - Rental Assistance Programs
  - Homelessness Prevention
  - Housing Vouchers
  - Emergency Services
- Use different shades of orange
- Title: "Support Services by City"

**Bottom Section - Stability Highlights:**
- 4 cards showing:
  - Lowest Eviction Rate: [city] at [rate]%
  - Highest Assistance Spending: [city] with $[amount]
  - Most Comprehensive Programs: [city]
  - Total Assistance Budget: $[sum] million

**Data Integration:**
- Extract eviction data from markdown files
- Include spending amounts and program details
- Show year-over-year trends where available
```

---

## Page 5: Policy Implementation Dashboard

### **Visualization Prompt:**
```
Create a policy implementation dashboard in landscape orientation (16:9) focusing on ordinances and enforcement:

**Top Section:**
- Title: "Policy Implementation Analysis"
- Subtitle: "Inclusionary Zoning, Rent Control, and Enforcement Effectiveness"

**Main Content (3-Column Grid):**

**Left Column - Policy Rankings:**
- Horizontal bar chart of top 10 cities by policy implementation score
- Include key policy metrics
- Color: Quaternary red (#C73E1D)
- Show both score and policy count
- Title: "Policy Implementation Score Rankings"

**Center Column - Policy Types:**
- Stacked bar chart showing:
  - Inclusionary Zoning Units
  - Rent-Controlled Units
  - Rent-Stabilized Units
  - Enforcement Actions
- Use different shades of red
- Title: "Policy Types by City"

**Right Column - Enforcement Effectiveness:**
- Dual-axis chart showing:
  - Left axis: Policy Score (bars)
  - Right axis: Enforcement Actions (line)
- Use red for policy, darker red for enforcement
- Title: "Policy Score vs Enforcement Actions"

**Bottom Section - Policy Highlights:**
- 4 cards showing:
  - Most Inclusionary Units: [city] with [number] units
  - Strongest Rent Control: [city] with [number] units
  - Most Active Enforcement: [city] with [number] actions
  - Total Policy Coverage: [percentage] of cities

**Data Integration:**
- Extract policy details from markdown files
- Include unit counts and enforcement data
- Show policy effectiveness metrics
```

---

## Page 6: Transparency & Data Access Dashboard

### **Visualization Prompt:**
```
Create a transparency and data access dashboard in landscape orientation (16:9) focusing on public information availability:

**Top Section:**
- Title: "Transparency & Data Access Analysis"
- Subtitle: "Public Dashboards, Open Data, and Information Availability"

**Main Content (3-Column Grid):**

**Left Column - Transparency Rankings:**
- Horizontal bar chart of top 10 cities by transparency score
- Include data availability metrics
- Color: Quinary violet (#7209B7)
- Show both score and data points
- Title: "Transparency Score Rankings"

**Center Column - Data Availability:**
- Stacked bar chart showing:
  - Public Dashboards
  - Open Data Portals
  - Regular Reports
  - Real-time Updates
- Use different shades of violet
- Title: "Data Availability by City"

**Right Column - Update Frequency:**
- Scatter plot showing:
  - X-axis: Data Freshness (days since last update)
  - Y-axis: Transparency Score
  - Bubble size: Number of Data Sources
  - Color: Update Frequency
- Title: "Data Freshness vs Transparency Score"

**Bottom Section - Transparency Highlights:**
- 4 cards showing:
  - Most Transparent: [city] with [score] score
  - Most Data Sources: [city] with [number] sources
  - Most Frequent Updates: [city] with [frequency]
  - Total Data Sources: [sum] across all cities

**Data Integration:**
- Extract dashboard and data source information from markdown files
- Include update frequencies and data quality metrics
- Show accessibility and usability ratings
```

---

## Page 7: Comparative Analysis Dashboard

### **Visualization Prompt:**
```
Create a comparative analysis dashboard in landscape orientation (16:9) showing city-to-city comparisons:

**Top Section:**
- Title: "City-to-City Comparative Analysis"
- Subtitle: "Side-by-Side Performance Comparison Across All Indicators"

**Main Content (3-Column Grid):**

**Left Column - Performance Matrix:**
- Heatmap showing all cities vs all indicators
- Color gradient from green (high) to red (low)
- Include exact scores in each cell
- Sort cities by overall performance
- Title: "Performance Heatmap"

**Center Column - Strengths & Weaknesses:**
- Radar chart for top 5 cities showing:
  - Funding
  - Housing Supply
  - Resident Stability
  - Policy Implementation
  - Transparency
- Use different colors for each city
- Title: "Top 5 Cities - Multi-Dimensional View"

**Right Column - Performance Gaps:**
- Bar chart showing:
  - Largest gaps between best and worst scores
  - Cities with most consistent performance
  - Cities with most variable performance
- Use gradient colors
- Title: "Performance Consistency Analysis"

**Bottom Section - Key Comparisons:**
- 4 cards showing:
  - Best Overall: [city] with [score]
  - Most Improved: [city] with [change]
  - Most Consistent: [city] with [variance]
  - Biggest Opportunity: [city] in [indicator]

**Data Integration:**
- Use complete normalized scores data
- Include trend analysis where available
- Show relative performance rankings
```

---

## Page 8: Regional Trends Dashboard

### **Visualization Prompt:**
```
Create a regional trends dashboard in landscape orientation (16:9) showing geographic patterns and trends:

**Top Section:**
- Title: "Regional Trends & Geographic Analysis"
- Subtitle: "Performance Patterns Across Different Regions and Metro Areas"

**Main Content (3-Column Grid):**

**Left Column - Regional Performance:**
- Bar chart grouped by region:
  - Northeast (NYC, Boston, Philadelphia)
  - West Coast (LA, San Francisco, Seattle, San Jose, San Diego)
  - South (Dallas, Houston, Atlanta, Miami, Jacksonville)
  - Midwest (Chicago, Detroit, Columbus)
  - Southwest (Phoenix, San Antonio, Austin, Fort Worth)
- Show average scores by region
- Color: Regional color coding
- Title: "Average Performance by Region"

**Center Column - Metro Area Analysis:**
- Scatter plot showing:
  - X-axis: Metro Population
  - Y-axis: Overall Score
  - Bubble size: Total Funding
  - Color: Region
- Include trend line
- Title: "Metro Size vs Performance"

**Right Column - Regional Strengths:**
- Stacked bar chart showing:
  - Which regions excel in which indicators
  - Regional specializations
  - Use indicator colors
- Title: "Regional Specializations by Indicator"

**Bottom Section - Regional Highlights:**
- 4 cards showing:
  - Top Performing Region: [region] with [score]
  - Most Funding: [region] with $[amount]
  - Best Policy Implementation: [region]
  - Most Transparent: [region]

**Data Integration:**
- Group cities by geographic regions
- Include metro area population data
- Show regional policy differences
```

---

## Page 9: Data Quality & Verification Dashboard

### **Visualization Prompt:**
```
Create a data quality and verification dashboard in landscape orientation (16:9) showing data completeness and verification status:

**Top Section:**
- Title: "Data Quality & Verification Status"
- Subtitle: "Completeness, Accuracy, and Source Verification Across All Cities"

**Main Content (3-Column Grid):**

**Left Column - Data Completeness:**
- Horizontal bar chart showing:
  - Percentage of complete data by city
  - Missing data indicators
  - Verification status
- Color: Green (complete) to Red (incomplete)
- Title: "Data Completeness by City"

**Center Column - Verification Status:**
- Stacked bar chart showing:
  - Verified Claims
  - Pending Verification
  - Unverifiable Claims
  - Missing Sources
- Use different shades of gray
- Title: "Verification Status by City"

**Right Column - Source Quality:**
- Scatter plot showing:
  - X-axis: Number of Sources
  - Y-axis: Source Quality Score
  - Bubble size: Number of Claims
  - Color: Verification Status
- Title: "Source Quality vs Quantity"

**Bottom Section - Quality Highlights:**
- 4 cards showing:
  - Most Complete Data: [city] with [percentage]%
  - Most Verified: [city] with [number] claims
  - Highest Quality Sources: [city]
  - Most Missing Data: [city] in [indicator]

**Data Integration:**
- Use verification status from markdown files
- Include source quality assessments
- Show data completeness metrics
```

---

## Page 10: Recommendations & Action Items Dashboard

### **Visualization Prompt:**
```
Create a recommendations and action items dashboard in landscape orientation (16:9) providing actionable insights:

**Top Section:**
- Title: "Recommendations & Action Items"
- Subtitle: "Priority Actions and Improvement Opportunities for Each City"

**Main Content (3-Column Grid):**

**Left Column - Priority Actions:**
- Ranked list of top 10 cities needing immediate attention
- Include specific recommendations
- Color: Red (urgent) to Yellow (moderate)
- Show current score and target score
- Title: "Priority Action Cities"

**Center Column - Improvement Opportunities:**
- Bar chart showing:
  - Biggest improvement potential by indicator
  - Quick wins vs long-term projects
  - Resource requirements
- Use indicator colors
- Title: "Improvement Opportunities by Indicator"

**Right Column - Success Stories:**
- Highlight cities with best practices
- Include specific strategies that worked
- Show before/after improvements
- Title: "Best Practices & Success Stories"

**Bottom Section - Action Plan:**
- 4 cards showing:
  - Immediate Actions (0-6 months)
  - Short-term Goals (6-18 months)
  - Long-term Vision (18+ months)
  - Resource Requirements

**Data Integration:**
- Use performance gaps to identify opportunities
- Include specific recommendations from analysis
- Show resource requirements and timelines
```

---

## Implementation Guidelines

### **Consistent Design Elements:**
1. **Header**: Always include title, subtitle, and date
2. **Grid System**: 3-column layout for main content
3. **Color Coding**: Consistent use of indicator colors
4. **Typography**: Standardized font sizes and weights
5. **Spacing**: Consistent margins and padding
6. **Icons**: Use consistent icon set for all visualizations
7. **Data Labels**: Always show exact values
8. **Legends**: Consistent positioning and styling
9. **Borders**: Subtle borders and shadows
10. **Responsiveness**: Ensure readability at dashboard size

### **Data Integration Strategy:**
1. **Primary Source**: Complete normalized scores CSV
2. **Secondary Source**: Individual markdown files for details
3. **Verification**: Include verification status indicators
4. **Updates**: Design for easy data refresh
5. **Validation**: Cross-reference multiple sources

### **Technical Requirements:**
- **Format**: High-resolution PNG or SVG
- **Size**: 1920x1080px minimum
- **Color Space**: RGB for digital display
- **Fonts**: Web-safe fonts or embedded fonts
- **Accessibility**: High contrast ratios, readable text sizes
- **Export**: Multiple formats for different use cases

This comprehensive visualization strategy ensures consistency across all dashboard pages while effectively representing the complex affordable housing data in an accessible and actionable format.
