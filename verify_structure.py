#!/usr/bin/env python3
"""
Verification script for project structure

This script verifies that the project has been properly organized and all
files are in their correct locations.
"""

import os
from pathlib import Path
from project_config import CITIES, INDICATOR_CATEGORIES, CITY_FOLDER_MAPPING

def verify_directory_structure():
    """Verify that all required directories exist"""
    required_dirs = [
        "docs/methodology",
        "docs/reports", 
        "docs/analysis",
        "data/raw",
        "data/processed",
        "data/outputs",
        "scripts/data_processing",
        "scripts/scoring",
        "scripts/verification",
        "scripts/visualization",
        "cities"
    ]
    
    missing_dirs = []
    for dir_path in required_dirs:
        if not os.path.exists(dir_path):
            missing_dirs.append(dir_path)
    
    if missing_dirs:
        print(f"❌ Missing directories: {missing_dirs}")
        return False
    else:
        print("✅ All required directories exist")
        return True

def verify_city_structure():
    """Verify that all city directories and files exist"""
    missing_cities = []
    missing_files = []
    
    for city in CITIES:
        city_folder = CITY_FOLDER_MAPPING.get(city, city.lower().replace(" ", "_"))
        city_dir = Path("cities") / city_folder
        
        if not city_dir.exists():
            missing_cities.append(city)
            continue
            
        # Check for required files
        for category in INDICATOR_CATEGORIES.keys():
            # Handle special cases for Los Angeles and New York City
            if city == "Los Angeles":
                prefix = "la"
            elif city == "New York City":
                prefix = "nyc"
            else:
                prefix = city_folder
            
            if category == "Funding":
                filename = f"{prefix}_housing_funding.md"
            elif category == "Housing Supply":
                filename = f"{prefix}_housing_supply.md"
            elif category == "Resident Stability":
                filename = f"{prefix}_resident_stability.md"
            elif category == "Policy Implementation":
                filename = f"{prefix}_policy_implementation.md"
            elif category == "Transparency/Data Access":
                filename = f"{prefix}_transparency_data_access.md"
            else:
                filename = f"{prefix}_{category.lower().replace(' ', '_')}.md"
            
            file_path = city_dir / filename
            if not file_path.exists():
                missing_files.append(f"{city}/{filename}")
    
    if missing_cities:
        print(f"❌ Missing city directories: {missing_cities}")
        return False
    
    if missing_files:
        print(f"❌ Missing city files: {missing_files}")
        return False
    
    print("✅ All city directories and files exist")
    return True

def verify_scripts():
    """Verify that all script files exist"""
    script_files = [
        "scripts/data_processing/process_all_cities.py",
        "scripts/data_processing/load_data.py",
        "scripts/data_processing/implement_citations.py",
        "scripts/scoring/score_cities.py",
        "scripts/scoring/enhanced_city_scorer.py",
        "scripts/scoring/demo_improved_scoring.py",
        "scripts/verification/verify_citations.py",
        "scripts/visualization/generate_heatmap.py",
        "scripts/visualization/generate_chart.py"
    ]
    
    missing_scripts = []
    for script in script_files:
        if not os.path.exists(script):
            missing_scripts.append(script)
    
    if missing_scripts:
        print(f"❌ Missing script files: {missing_scripts}")
        return False
    
    print("✅ All script files exist")
    return True

def verify_documentation():
    """Verify that all documentation files exist"""
    doc_files = [
        "docs/methodology/Affordable Housing Indicators Across Major US Cities.md",
        "docs/analysis/DATA_SOURCES_AND_APIS_ANALYSIS.md",
        "docs/analysis/SCORING_SYSTEM_IMPROVEMENTS.md",
        "README.md",
        "requirements.txt",
        "project_config.py"
    ]
    
    missing_docs = []
    for doc in doc_files:
        if not os.path.exists(doc):
            missing_docs.append(doc)
    
    if missing_docs:
        print(f"❌ Missing documentation files: {missing_docs}")
        return False
    
    print("✅ All documentation files exist")
    return True

def verify_data_files():
    """Verify that key data files exist"""
    data_files = [
        "data/processed/updated_normalized_scores.csv",
        "data/processed/complete_normalized_scores_with_citations.csv",
        "data/processed/normalized_scores.csv",
        "data/processed/overall_scores.csv"
    ]
    
    missing_data = []
    for data_file in data_files:
        if not os.path.exists(data_file):
            missing_data.append(data_file)
    
    if missing_data:
        print(f"❌ Missing data files: {missing_data}")
        return False
    
    print("✅ All key data files exist")
    return True

def main():
    """Main verification function"""
    print("🔍 Verifying project structure...")
    print("=" * 50)
    
    checks = [
        ("Directory Structure", verify_directory_structure),
        ("City Structure", verify_city_structure),
        ("Scripts", verify_scripts),
        ("Documentation", verify_documentation),
        ("Data Files", verify_data_files)
    ]
    
    all_passed = True
    for check_name, check_func in checks:
        print(f"\n📁 {check_name}:")
        if not check_func():
            all_passed = False
    
    print("\n" + "=" * 50)
    if all_passed:
        print("✅ Project structure verification completed successfully!")
        print("\nThe project has been properly organized with:")
        print(f"- {len(CITIES)} cities with complete data files")
        print(f"- {len(INDICATOR_CATEGORIES)} indicator categories")
        print("- Modular script organization")
        print("- Comprehensive documentation")
        print("- Structured data storage")
    else:
        print("❌ Project structure verification failed!")
        print("Please check the missing files and directories above.")

if __name__ == "__main__":
    main()
