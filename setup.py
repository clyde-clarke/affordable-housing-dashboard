"""
Setup script for Affordable Housing Indicators Analysis Project

This script initializes the project environment and installs required dependencies.
"""

import subprocess
import sys
from pathlib import Path

def install_requirements():
    """Install required packages from requirements.txt"""
    try:
        subprocess.check_call([sys.executable, "-m", "pip", "install", "-r", "requirements.txt"])
        print("✅ Requirements installed successfully!")
    except subprocess.CalledProcessError as e:
        print(f"❌ Error installing requirements: {e}")
        return False
    return True

def setup_project_structure():
    """Set up the project directory structure"""
    try:
        from project_config import ensure_directories
        ensure_directories()
        print("✅ Project structure created successfully!")
    except ImportError as e:
        print(f"❌ Error setting up project structure: {e}")
        return False
    return True

def verify_installation():
    """Verify that all required packages are installed"""
    required_packages = [
        "pandas", "numpy", "matplotlib", "seaborn", "plotly", "requests"
    ]
    
    missing_packages = []
    for package in required_packages:
        try:
            __import__(package)
        except ImportError:
            missing_packages.append(package)
    
    if missing_packages:
        print(f"❌ Missing packages: {', '.join(missing_packages)}")
        return False
    else:
        print("✅ All required packages are installed!")
        return True

def main():
    """Main setup function"""
    print("🚀 Setting up Affordable Housing Indicators Analysis Project...")
    print("=" * 60)
    
    # Install requirements
    print("\n📦 Installing required packages...")
    if not install_requirements():
        print("❌ Setup failed during package installation")
        return False
    
    # Set up project structure
    print("\n📁 Setting up project structure...")
    if not setup_project_structure():
        print("❌ Setup failed during project structure creation")
        return False
    
    # Verify installation
    print("\n🔍 Verifying installation...")
    if not verify_installation():
        print("❌ Setup failed during verification")
        return False
    
    print("\n" + "=" * 60)
    print("✅ Project setup completed successfully!")
    print("\nNext steps:")
    print("1. Run the data processing scripts in scripts/data_processing/")
    print("2. Execute the scoring analysis in scripts/scoring/")
    print("3. Generate visualizations in scripts/visualization/")
    print("\nFor more information, see README.md")

if __name__ == "__main__":
    main()
