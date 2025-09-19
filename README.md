# Affordable Housing Dashboard

A comprehensive analysis and interactive dashboard for affordable housing indicators across 24 major US cities.

## 🏠 Overview

This project provides a data-driven assessment of affordable housing performance across major US cities, evaluating five key indicator categories:

- **Funding** (25% weight): Financial commitment to affordable housing
- **Housing Supply** (25% weight): Tangible output of affordable housing efforts  
- **Resident Stability** (20% weight): Well-being and security of residents
- **Policy Implementation** (20% weight): Effectiveness of local policies and regulations
- **Transparency/Data Access** (10% weight): Availability and quality of public information

## 🚀 Quick Start

### Prerequisites
- Python 3.8+
- Node.js 16+ (for React dashboard)
- Modern web browser

### Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/yourusername/affordable-housing-dashboard.git
   cd affordable-housing-dashboard
   ```

2. **Install Python dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Run the simple HTML dashboard**
   ```bash
   cd dashboard
   python3 -m http.server 3002
   open http://localhost:3002/simple-dashboard-fixed.html
   ```

4. **Run the React dashboard (optional)**
   ```bash
   cd dashboard/frontend
   npm install
   npm start
   ```

## 📊 Dashboard Features

### Interactive Visualizations
- **Radar Charts**: Compare multiple cities across policy dimensions
- **Rankings**: Sortable city rankings by different metrics
- **Trend Analysis**: Historical performance tracking
- **Regional Comparisons**: Geographic performance patterns

### Data Management
- **Automated Scoring**: Standardized evaluation framework
- **Data Verification**: Citation tracking and source validation
- **Export Capabilities**: CSV and image export options

## 🏗️ Project Structure

```
├── cities/                    # City-specific data files
│   ├── atlanta/
│   ├── austin/
│   └── ...
├── dashboard/                 # Dashboard implementations
│   ├── frontend/             # React dashboard
│   ├── backend/              # FastAPI backend
│   └── simple-dashboard-fixed.html
├── docs/                     # Documentation
│   ├── methodology/
│   └── analysis/
├── scripts/                  # Data processing scripts
│   ├── data_processing/
│   ├── scoring/
│   └── visualization/
└── data/                     # Processed data outputs
    ├── processed/
    └── outputs/
```

## 📈 Key Findings

### Top Performing Cities
1. **New York City** (86.0) - Strong funding and policy implementation
2. **Los Angeles** (78.0) - Comprehensive housing supply initiatives
3. **Seattle** (78.5) - Excellent transparency and data access

### Key Insights
- **Funding disparities** vary significantly across cities
- **Policy implementation** shows strong correlation with outcomes
- **Transparency** remains a challenge for many municipalities

## 🛠️ Development

### Data Collection
The project uses a structured approach to collect and validate housing data:
- Official city government websites
- Housing authority reports
- Urban planning documents
- Reputable news sources

### Scoring Methodology
1. **Raw Score Assignment**: 0-100 scale based on collected data
2. **Normalization**: Standardized scoring across indicators
3. **Weighted Aggregation**: Category-specific weights applied
4. **Ranking**: Comparative performance assessment

## 📚 Documentation

- [Methodology](docs/methodology/Affordable%20Housing%20Indicators%20Across%20Major%20US%20Cities.md)
- [Human-Centered Design Exercises](Human-Centered_Design_Exercises.md)
- [Project Organization Summary](PROJECT_ORGANIZATION_SUMMARY.md)

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add some amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- Data sources from city governments and housing authorities
- Eviction Lab for eviction data
- Community organizations providing local insights

## 📞 Contact

For questions or collaboration opportunities, please open an issue or contact the project maintainers.

---

**Note**: This dashboard is designed for research and policy analysis purposes. Data should be verified with official sources before making policy decisions.
