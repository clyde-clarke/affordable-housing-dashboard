import { CityData } from '../types';

// This service will be used to load actual data from the CSV files
// For now, it uses mock data but can be easily extended to load real data

export class DataService {
  private static instance: DataService;
  private cityData: CityData[] = [];

  private constructor() {
    // Initialize with mock data
    this.loadMockData();
  }

  public static getInstance(): DataService {
    if (!DataService.instance) {
      DataService.instance = new DataService();
    }
    return DataService.instance;
  }

  private loadMockData(): void {
    // This will be replaced with actual CSV loading
    this.cityData = [
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
      // Add more cities as needed
    ];
  }

  public async loadCSVData(csvPath: string): Promise<void> {
    try {
      // This would load actual CSV data
      // For now, we'll use mock data
      console.log(`Loading data from ${csvPath}`);
      this.loadMockData();
    } catch (error) {
      console.error('Error loading CSV data:', error);
      throw error;
    }
  }

  public getCityData(): CityData[] {
    return this.cityData;
  }

  public getCityByName(cityName: string): CityData | undefined {
    return this.cityData.find(city => city.city === cityName);
  }

  public getTopCities(count: number = 10): CityData[] {
    return [...this.cityData]
      .sort((a, b) => b.overallScore - a.overallScore)
      .slice(0, count);
  }

  public getCitiesByCategory(category: keyof Omit<CityData, 'city' | 'overallScore'>, count: number = 10): CityData[] {
    return [...this.cityData]
      .sort((a, b) => b[category] - a[category])
      .slice(0, count);
  }

  public getAverageScore(): number {
    return this.cityData.reduce((sum, city) => sum + city.overallScore, 0) / this.cityData.length;
  }

  public getTotalFunding(): number {
    return this.cityData.reduce((sum, city) => sum + city.funding, 0);
  }

  public getPerformanceDistribution(): Array<{ name: string; value: number; color: string }> {
    const excellent = this.cityData.filter(city => city.overallScore >= 80).length;
    const good = this.cityData.filter(city => city.overallScore >= 60 && city.overallScore < 80).length;
    const fair = this.cityData.filter(city => city.overallScore >= 40 && city.overallScore < 60).length;
    const poor = this.cityData.filter(city => city.overallScore < 40).length;

    return [
      { name: 'Excellent (80-100)', value: excellent, color: '#28A745' },
      { name: 'Good (60-79)', value: good, color: '#2E86AB' },
      { name: 'Fair (40-59)', value: fair, color: '#FFC107' },
      { name: 'Poor (0-39)', value: poor, color: '#DC3545' }
    ];
  }
}

export default DataService;
