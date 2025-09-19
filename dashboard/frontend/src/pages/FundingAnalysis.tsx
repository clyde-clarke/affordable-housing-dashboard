import React from 'react';
import { BarChart, Bar, XAxis, YAxis, CartesianGrid, Tooltip, ResponsiveContainer, ScatterChart, Scatter, ComposedChart, Line, LineChart } from 'recharts';
import { mockCityData } from '../data/mockData';

const FundingAnalysis: React.FC = () => {
  // Prepare data for top 10 cities by funding score
  const top10Funding = [...mockCityData]
    .sort((a, b) => b.funding - a.funding)
    .slice(0, 10);

  // Mock funding sources data
  const fundingSources = [
    { city: 'New York City', cityBudget: 2000, bondMeasures: 500, federalFunding: 300, trustFunds: 200 },
    { city: 'Los Angeles', cityBudget: 1500, bondMeasures: 400, federalFunding: 250, trustFunds: 150 },
    { city: 'Chicago', cityBudget: 800, bondMeasures: 200, federalFunding: 150, trustFunds: 100 },
    { city: 'Houston', cityBudget: 600, bondMeasures: 150, federalFunding: 100, trustFunds: 80 },
    { city: 'Phoenix', cityBudget: 500, bondMeasures: 100, federalFunding: 80, trustFunds: 60 },
    { city: 'Philadelphia', cityBudget: 700, bondMeasures: 180, federalFunding: 120, trustFunds: 90 },
    { city: 'San Antonio', cityBudget: 300, bondMeasures: 80, federalFunding: 60, trustFunds: 40 },
    { city: 'San Diego', cityBudget: 550, bondMeasures: 120, federalFunding: 90, trustFunds: 70 },
    { city: 'Dallas', cityBudget: 400, bondMeasures: 100, federalFunding: 70, trustFunds: 50 },
    { city: 'San Jose', cityBudget: 800, bondMeasures: 200, federalFunding: 150, trustFunds: 120 }
  ];

  // Mock per capita data
  const perCapitaData = [
    { city: 'New York City', population: 8.3, perCapita: 361, totalFunding: 3000, fundingScore: 95 },
    { city: 'Los Angeles', population: 4.0, perCapita: 575, totalFunding: 2300, fundingScore: 85 },
    { city: 'Chicago', population: 2.7, perCapita: 463, totalFunding: 1250, fundingScore: 45 },
    { city: 'Houston', population: 2.3, perCapita: 348, totalFunding: 800, fundingScore: 60 },
    { city: 'Phoenix', population: 1.6, perCapita: 500, totalFunding: 800, fundingScore: 50 },
    { city: 'Philadelphia', population: 1.6, perCapita: 681, totalFunding: 1090, fundingScore: 70 },
    { city: 'San Antonio', population: 1.5, perCapita: 320, totalFunding: 480, fundingScore: 45 },
    { city: 'San Diego', population: 1.4, perCapita: 529, totalFunding: 740, fundingScore: 55 },
    { city: 'Dallas', population: 1.3, perCapita: 400, totalFunding: 520, fundingScore: 50 },
    { city: 'San Jose', population: 1.0, perCapita: 1270, totalFunding: 1270, fundingScore: 80 }
  ];

  // Calculate key metrics
  const largestAllocation = Math.max(...fundingSources.map(f => f.cityBudget));
  const largestAllocationCity = fundingSources.find(f => f.cityBudget === largestAllocation)?.city;
  const highestPerCapita = Math.max(...perCapitaData.map(p => p.perCapita));
  const highestPerCapitaCity = perCapitaData.find(p => p.perCapita === highestPerCapita)?.city;
  const totalIdentifiedFunding = fundingSources.reduce((sum, f) => sum + f.cityBudget + f.bondMeasures + f.federalFunding + f.trustFunds, 0);

  return (
    <div className="dashboard-container">
      {/* Header */}
      <div className="page-header">
        <h1 className="page-title">Affordable Housing Funding Analysis</h1>
        <p className="page-subtitle">Budget Allocations, Bond Measures, and Per Capita Investments</p>
      </div>

      {/* Main Content */}
      <div className="grid-container">
        {/* Left Column - Top Funders */}
        <div className="grid-item">
          <h3>Funding Score Rankings</h3>
          <div className="chart-container">
            <ResponsiveContainer width="100%" height={400}>
              <BarChart data={top10Funding} layout="horizontal">
                <CartesianGrid strokeDasharray="3 3" />
                <XAxis type="number" domain={[0, 100]} />
                <YAxis dataKey="city" type="category" width={120} />
                <Tooltip 
                  formatter={(value: number) => [`${value.toFixed(1)}`, 'Funding Score']}
                  labelStyle={{ color: '#2C3E50' }}
                />
                <Bar 
                  dataKey="funding" 
                  fill="#2E86AB"
                  radius={[0, 4, 4, 0]}
                />
              </BarChart>
            </ResponsiveContainer>
          </div>
        </div>

        {/* Center Column - Budget Breakdown */}
        <div className="grid-item">
          <h3>Funding Sources by City</h3>
          <div className="chart-container">
            <ResponsiveContainer width="100%" height={400}>
              <ComposedChart data={fundingSources.slice(0, 8)}>
                <CartesianGrid strokeDasharray="3 3" />
                <XAxis dataKey="city" angle={-45} textAnchor="end" height={100} />
                <YAxis />
                <Tooltip 
                  formatter={(value: number, name: string) => [`$${value}M`, name]}
                />
                <Bar dataKey="cityBudget" stackId="a" fill="#2E86AB" name="City Budget" />
                <Bar dataKey="bondMeasures" stackId="a" fill="#1E5F7A" name="Bond Measures" />
                <Bar dataKey="federalFunding" stackId="a" fill="#4A9FD1" name="Federal Funding" />
                <Bar dataKey="trustFunds" stackId="a" fill="#7BB3D9" name="Trust Funds" />
              </ComposedChart>
            </ResponsiveContainer>
          </div>
        </div>

        {/* Right Column - Per Capita Analysis */}
        <div className="grid-item">
          <h3>Per Capita Investment vs Population</h3>
          <div className="chart-container">
            <ResponsiveContainer width="100%" height={400}>
              <ScatterChart data={perCapitaData}>
                <CartesianGrid strokeDasharray="3 3" />
                <XAxis dataKey="population" name="Population (M)" />
                <YAxis dataKey="perCapita" name="Per Capita ($)" />
                <Tooltip 
                  cursor={{ strokeDasharray: '3 3' }}
                  formatter={(value: number, name: string) => [
                    name === 'population' ? `${value}M` : `$${value}`,
                    name === 'population' ? 'Population' : 'Per Capita Investment'
                  ]}
                />
                <Scatter 
                  dataKey="perCapita" 
                  fill="#2E86AB"
                  r={6}
                />
              </ScatterChart>
            </ResponsiveContainer>
          </div>
        </div>
      </div>

      {/* Bottom Section - Key Funding Highlights */}
      <div className="grid-container">
        <div className="metric-card">
          <div className="metric-value">${largestAllocation}M</div>
          <div className="metric-label">Largest Single Allocation</div>
          <div className="text-sm text-gray-600 mt-1">{largestAllocationCity}</div>
        </div>
        <div className="metric-card">
          <div className="metric-value">${highestPerCapita}</div>
          <div className="metric-label">Highest Per Capita</div>
          <div className="text-sm text-gray-600 mt-1">{highestPerCapitaCity}</div>
        </div>
        <div className="metric-card">
          <div className="metric-value">8</div>
          <div className="metric-label">Cities with Bond Measures</div>
          <div className="text-sm text-gray-600 mt-1">Active bond programs</div>
        </div>
        <div className="metric-card">
          <div className="metric-value">${totalIdentifiedFunding.toFixed(0)}M</div>
          <div className="metric-label">Total Identified Funding</div>
          <div className="text-sm text-gray-600 mt-1">Across all sources</div>
        </div>
      </div>
    </div>
  );
};

export default FundingAnalysis;
