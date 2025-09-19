#!/bin/bash

# Affordable Housing Dashboard Setup Script
# This script sets up both the React frontend and FastAPI backend

echo "🚀 Setting up Affordable Housing Dashboard..."
echo "=============================================="

# Check if Node.js is installed
if ! command -v node &> /dev/null; then
    echo "❌ Node.js is not installed. Please install Node.js 16+ first."
    echo "   Visit: https://nodejs.org/"
    exit 1
fi

# Check if Python is installed
if ! command -v python3 &> /dev/null; then
    echo "❌ Python 3 is not installed. Please install Python 3.8+ first."
    echo "   Visit: https://python.org/"
    exit 1
fi

echo "✅ Prerequisites check passed"

# Setup Frontend
echo ""
echo "📦 Setting up React Frontend..."
echo "==============================="

cd frontend

# Install dependencies
echo "Installing npm dependencies..."
npm install

if [ $? -eq 0 ]; then
    echo "✅ Frontend dependencies installed successfully"
else
    echo "❌ Failed to install frontend dependencies"
    exit 1
fi

# Build the project
echo "Building React application..."
npm run build

if [ $? -eq 0 ]; then
    echo "✅ Frontend build completed successfully"
else
    echo "❌ Frontend build failed"
    exit 1
fi

cd ..

# Setup Backend
echo ""
echo "🐍 Setting up FastAPI Backend..."
echo "================================="

cd backend

# Create virtual environment
echo "Creating Python virtual environment..."
python3 -m venv venv

# Activate virtual environment
echo "Activating virtual environment..."
source venv/bin/activate

# Install dependencies
echo "Installing Python dependencies..."
pip install -r requirements.txt

if [ $? -eq 0 ]; then
    echo "✅ Backend dependencies installed successfully"
else
    echo "❌ Failed to install backend dependencies"
    exit 1
fi

cd ..

# Create startup scripts
echo ""
echo "📝 Creating startup scripts..."
echo "=============================="

# Frontend startup script
cat > start-frontend.sh << 'EOF'
#!/bin/bash
echo "🚀 Starting React Frontend..."
cd frontend
npm start
EOF

chmod +x start-frontend.sh

# Backend startup script
cat > start-backend.sh << 'EOF'
#!/bin/bash
echo "🐍 Starting FastAPI Backend..."
cd backend
source venv/bin/activate
python main.py
EOF

chmod +x start-backend.sh

# Combined startup script
cat > start-dashboard.sh << 'EOF'
#!/bin/bash
echo "🚀 Starting Affordable Housing Dashboard..."
echo "=========================================="

# Start backend in background
echo "Starting backend server..."
cd backend
source venv/bin/activate
python main.py &
BACKEND_PID=$!

# Wait a moment for backend to start
sleep 3

# Start frontend
echo "Starting frontend server..."
cd ../frontend
npm start &
FRONTEND_PID=$!

echo ""
echo "✅ Dashboard started successfully!"
echo "   Frontend: http://localhost:3000"
echo "   Backend API: http://localhost:8000"
echo "   API Docs: http://localhost:8000/docs"
echo ""
echo "Press Ctrl+C to stop both servers"

# Wait for user to stop
wait $FRONTEND_PID $BACKEND_PID
EOF

chmod +x start-dashboard.sh

echo "✅ Startup scripts created"

# Create data integration script
echo ""
echo "🔗 Creating data integration script..."
echo "======================================"

cat > integrate-data.py << 'EOF'
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
EOF

chmod +x integrate-data.py

echo "✅ Data integration script created"

# Final instructions
echo ""
echo "🎉 Dashboard Setup Complete!"
echo "============================"
echo ""
echo "To start the dashboard:"
echo "  ./start-dashboard.sh"
echo ""
echo "To start components separately:"
echo "  ./start-frontend.sh  (React frontend)"
echo "  ./start-backend.sh   (FastAPI backend)"
echo ""
echo "To integrate latest data:"
echo "  python3 integrate-data.py"
echo ""
echo "Dashboard URLs:"
echo "  Frontend: http://localhost:3000"
echo "  Backend API: http://localhost:8000"
echo "  API Documentation: http://localhost:8000/docs"
echo ""
echo "For more information, see README.md"
