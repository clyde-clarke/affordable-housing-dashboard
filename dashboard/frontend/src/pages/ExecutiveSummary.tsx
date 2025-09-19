import React from 'react';
import { BarChart, Bar, XAxis, YAxis, CartesianGrid, Tooltip, ResponsiveContainer, PieChart, Pie, Cell } from 'recharts';
import { mockCityData } from '../data/mockData';

const ExecutiveSummary: React.FC = () => {
  // Prepare data for top 10 cities
  const top10Cities = [...mockCityData]
    .sort((a, b) => b.overallScore - a.overallScore)
    .slice(0, 10);

  // Prepare data for performance distribution
  const performanceDistribution = [
    { name: 'Excellent (80-100)', value: mockCityData.filter(city => city.overallScore >= 80).length, color: '#28A745' },
    { name: 'Good (60-79)', value: mockCityData.filter(city => city.overallScore >= 60 && city.overallScore < 80).length, color: '#2E86AB' },
    { name: 'Fair (40-59)', value: mockCityData.filter(city => city.overallScore >= 40 && city.overallScore < 60).length, color: '#FFC107' },
    { name: 'Poor (0-39)', value: mockCityData.filter(city => city.overallScore < 40).length, color: '#DC3545' }
  ];

  // Calculate key metrics
  const averageScore = mockCityData.reduce((sum, city) => sum + city.overallScore, 0) / mockCityData.length;
  const totalFunding = mockCityData.reduce((sum, city) => sum + city.funding, 0);
  const citiesWithCompleteData = mockCityData.length;

  return (
    <div className="dashboard-container">
      {/* Header */}
      <div className="page-header">
        <h1 className="page-title">Affordable Housing Performance Across Major US Cities</h1>
        <p className="page-subtitle">Comprehensive Analysis of 24 Cities Across 5 Key Indicators</p>
        <p className="page-date">January 2025</p>
      </div>

      {/* Main Content */}
      <div className="grid-container">
        {/* Left Column - Overall Rankings */}
        <div className="grid-item">
          <h3>Top 10 Performing Cities</h3>
          <div className="chart-container">
            <ResponsiveContainer width="100%" height={400}>
              <BarChart data={top10Cities} layout="horizontal">
                <CartesianGrid strokeDasharray="3 3" />
                <XAxis type="number" domain={[0, 100]} />
                <YAxis dataKey="city" type="category" width={120} />
                <Tooltip 
                  formatter={(value: number) => [`${value.toFixed(1)}`, 'Overall Score']}
                  labelStyle={{ color: '#2C3E50' }}
                />
                <Bar 
                  dataKey="overallScore" 
                  fill="#2E86AB"
                  radius={[0, 4, 4, 0]}
                />
              </BarChart>
            </ResponsiveContainer>
          </div>
        </div>

        {/* Center Column - Score Distribution */}
        <div className="grid-item">
          <h3>Performance Distribution</h3>
          <div className="chart-container">
            <ResponsiveContainer width="100%" height={400}>
              <PieChart>
                <Pie
                  data={performanceDistribution}
                  cx="50%"
                  cy="50%"
                  innerRadius={60}
                  outerRadius={120}
                  paddingAngle={5}
                  dataKey="value"
                >
                  {performanceDistribution.map((entry, index) => (
                    <Cell key={`cell-${index}`} fill={entry.color} />
                  ))}
                </Pie>
                <Tooltip 
                  formatter={(value: number, name: string) => [
                    `${value} cities (${((value / mockCityData.length) * 100).toFixed(1)}%)`, 
                    name
                  ]}
                />
              </PieChart>
            </ResponsiveContainer>
          </div>
          <div className="mt-4">
            {performanceDistribution.map((item, index) => (
              <div key={index} className="flex items-center mb-2">
                <div 
                  className="w-4 h-4 rounded mr-2" 
                  style={{ backgroundColor: item.color }}
                ></div>
                <span className="text-sm">{item.name}: {item.value} cities</span>
              </div>
            ))}
          </div>
        </div>

        {/* Right Column - Key Insights */}
        <div className="grid-item">
          <h3>Key Findings</h3>
          <div className="space-y-4">
            <div className="flex items-start">
              <div className="w-2 h-2 bg-primary rounded-full mt-2 mr-3"></div>
              <div>
                <p className="font-medium">NYC leads with highest overall score</p>
                <p className="text-sm text-gray-600">86.0 overall score with $2B annual budget</p>
              </div>
            </div>
            <div className="flex items-start">
              <div className="w-2 h-2 bg-secondary rounded-full mt-2 mr-3"></div>
              <div>
                <p className="font-medium">West Coast cities show strong performance</p>
                <p className="text-sm text-gray-600">Average 75.6 score across 5 cities</p>
              </div>
            </div>
            <div className="flex items-start">
              <div className="w-2 h-2 bg-tertiary rounded-full mt-2 mr-3"></div>
              <div>
                <p className="font-medium">Transparency scores vary widely</p>
                <p className="text-sm text-gray-600">Range from 50% to 100% across cities</p>
              </div>
            </div>
            <div className="flex items-start">
              <div className="w-2 h-2 bg-quaternary rounded-full mt-2 mr-3"></div>
              <div>
                <p className="font-medium">Policy implementation needs improvement</p>
                <p className="text-sm text-gray-600">Average score of 68.5 across all cities</p>
              </div>
            </div>
          </div>
        </div>
      </div>

      {/* Bottom Section - Quick Stats */}
      <div className="grid-container">
        <div className="metric-card">
          <div className="metric-value">{mockCityData.length}</div>
          <div className="metric-label">Total Cities Analyzed</div>
        </div>
        <div className="metric-card">
          <div className="metric-value">{averageScore.toFixed(1)}</div>
          <div className="metric-label">Average Overall Score</div>
        </div>
        <div className="metric-card">
          <div className="metric-value">${totalFunding.toFixed(1)}B</div>
          <div className="metric-label">Total Funding Identified</div>
        </div>
        <div className="metric-card">
          <div className="metric-value">{citiesWithCompleteData}</div>
          <div className="metric-label">Cities with Complete Data</div>
        </div>
      </div>
    </div>
  );
};

export default ExecutiveSummary;
