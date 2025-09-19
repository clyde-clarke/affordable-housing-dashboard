"""
FastAPI backend for Affordable Housing Dashboard

This backend serves data from the CSV files and provides API endpoints
for the React frontend dashboard.
"""

from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
import pandas as pd
import json
from pathlib import Path
from typing import List, Dict, Any
import os

app = FastAPI(
    title="Affordable Housing Dashboard API",
    description="API for serving affordable housing data to the React dashboard",
    version="1.0.0"
)

# Enable CORS for React frontend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000", "http://127.0.0.1:3000"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Data loading
def load_city_data() -> pd.DataFrame:
    """Load city data from CSV files"""
    try:
        # Try to load from the processed data directory
        csv_path = Path("../../data/processed/updated_normalized_scores.csv")
        if csv_path.exists():
            df = pd.read_csv(csv_path)
            return df
        else:
            # Fallback to mock data if CSV not found
            return create_mock_data()
    except Exception as e:
        print(f"Error loading data: {e}")
        return create_mock_data()

def create_mock_data() -> pd.DataFrame:
    """Create mock data if CSV files are not available"""
    mock_data = {
        'City': ['New York City', 'Los Angeles', 'Chicago', 'Houston', 'Phoenix'],
        'Funding': [95.0, 85.0, 45.0, 60.0, 50.0],
        'Housing Supply': [85.0, 80.0, 57.0, 70.0, 65.0],
        'Resident Stability': [75.0, 70.0, 65.0, 55.0, 60.0],
        'Policy Implementation': [90.0, 75.0, 80.0, 65.0, 70.0],
        'Transparency/Data Access': [85.0, 80.0, 100.0, 75.0, 80.0],
        'Overall Score': [86.0, 78.0, 58.3, 65.0, 61.0]
    }
    return pd.DataFrame(mock_data)

# Load data on startup
city_data = load_city_data()

@app.get("/")
async def root():
    """Root endpoint"""
    return {"message": "Affordable Housing Dashboard API", "version": "1.0.0"}

@app.get("/health")
async def health_check():
    """Health check endpoint"""
    return {"status": "healthy", "data_loaded": len(city_data) > 0}

@app.get("/cities")
async def get_cities() -> List[Dict[str, Any]]:
    """Get all cities data"""
    try:
        return city_data.to_dict('records')
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/cities/{city_name}")
async def get_city(city_name: str) -> Dict[str, Any]:
    """Get specific city data"""
    try:
        city_row = city_data[city_data['City'] == city_name]
        if city_row.empty:
            raise HTTPException(status_code=404, detail="City not found")
        return city_row.iloc[0].to_dict()
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/cities/top/{limit}")
async def get_top_cities(limit: int = 10) -> List[Dict[str, Any]]:
    """Get top performing cities by overall score"""
    try:
        top_cities = city_data.nlargest(limit, 'Overall Score')
        return top_cities.to_dict('records')
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/cities/category/{category}")
async def get_cities_by_category(category: str, limit: int = 10) -> List[Dict[str, Any]]:
    """Get cities ranked by specific category"""
    try:
        if category not in city_data.columns:
            raise HTTPException(status_code=400, detail="Invalid category")
        
        sorted_cities = city_data.nlargest(limit, category)
        return sorted_cities.to_dict('records')
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/stats/summary")
async def get_summary_stats() -> Dict[str, Any]:
    """Get summary statistics"""
    try:
        return {
            "total_cities": len(city_data),
            "average_overall_score": city_data['Overall Score'].mean(),
            "average_funding": city_data['Funding'].mean(),
            "average_housing_supply": city_data['Housing Supply'].mean(),
            "average_resident_stability": city_data['Resident Stability'].mean(),
            "average_policy_implementation": city_data['Policy Implementation'].mean(),
            "average_transparency": city_data['Transparency/Data Access'].mean(),
            "total_funding": city_data['Funding'].sum(),
            "best_city": city_data.loc[city_data['Overall Score'].idxmax(), 'City'],
            "best_score": city_data['Overall Score'].max()
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/stats/performance-distribution")
async def get_performance_distribution() -> List[Dict[str, Any]]:
    """Get performance distribution across score ranges"""
    try:
        excellent = len(city_data[city_data['Overall Score'] >= 80])
        good = len(city_data[(city_data['Overall Score'] >= 60) & (city_data['Overall Score'] < 80)])
        fair = len(city_data[(city_data['Overall Score'] >= 40) & (city_data['Overall Score'] < 60)])
        poor = len(city_data[city_data['Overall Score'] < 40])
        
        return [
            {"name": "Excellent (80-100)", "value": excellent, "color": "#28A745"},
            {"name": "Good (60-79)", "value": good, "color": "#2E86AB"},
            {"name": "Fair (40-59)", "value": fair, "color": "#FFC107"},
            {"name": "Poor (0-39)", "value": poor, "color": "#DC3545"}
        ]
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/regions")
async def get_regional_data() -> List[Dict[str, Any]]:
    """Get regional analysis data"""
    try:
        # Define regions based on city names
        regions = {
            'Northeast': ['New York City', 'Boston', 'Philadelphia'],
            'West Coast': ['Los Angeles', 'San Francisco', 'Seattle', 'San Jose', 'San Diego'],
            'South': ['Dallas', 'Houston', 'Atlanta', 'Miami', 'Jacksonville'],
            'Midwest': ['Chicago', 'Detroit', 'Columbus'],
            'Southwest': ['Phoenix', 'San Antonio', 'Austin', 'Fort Worth', 'Denver']
        }
        
        regional_data = []
        for region, cities in regions.items():
            region_cities = city_data[city_data['City'].isin(cities)]
            if not region_cities.empty:
                regional_data.append({
                    "region": region,
                    "cities": cities,
                    "average_score": region_cities['Overall Score'].mean(),
                    "total_funding": region_cities['Funding'].sum(),
                    "city_count": len(region_cities)
                })
        
        return regional_data
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
