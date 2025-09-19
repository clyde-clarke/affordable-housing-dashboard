import { CityData, RegionalData, DataQuality, Recommendation } from '../types';

// Mock data based on the actual CSV data from the project
export const mockCityData: CityData[] = [
  {
    city: 'New York City',
    funding: 95.0,
    housingSupply: 85.0,
    residentStability: 75.0,
    policyImplementation: 90.0,
    transparencyDataAccess: 85.0,
    overallScore: 86.0
  },
  {
    city: 'Los Angeles',
    funding: 85.0,
    housingSupply: 80.0,
    residentStability: 70.0,
    policyImplementation: 75.0,
    transparencyDataAccess: 80.0,
    overallScore: 78.0
  },
  {
    city: 'Chicago',
    funding: 45.0,
    housingSupply: 57.0,
    residentStability: 65.0,
    policyImplementation: 80.0,
    transparencyDataAccess: 100.0,
    overallScore: 58.3
  },
  {
    city: 'Houston',
    funding: 60.0,
    housingSupply: 70.0,
    residentStability: 55.0,
    policyImplementation: 65.0,
    transparencyDataAccess: 75.0,
    overallScore: 65.0
  },
  {
    city: 'Phoenix',
    funding: 50.0,
    housingSupply: 65.0,
    residentStability: 60.0,
    policyImplementation: 70.0,
    transparencyDataAccess: 80.0,
    overallScore: 61.0
  },
  {
    city: 'Philadelphia',
    funding: 70.0,
    housingSupply: 60.0,
    residentStability: 70.0,
    policyImplementation: 75.0,
    transparencyDataAccess: 85.0,
    overallScore: 70.0
  },
  {
    city: 'San Antonio',
    funding: 45.0,
    housingSupply: 55.0,
    residentStability: 50.0,
    policyImplementation: 60.0,
    transparencyDataAccess: 70.0,
    overallScore: 55.0
  },
  {
    city: 'San Diego',
    funding: 55.0,
    housingSupply: 60.0,
    residentStability: 65.0,
    policyImplementation: 70.0,
    transparencyDataAccess: 75.0,
    overallScore: 63.0
  },
  {
    city: 'Dallas',
    funding: 50.0,
    housingSupply: 65.0,
    residentStability: 55.0,
    policyImplementation: 60.0,
    transparencyDataAccess: 70.0,
    overallScore: 58.0
  },
  {
    city: 'San Jose',
    funding: 80.0,
    housingSupply: 75.0,
    residentStability: 70.0,
    policyImplementation: 85.0,
    transparencyDataAccess: 90.0,
    overallScore: 78.0
  },
  {
    city: 'Austin',
    funding: 75.0,
    housingSupply: 70.0,
    residentStability: 65.0,
    policyImplementation: 80.0,
    transparencyDataAccess: 85.0,
    overallScore: 73.0
  },
  {
    city: 'Jacksonville',
    funding: 40.0,
    housingSupply: 50.0,
    residentStability: 45.0,
    policyImplementation: 55.0,
    transparencyDataAccess: 60.0,
    overallScore: 49.0
  },
  {
    city: 'Fort Worth',
    funding: 35.0,
    housingSupply: 45.0,
    residentStability: 40.0,
    policyImplementation: 50.0,
    transparencyDataAccess: 55.0,
    overallScore: 44.0
  },
  {
    city: 'Columbus',
    funding: 50.0,
    housingSupply: 60.0,
    residentStability: 55.0,
    policyImplementation: 65.0,
    transparencyDataAccess: 70.0,
    overallScore: 58.0
  },
  {
    city: 'Charlotte',
    funding: 60.0,
    housingSupply: 65.0,
    residentStability: 60.0,
    policyImplementation: 70.0,
    transparencyDataAccess: 75.0,
    overallScore: 65.0
  },
  {
    city: 'Seattle',
    funding: 85.0,
    housingSupply: 80.0,
    residentStability: 75.0,
    policyImplementation: 85.0,
    transparencyDataAccess: 90.0,
    overallScore: 82.0
  },
  {
    city: 'Denver',
    funding: 70.0,
    housingSupply: 75.0,
    residentStability: 70.0,
    policyImplementation: 80.0,
    transparencyDataAccess: 85.0,
    overallScore: 74.0
  },
  {
    city: 'Washington DC',
    funding: 90.0,
    housingSupply: 85.0,
    residentStability: 80.0,
    policyImplementation: 90.0,
    transparencyDataAccess: 95.0,
    overallScore: 87.0
  },
  {
    city: 'Boston',
    funding: 80.0,
    housingSupply: 75.0,
    residentStability: 70.0,
    policyImplementation: 85.0,
    transparencyDataAccess: 80.0,
    overallScore: 77.0
  },
  {
    city: 'El Paso',
    funding: 30.0,
    housingSupply: 40.0,
    residentStability: 35.0,
    policyImplementation: 45.0,
    transparencyDataAccess: 50.0,
    overallScore: 39.0
  },
  {
    city: 'Detroit',
    funding: 55.0,
    housingSupply: 50.0,
    residentStability: 60.0,
    policyImplementation: 65.0,
    transparencyDataAccess: 70.0,
    overallScore: 58.0
  },
  {
    city: 'Nashville',
    funding: 45.0,
    housingSupply: 55.0,
    residentStability: 50.0,
    policyImplementation: 60.0,
    transparencyDataAccess: 65.0,
    overallScore: 54.0
  },
  {
    city: 'Memphis',
    funding: 35.0,
    housingSupply: 45.0,
    residentStability: 40.0,
    policyImplementation: 50.0,
    transparencyDataAccess: 55.0,
    overallScore: 44.0
  },
  {
    city: 'Portland',
    funding: 75.0,
    housingSupply: 80.0,
    residentStability: 75.0,
    policyImplementation: 85.0,
    transparencyDataAccess: 80.0,
    overallScore: 78.0
  }
];

