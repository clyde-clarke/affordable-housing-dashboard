export interface CityData {
  city: string;
  funding: number;
  housingSupply: number;
  residentStability: number;
  policyImplementation: number;
  transparencyDataAccess: number;
  overallScore: number;
}

export interface IndicatorCategory {
  name: string;
  weight: number;
  color: string;
  description: string;
}

export interface MetricCard {
  title: string;
  value: string | number;
  subtitle?: string;
  color?: string;
  icon?: string;
}

export interface ChartData {
  name: string;
  value: number;
  color?: string;
  [key: string]: any;
}

export interface DashboardPage {
  id: string;
  title: string;
  subtitle: string;
  component: React.ComponentType;
}

export interface RegionalData {
  region: string;
  cities: string[];
  averageScore: number;
  totalFunding: number;
  population: number;
}

export interface DataQuality {
  city: string;
  completeness: number;
  verificationStatus: 'verified' | 'pending' | 'unverified';
  sourceCount: number;
  lastUpdated: string;
}

export interface Recommendation {
  city: string;
  priority: 'high' | 'medium' | 'low';
  category: string;
  action: string;
  targetScore: number;
  currentScore: number;
}

export const INDICATOR_CATEGORIES: IndicatorCategory[] = [
  {
    name: 'Funding',
    weight: 0.25,
    color: '#2E86AB',
    description: 'Financial commitment to affordable housing'
  },
  {
    name: 'Housing Supply',
    weight: 0.25,
    color: '#A23B72',
    description: 'Production and preservation of affordable units'
  },
  {
    name: 'Resident Stability',
    weight: 0.20,
    color: '#F18F01',
    description: 'Prevention of displacement and eviction'
  },
  {
    name: 'Policy Implementation',
    weight: 0.20,
    color: '#C73E1D',
    description: 'Enforcement of housing policies and regulations'
  },
  {
    name: 'Transparency/Data Access',
    weight: 0.10,
    color: '#7209B7',
    description: 'Public data availability and reporting'
  }
];

export const CITIES = [
  'Atlanta', 'Austin', 'Boston', 'Charlotte', 'Chicago', 'Columbus',
  'Dallas', 'Denver', 'Detroit', 'Fort Worth', 'Houston', 'Jacksonville',
  'Los Angeles', 'Miami', 'New Orleans', 'New York City', 'Philadelphia',
  'Phoenix', 'San Antonio', 'San Diego', 'San Francisco', 'San Jose',
  'Seattle', 'Washington DC'
];

export const REGIONS = {
  'Northeast': ['New York City', 'Boston', 'Philadelphia'],
  'West Coast': ['Los Angeles', 'San Francisco', 'Seattle', 'San Jose', 'San Diego'],
  'South': ['Dallas', 'Houston', 'Atlanta', 'Miami', 'Jacksonville'],
  'Midwest': ['Chicago', 'Detroit', 'Columbus'],
  'Southwest': ['Phoenix', 'San Antonio', 'Austin', 'Fort Worth', 'Denver']
};
