import React from 'react';

const ComparativeAnalysis: React.FC = () => {
  return (
    <div className="dashboard-container">
      <div className="page-header">
        <h1 className="page-title">City-to-City Comparative Analysis</h1>
        <p className="page-subtitle">Side-by-Side Performance Comparison Across All Indicators</p>
      </div>
      <div className="grid-container">
        <div className="grid-item">
          <h3>Performance Heatmap</h3>
          <div className="loading">Chart coming soon...</div>
        </div>
        <div className="grid-item">
          <h3>Top 5 Cities - Multi-Dimensional View</h3>
          <div className="loading">Chart coming soon...</div>
        </div>
        <div className="grid-item">
          <h3>Performance Consistency Analysis</h3>
          <div className="loading">Chart coming soon...</div>
        </div>
      </div>
    </div>
  );
};

export default ComparativeAnalysis;
