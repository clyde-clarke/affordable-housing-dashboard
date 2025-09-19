import React, { useState } from 'react';
import Navigation from './components/Navigation';
import ExecutiveSummary from './pages/ExecutiveSummary';
import FundingAnalysis from './pages/FundingAnalysis';
import HousingSupply from './pages/HousingSupply';
import ResidentStability from './pages/ResidentStability';
import PolicyImplementation from './pages/PolicyImplementation';
import TransparencyDataAccess from './pages/TransparencyDataAccess';
import ComparativeAnalysis from './pages/ComparativeAnalysis';
import RegionalTrends from './pages/RegionalTrends';
import DataQuality from './pages/DataQuality';
import Recommendations from './pages/Recommendations';

const App: React.FC = () => {
  const [currentPage, setCurrentPage] = useState('executive-summary');

  const pages = [
    { id: 'executive-summary', title: 'Executive Summary', component: ExecutiveSummary },
    { id: 'funding-analysis', title: 'Funding Analysis', component: FundingAnalysis },
    { id: 'housing-supply', title: 'Housing Supply', component: HousingSupply },
    { id: 'resident-stability', title: 'Resident Stability', component: ResidentStability },
    { id: 'policy-implementation', title: 'Policy Implementation', component: PolicyImplementation },
    { id: 'transparency-data-access', title: 'Transparency & Data Access', component: TransparencyDataAccess },
    { id: 'comparative-analysis', title: 'Comparative Analysis', component: ComparativeAnalysis },
    { id: 'regional-trends', title: 'Regional Trends', component: RegionalTrends },
    { id: 'data-quality', title: 'Data Quality', component: DataQuality },
    { id: 'recommendations', title: 'Recommendations', component: Recommendations }
  ];

  const CurrentComponent = pages.find(page => page.id === currentPage)?.component || ExecutiveSummary;

  return (
    <div className="dashboard-container">
      <Navigation 
        pages={pages} 
        currentPage={currentPage} 
        onPageChange={setCurrentPage} 
      />
      <CurrentComponent />
    </div>
  );
};

export default App;
