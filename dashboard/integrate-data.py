#!/usr/bin/env python3
"""
Data Integration Script for Dashboard

This script copies the latest CSV data from the main project
to the dashboard backend for real-time updates.
"""

import shutil
import os
from pathlib import Path

def integrate_data():
    """Copy CSV data from main project to dashboard"""
    # Source paths
    source_dir = Path("../data/processed")
    target_dir = Path("backend")
    
    # CSV files to copy
    csv_files = [
        "updated_normalized_scores.csv",
        "complete_normalized_scores_with_citations.csv",
        "normalized_scores.csv",
        "overall_scores.csv"
    ]
    
    print("🔄 Integrating data from main project...")
    
    for csv_file in csv_files:
        source_path = source_dir / csv_file
        target_path = target_dir / csv_file
        
        if source_path.exists():
            shutil.copy2(source_path, target_path)
            print(f"✅ Copied {csv_file}")
        else:
            print(f"⚠️  {csv_file} not found in source directory")
    
    print("✅ Data integration completed!")

if __name__ == "__main__":
    integrate_data()
