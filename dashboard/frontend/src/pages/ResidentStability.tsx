import React from 'react';

const ResidentStability: React.FC = () => {
  return (
    <div className="dashboard-container">
      <div className="page-header">
        <h1 className="page-title">Resident Stability Analysis</h1>
        <p className="page-subtitle">Eviction Rates, Rental Assistance, and Homelessness Prevention</p>
      </div>
      <div className="grid-container">
        <div className="grid-item">
          <h3>Resident Stability Score Rankings</h3>
          <div className="loading">Chart coming soon...</div>
        </div>
        <div className="grid-item">
          <h3>Eviction Rates vs Assistance Spending</h3>
          <div className="loading">Chart coming soon...</div>
        </div>
        <div className="grid-item">
          <h3>Support Services by City</h3>
          <div className="loading">Chart coming soon...</div>
        </div>
      </div>
    </div>
  );
};

export default ResidentStability;
