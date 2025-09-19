import React from 'react';
import { BarChart, Bar, XAxis, YAxis, CartesianGrid, Tooltip, ResponsiveContainer, ComposedChart, Line, ProgressBar } from 'recharts';
import { mockCityData } from '../data/mockData';

const HousingSupply: React.FC = () => {
  // Prepare data for top 10 cities by housing supply score
  const top10HousingSupply = [...mockCityData]
    .sort((a, b) => b.housingSupply - a.housingSupply)
    .slice(0, 10);

  // Mock production vs pipeline data
  const productionPipelineData = [
    { city: 'New York City', unitsProduced: 15000, pipelineUnits: 25000, target: 20000 },
    { city: 'Los Angeles', city: 'Los Angeles', unitsProduced: 12000, pipelineUnits: 18000, target: 15000 },
    { city: 'Chicago', unitsProduced: 8000, pipelineUnits: 12000, target: 10000 },
    { city: 'Houston', unitsProduced: 6000, pipelineUnits: 9000, target: 8000 },
    { city: 'Phoenix', unitsProduced: 5000, pipelineUnits: 7500, target: 7000 },
    { city: 'Philadelphia', unitsProduced: 7000, pipelineUnits: 10000, target: 9000 },
    { city: 'San Antonio', unitsProduced: 3000, pipelineUnits: 5000, target: 4000 },
    { city: 'San Diego', unitsProduced: 4500, pipelineUnits: 6500, target: 6000 },
    { city: 'Dallas', unitsProduced: 4000, pipelineUnits: 6000, target: 5500 },
    { city: 'San Jose', unitsProduced: 5500, pipelineUnits: 8000, target: 7000 }
  ];

  // Mock target progress data
  const targetProgressData = [
    { city: 'New York City', progress: 75, target: 20000, current: 15000 },
    { city: 'Los Angeles', progress: 80, target: 15000, current: 12000 },
    { city: 'Chicago', progress: 80, target: 10000, current: 8000 },
    { city: 'Houston', progress: 75, target: 8000, current: 6000 },
    { city: 'Phoenix', progress: 71, target: 7000, current: 5000 },
    { city: 'Philadelphia', progress: 78, target: 9000, current: 7000 },
    { city: 'San Antonio', progress: 75, target: 4000, current: 3000 },
    { city: 'San Diego', progress: 75, target: 6000, current: 4500 },
    { city: 'Dallas', progress: 73, target: 5500, current: 4000 },
    { city: 'San Jose', progress: 79, target: 7000, current: 5500 }
  ];

  // Calculate key metrics
  const mostUnitsProduced = Math.max(...productionPipelineData.map(p => p.unitsProduced));
  const mostUnitsCity = productionPipelineData.find(p => p.unitsProduced === mostUnitsProduced)?.city;
  const largestPipeline = Math.max(...productionPipelineData.map(p => p.pipelineUnits));
  const largestPipelineCity = productionPipelineData.find(p => p.pipelineUnits === largestPipeline)?.city;
  const averageTargetAchievement = targetProgressData.reduce((sum, t) => sum + t.progress, 0) / targetProgressData.length;
  const totalPipelineUnits = productionPipelineData.reduce((sum, p) => sum + p.pipelineUnits, 0);

  return (
    <div className="dashboard-container">
      {/* Header */}
      <div className="page-header">
        <h1 className="page-title">Housing Supply Analysis</h1>
        <p className="page-subtitle">Unit Production, Pipeline, and Progress Toward Targets</p>
      </div>

      {/* Main Content */}
      <div className="grid-container">
        {/* Left Column - Unit Production Leaders */}
        <div className="grid-item">
          <h3>Housing Supply Score Rankings</h3>
          <div className="chart-container">
            <ResponsiveContainer width="100%" height={400}>
              <BarChart data={top10HousingSupply} layout="horizontal">
                <CartesianGrid strokeDasharray="3 3" />
                <XAxis type="number" domain={[0, 100]} />
                <YAxis dataKey="city" type="category" width={120} />
                <Tooltip 
                  formatter={(value: number) => [`${value.toFixed(1)}`, 'Housing Supply Score']}
                  labelStyle={{ color: '#2C3E50' }}
                />
                <Bar 
                  dataKey="housingSupply" 
                  fill="#A23B72"
                  radius={[0, 4, 4, 0]}
                />
              </BarChart>
            </ResponsiveContainer>
          </div>
        </div>

        {/* Center Column - Production vs Pipeline */}
        <div className="grid-item">
          <h3>Production vs Pipeline Capacity</h3>
          <div className="chart-container">
            <ResponsiveContainer width="100%" height={400}>
              <ComposedChart data={productionPipelineData.slice(0, 8)}>
                <CartesianGrid strokeDasharray="3 3" />
                <XAxis dataKey="city" angle={-45} textAnchor="end" height={100} />
                <YAxis />
                <Tooltip 
                  formatter={(value: number, name: string) => [
                    `${value.toLocaleString()}`, 
                    name === 'unitsProduced' ? 'Units Produced' : 'Pipeline Units'
                  ]}
                />
                <Bar dataKey="unitsProduced" fill="#A23B72" name="Units Produced" />
                <Line 
                  type="monotone" 
                  dataKey="pipelineUnits" 
                  stroke="#7A2B5A" 
                  strokeWidth={3}
                  name="Pipeline Units"
                />
              </ComposedChart>
            </ResponsiveContainer>
          </div>
        </div>

        {/* Right Column - Target Progress */}
        <div className="grid-item">
          <h3>Progress Toward Housing Targets</h3>
          <div className="space-y-4">
            {targetProgressData.slice(0, 8).map((item, index) => (
              <div key={index} className="mb-4">
                <div className="flex justify-between items-center mb-2">
                  <span className="text-sm font-medium">{item.city}</span>
                  <span className="text-sm text-gray-600">{item.progress}%</span>
                </div>
                <div className="w-full bg-gray-200 rounded-full h-2">
                  <div 
                    className="bg-gradient-to-r from-red-500 via-yellow-500 to-green-500 h-2 rounded-full transition-all duration-300"
                    style={{ width: `${item.progress}%` }}
                  ></div>
                </div>
                <div className="flex justify-between text-xs text-gray-500 mt-1">
                  <span>{item.current.toLocaleString()} units</span>
                  <span>Target: {item.target.toLocaleString()}</span>
                </div>
              </div>
            ))}
          </div>
        </div>
      </div>

      {/* Bottom Section - Supply Highlights */}
      <div className="grid-container">
        <div className="metric-card">
          <div className="metric-value">{mostUnitsProduced.toLocaleString()}</div>
          <div className="metric-label">Most Units Produced</div>
          <div className="text-sm text-gray-600 mt-1">{mostUnitsCity}</div>
        </div>
        <div className="metric-card">
          <div className="metric-value">{largestPipeline.toLocaleString()}</div>
          <div className="metric-label">Largest Pipeline</div>
          <div className="text-sm text-gray-600 mt-1">{largestPipelineCity}</div>
        </div>
        <div className="metric-card">
          <div className="metric-value">{averageTargetAchievement.toFixed(1)}%</div>
          <div className="metric-label">Target Achievement Rate</div>
          <div className="text-sm text-gray-600 mt-1">Average across cities</div>
        </div>
        <div className="metric-card">
          <div className="metric-value">{totalPipelineUnits.toLocaleString()}</div>
          <div className="metric-label">Total Units in Pipeline</div>
          <div className="text-sm text-gray-600 mt-1">Future production capacity</div>
        </div>
      </div>
    </div>
  );
};

export default HousingSupply;
