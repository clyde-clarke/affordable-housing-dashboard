# Affordable Housing Dashboard

An interactive React dashboard for visualizing affordable housing indicators across major US cities.

## Features

- **10 Comprehensive Dashboard Pages**: Executive Summary, Funding Analysis, Housing Supply, Resident Stability, Policy Implementation, Transparency & Data Access, Comparative Analysis, Regional Trends, Data Quality, and Recommendations
- **Interactive Visualizations**: Bar charts, pie charts, scatter plots, heatmaps, and progress bars
- **Responsive Design**: Optimized for desktop and tablet viewing
- **Real-time Data Integration**: Connects to CSV data sources from the main project
- **Consistent Design System**: 16:9 landscape orientation with standardized color palette

## Project Structure

```
dashboard/
├── frontend/                 # React application
│   ├── public/              # Static assets
│   ├── src/
│   │   ├── components/      # Reusable UI components
│   │   ├── pages/          # Dashboard pages
│   │   ├── services/       # Data services and API calls
│   │   ├── types/          # TypeScript type definitions
│   │   ├── data/           # Mock data and data utilities
│   │   └── styles/         # CSS styles and themes
│   ├── package.json        # Dependencies and scripts
│   └── README.md
└── backend/                # Future FastAPI backend (optional)
```

## Getting Started

### Prerequisites

- Node.js 16+ and npm
- Modern web browser

### Installation

1. **Navigate to the frontend directory:**
   ```bash
   cd dashboard/frontend
   ```

2. **Install dependencies:**
   ```bash
   npm install
   ```

3. **Start the development server:**
   ```bash
   npm start
   ```

4. **Open your browser:**
   Navigate to `http://localhost:3000`

### Building for Production

```bash
npm run build
```

This creates a `build` folder with optimized production files.

## Dashboard Pages

### 1. Executive Summary
- Top 10 performing cities
- Performance distribution across all cities
- Key findings and insights
- Quick statistics overview

### 2. Funding Analysis
- Funding score rankings
- Budget breakdown by source
- Per capita investment analysis
- Key funding highlights

### 3. Housing Supply
- Housing supply score rankings
- Production vs pipeline capacity
- Progress toward housing targets
- Supply highlights and metrics

### 4. Resident Stability
- Stability score rankings
- Eviction rates vs assistance spending
- Support services by city
- Stability highlights

### 5. Policy Implementation
- Policy implementation rankings
- Policy types by city
- Enforcement effectiveness
- Policy highlights

### 6. Transparency & Data Access
- Transparency score rankings
- Data availability by city
- Data freshness analysis
- Transparency highlights

### 7. Comparative Analysis
- Performance heatmap
- Multi-dimensional city comparison
- Performance consistency analysis
- Key comparisons

### 8. Regional Trends
- Regional performance analysis
- Metro size vs performance
- Regional specializations
- Regional highlights

### 9. Data Quality
- Data completeness by city
- Verification status
- Source quality analysis
- Quality highlights

### 10. Recommendations
- Priority action cities
- Improvement opportunities
- Best practices and success stories
- Action plan overview

## Design System

### Color Palette
- **Primary (Funding)**: #2E86AB (Blue)
- **Secondary (Housing Supply)**: #A23B72 (Purple)
- **Tertiary (Resident Stability)**: #F18F01 (Orange)
- **Quaternary (Policy Implementation)**: #C73E1D (Red)
- **Quinary (Transparency)**: #7209B7 (Violet)
- **Success**: #28A745 (Green)
- **Warning**: #FFC107 (Yellow)
- **Danger**: #DC3545 (Red)

### Typography
- **Font Family**: Inter, system fonts
- **Title**: 32px, Bold
- **Subtitle**: 24px, SemiBold
- **Body**: 16px, Regular
- **Caption**: 12px, Regular

### Layout
- **Aspect Ratio**: 16:9 (1920x1080px)
- **Grid System**: 3-column responsive layout
- **Spacing**: Consistent 2rem gaps
- **Border Radius**: 12px for cards, 8px for buttons

## Data Integration

### Current Implementation
- Uses mock data for demonstration
- Data service architecture ready for CSV integration
- TypeScript interfaces for type safety

### Future Integration
- Connect to actual CSV files from the main project
- Implement real-time data updates
- Add data validation and error handling
- Support for multiple data sources

## Customization

### Adding New Pages
1. Create a new component in `src/pages/`
2. Add the page to the navigation in `App.tsx`
3. Follow the established design patterns

### Modifying Visualizations
- All charts use Recharts library
- Consistent styling through CSS classes
- Responsive design considerations

### Updating Data
- Modify `src/data/mockData.ts` for mock data
- Update `src/services/dataService.ts` for real data integration
- Ensure data matches TypeScript interfaces

## Technical Stack

- **React 18** with TypeScript
- **Recharts** for data visualization
- **CSS3** for styling and responsive design
- **Axios** for API calls (future)
- **React Router** for navigation (future)

## Browser Support

- Chrome 90+
- Firefox 88+
- Safari 14+
- Edge 90+

## Performance

- Optimized bundle size
- Lazy loading for large datasets
- Responsive images and charts
- Efficient re-rendering

## Contributing

1. Follow the established code patterns
2. Use TypeScript for type safety
3. Maintain consistent styling
4. Test across different screen sizes
5. Update documentation as needed

## License

This project is part of the Affordable Housing Indicators analysis and follows the same license terms.
