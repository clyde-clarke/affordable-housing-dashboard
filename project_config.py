"""
Project Configuration for Affordable Housing Indicators Analysis

This module contains configuration settings, constants, and paths used throughout
the project for consistent data processing and analysis.
"""

import os
from pathlib import Path

# Project root directory
PROJECT_ROOT = Path(__file__).parent

# Data directories
DATA_DIR = PROJECT_ROOT / "data"
RAW_DATA_DIR = DATA_DIR / "raw"
PROCESSED_DATA_DIR = DATA_DIR / "processed"
OUTPUTS_DIR = DATA_DIR / "outputs"

# Scripts directories
SCRIPTS_DIR = PROJECT_ROOT / "scripts"
DATA_PROCESSING_DIR = SCRIPTS_DIR / "data_processing"
SCORING_DIR = SCRIPTS_DIR / "scoring"
VERIFICATION_DIR = SCRIPTS_DIR / "verification"
VISUALIZATION_DIR = SCRIPTS_DIR / "visualization"

# Documentation directories
DOCS_DIR = PROJECT_ROOT / "docs"
METHODOLOGY_DIR = DOCS_DIR / "methodology"
REPORTS_DIR = DOCS_DIR / "reports"
ANALYSIS_DIR = DOCS_DIR / "analysis"

# Cities directory
CITIES_DIR = PROJECT_ROOT / "cities"

# Indicator categories and weights
INDICATOR_CATEGORIES = {
    "Funding": 0.25,
    "Housing Supply": 0.25,
    "Resident Stability": 0.20,
    "Policy Implementation": 0.20,
    "Transparency/Data Access": 0.10
}

# Cities included in the analysis
CITIES = [
    "Atlanta", "Austin", "Boston", "Charlotte", "Chicago", "Columbus",
    "Dallas", "Denver", "Detroit", "Fort Worth", "Houston", "Jacksonville",
    "Los Angeles", "Miami", "New Orleans", "New York City", "Philadelphia",
    "Phoenix", "San Antonio", "San Diego", "San Francisco", "San Jose",
    "Seattle", "Washington DC"
]

# City folder mapping (for file organization)
CITY_FOLDER_MAPPING = {
    "Atlanta": "atlanta",
    "Austin": "austin",
    "Boston": "boston",
    "Charlotte": "charlotte",
    "Chicago": "chicago",
    "Columbus": "columbus",
    "Dallas": "dallas",
    "Denver": "denver",
    "Detroit": "detroit",
    "Fort Worth": "fort_worth",
    "Houston": "houston",
    "Jacksonville": "jacksonville",
    "Los Angeles": "los_angeles",
    "Miami": "miami",
    "New Orleans": "new_orleans",
    "New York City": "new_york_city",
    "Philadelphia": "philadelphia",
    "Phoenix": "phoenix",
    "San Antonio": "san_antonio",
    "San Diego": "san_diego",
    "San Francisco": "san_francisco",
    "San Jose": "san_jose",
    "Seattle": "seattle",
    "Washington DC": "washington_dc"
}

# File naming patterns
CITY_FILE_PATTERNS = {
    "Funding": "{}_housing_funding.md",
    "Housing Supply": "{}_housing_supply.md",
    "Resident Stability": "{}_resident_stability.md",
    "Policy Implementation": "{}_policy_implementation.md",
    "Transparency/Data Access": "{}_transparency_data_access.md"
}

# Scoring parameters
SCORING_CONFIG = {
    "min_score": 0,
    "max_score": 100,
    "normalization_method": "min_max",
    "weighted_aggregation": True
}

# Data source categories
DATA_SOURCE_CATEGORIES = {
    "federal": ["HUD", "Census Bureau", "Eviction Lab"],
    "state": ["California HCD", "Texas Demographics", "NYS HCR"],
    "city": ["Open Data Portals", "City Dashboards", "Budget Documents"],
    "academic": ["NYU Furman Center", "Terner Center", "HousingWorks Austin"],
    "nonprofit": ["New York Housing Conference", "Enterprise Community Partners"]
}

# Visualization settings
VISUALIZATION_CONFIG = {
    "default_figsize": (12, 8),
    "color_palette": "viridis",
    "dpi": 300,
    "format": "png"
}

# API endpoints and data sources
API_ENDPOINTS = {
    "hud": "https://hud.gov",
    "census": "https://census.gov",
    "eviction_lab": "https://evictionlab.org",
    "austin_data": "https://data.austintexas.gov",
    "charlotte_data": "https://data.charlottenc.gov",
    "nyc_data": "https://data.cityofnewyork.us",
    "la_data": "https://data.lacity.org",
    "seattle_data": "https://data.seattle.gov"
}

def get_city_file_path(city: str, category: str) -> Path:
    """Get the file path for a specific city and category."""
    city_folder = CITY_FOLDER_MAPPING.get(city, city.lower().replace(" ", "_"))
    filename = CITY_FILE_PATTERNS[category].format(city_folder)
    return CITIES_DIR / city_folder / filename

def get_output_path(filename: str) -> Path:
    """Get the output path for generated files."""
    return OUTPUTS_DIR / filename

def get_processed_data_path(filename: str) -> Path:
    """Get the processed data path for CSV files."""
    return PROCESSED_DATA_DIR / filename

def ensure_directories():
    """Ensure all required directories exist."""
    directories = [
        DATA_DIR, RAW_DATA_DIR, PROCESSED_DATA_DIR, OUTPUTS_DIR,
        SCRIPTS_DIR, DATA_PROCESSING_DIR, SCORING_DIR, VERIFICATION_DIR, VISUALIZATION_DIR,
        DOCS_DIR, METHODOLOGY_DIR, REPORTS_DIR, ANALYSIS_DIR,
        CITIES_DIR
    ]
    
    for directory in directories:
        directory.mkdir(parents=True, exist_ok=True)
    
    # Create city subdirectories
    for city_folder in CITY_FOLDER_MAPPING.values():
        (CITIES_DIR / city_folder).mkdir(parents=True, exist_ok=True)

if __name__ == "__main__":
    ensure_directories()
    print("Project directories created successfully!")