export const mockRegionalData: RegionalData[] = [
  {
    region: 'Northeast',
    cities: ['New York City', 'Boston', 'Philadelphia'],
    averageScore: 77.7,
    totalFunding: 15.2,
    population: 12.5
  },
  {
    region: 'West Coast',
    cities: ['Los Angeles', 'San Francisco', 'Seattle', 'San Jose', 'San Diego'],
    averageScore: 75.6,
    totalFunding: 18.5,
    population: 15.8
  },
  {
    region: 'South',
    cities: ['Dallas', 'Houston', 'Atlanta', 'Miami', 'Jacksonville'],
    averageScore: 58.2,
    totalFunding: 8.9,
    population: 12.3
  },
  {
    region: 'Midwest',
    cities: ['Chicago', 'Detroit', 'Columbus'],
    averageScore: 58.1,
    totalFunding: 6.2,
    population: 8.1
  },
  {
    region: 'Southwest',
    cities: ['Phoenix', 'San Antonio', 'Austin', 'Fort Worth', 'Denver'],
    averageScore: 56.0,
    totalFunding: 7.8,
    population: 9.4
  }
];

export const mockDataQuality: DataQuality[] = mockCityData.map(city => ({
  city: city.city,
  completeness: Math.random() * 30 + 70, // 70-100%
  verificationStatus: Math.random() > 0.3 ? 'verified' : 'pending',
  sourceCount: Math.floor(Math.random() * 10) + 5,
  lastUpdated: new Date(Date.now() - Math.random() * 30 * 24 * 60 * 60 * 1000).toISOString()
}));

export const mockRecommendations: Recommendation[] = [
  {
    city: 'Fort Worth',
    priority: 'high',
    category: 'Funding',
    action: 'Increase housing budget allocation by 50%',
    targetScore: 60,
    currentScore: 35
  },
  {
    city: 'Memphis',
    priority: 'high',
    category: 'Housing Supply',
    action: 'Implement inclusionary zoning ordinance',
    targetScore: 65,
    currentScore: 45
  },
  {
    city: 'Jacksonville',
    priority: 'medium',
    category: 'Transparency',
    action: 'Launch public housing dashboard',
    targetScore: 80,
    currentScore: 60
  },
  {
    city: 'El Paso',
    priority: 'high',
    category: 'Policy Implementation',
    action: 'Strengthen rent control enforcement',
    targetScore: 70,
    currentScore: 45
  }
];
