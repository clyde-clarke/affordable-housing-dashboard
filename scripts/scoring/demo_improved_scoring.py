#!/usr/bin/env python3
"""
Demo script showing the improved scoring system in action.
Compares the old vs new scoring methods and demonstrates data extraction.
"""

import pandas as pd
import os
from enhanced_city_scorer import EnhancedCityScorer
from score_cities import extract_score_from_content

def compare_scoring_methods():
    """Compare the old and new scoring methods."""
    print("=" * 80)
    print("SCORING SYSTEM COMPARISON")
    print("=" * 80)
    
    # Initialize the enhanced scorer
    enhanced_scorer = EnhancedCityScorer()
    
    # Test files to compare
    test_files = [
        "/Users/clydeclarke/Downloads/Major US Cities List/chicago_housing_funding.md",
        "/Users/clydeclarke/Downloads/Major US Cities List/seattle_housing_supply.md",
        "/Users/clydeclarke/Downloads/Major US Cities List/dallas_transparency_data_access.md"
    ]
    
    for file_path in test_files:
        if not os.path.exists(file_path):
            continue
            
        print(f"\nFile: {os.path.basename(file_path)}")
        print("-" * 50)
        
        # Read file content
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Extract city and category from filename
        filename = os.path.basename(file_path).replace('.md', '')
        parts = filename.split('_')
        city = parts[0].replace('_', ' ').title()
        category = parts[1].replace('_', ' ').title()
        
        # Old scoring method
        old_score = extract_score_from_content(content, category)
        
        # New scoring method
        try:
            data = enhanced_scorer.extract_city_data(file_path)
            new_score = enhanced_scorer.calculate_category_score(data)
            
            print(f"City: {city}")
            print(f"Category: {category}")
            print(f"Old Score: {old_score:.2f}")
            print(f"New Score: {new_score:.2f}")
            print(f"Improvement: {new_score - old_score:.2f} points")
            
            # Show extracted data
            print(f"\nExtracted Data:")
            print(f"  Dollar amounts: {data.dollar_amounts}")
            print(f"  Unit counts: {data.unit_counts}")
            print(f"  Percentages: {data.percentages}")
            print(f"  Key metrics: {data.key_metrics}")
            
        except Exception as e:
            print(f"Error with new scoring: {e}")

def demonstrate_data_storage_alternatives():
    """Demonstrate better data storage formats."""
    print("\n" + "=" * 80)
    print("DATA STORAGE FORMAT ALTERNATIVES")
    print("=" * 80)
    
    # Sample data structure for JSON format
    sample_city_data = {
        "city": "Chicago",
        "category": "Housing Funding",
        "data": {
            "budget_allocations": [
                {
                    "program": "Chicago Housing Authority",
                    "amount": 1300000000,
                    "year": 2025,
                    "source": "thecha.org"
                },
                {
                    "program": "Housing and Economic Development Bond",
                    "amount": 1250000000,
                    "year": 2025,
                    "source": "chicago.gov"
                }
            ],
            "per_capita_investment": 137.8,
            "programs": [
                "Qualified Allocation Plan (QAP)",
                "Housing Trust Fund",
                "Tax Credits"
            ],
            "key_metrics": {
                "total_funding": 2550000000,
                "program_count": 3,
                "population": 2611867
            }
        },
        "last_updated": "2025-01-27",
        "verification_status": "needs_verification"
    }
    
    print("Sample JSON Data Structure:")
    print("-" * 30)
    import json
    print(json.dumps(sample_city_data, indent=2))
    
    print("\nAdvantages of JSON format:")
    print("- Structured data that's easy to parse")
    print("- Supports complex nested data")
    print("- Human-readable")
    print("- Easy validation with schemas")
    print("- Better for programmatic access")
    
    # Sample CSV structure
    print("\n" + "=" * 50)
    print("Sample CSV Structure for Tabular Data:")
    print("-" * 50)
    
    csv_data = {
        "City": ["Chicago", "Chicago", "Chicago"],
        "Category": ["Funding", "Funding", "Funding"],
        "Program": ["CHA Budget", "Housing Bond", "Department Appropriations"],
        "Amount": [1300000000, 1250000000, 196680000],
        "Year": [2025, 2025, 2025],
        "Source": ["thecha.org", "chicago.gov", "bettergov.org"]
    }
    
    df = pd.DataFrame(csv_data)
    print(df.to_string(index=False))

def recommend_improvements():
    """Recommend improvements to the current system."""
    print("\n" + "=" * 80)
    print("RECOMMENDED IMPROVEMENTS")
    print("=" * 80)
    
    print("1. IMMEDIATE FIXES (Keep Markdown Files):")
    print("   ✓ Replace extract_score_from_content with EnhancedCityScorer")
    print("   ✓ Add proper data extraction logic")
    print("   ✓ Implement category-specific scoring criteria")
    print("   ✓ Add data validation and error handling")
    
    print("\n2. MEDIUM-TERM IMPROVEMENTS:")
    print("   • Create structured data extraction pipeline")
    print("   • Add data validation and quality checks")
    print("   • Implement automated verification workflows")
    print("   • Create standardized data schemas")
    
    print("\n3. LONG-TERM IMPROVEMENTS:")
    print("   • Migrate to structured data format (JSON/YAML)")
    print("   • Implement database storage for complex queries")
    print("   • Add real-time data updates")
    print("   • Create API for data access")
    print("   • Implement machine learning for score optimization")
    
    print("\n4. DATA STORAGE RECOMMENDATION:")
    print("   For this project, I recommend a HYBRID approach:")
    print("   • Keep markdown files for human-readable documentation")
    print("   • Add JSON files for structured data extraction")
    print("   • Use CSV files for tabular data and final scores")
    print("   • Implement automated sync between formats")

def create_improved_scoring_script():
    """Create an improved version of the original score_cities.py."""
    print("\n" + "=" * 80)
    print("CREATING IMPROVED SCORING SCRIPT")
    print("=" * 80)
    
    improved_script = '''#!/usr/bin/env python3
"""
Improved version of score_cities.py with proper data extraction and scoring.
"""

import pandas as pd
import os
from enhanced_city_scorer import EnhancedCityScorer

def main():
    """Main scoring function using the enhanced system."""
    # Initialize the enhanced scorer
    scorer = EnhancedCityScorer()
    
    # Process all cities
    print("Processing all cities with enhanced scoring system...")
    raw_scores = scorer.process_all_cities()
    
    # Normalize scores
    normalized_scores = scorer.normalize_scores(raw_scores)
    
    # Calculate overall scores
    overall_scores = scorer.calculate_overall_scores(normalized_scores)
    
    # Create DataFrames
    normalized_df = pd.DataFrame(normalized_scores).T
    overall_df = pd.DataFrame(list(overall_scores.items()), 
                            columns=['City', 'Overall Score']).set_index('City')
    
    # Sort by overall score
    overall_df = overall_df.sort_values('Overall Score', ascending=False)
    
    # Print results
    print("\\nNormalized Scores (0-100 scale):")
    print(normalized_df)
    print("\\nOverall Weighted Scores and Ranks:")
    print(overall_df)
    
    # Save results
    normalized_df.to_csv('improved_normalized_scores.csv')
    overall_df.to_csv('improved_overall_scores.csv')
    
    print("\\nResults saved to improved_normalized_scores.csv and improved_overall_scores.csv")

if __name__ == "__main__":
    main()
'''
    
    with open('/Users/clydeclarke/Downloads/Major US Cities List/improved_score_cities.py', 'w') as f:
        f.write(improved_script)
    
    print("Created improved_score_cities.py")
    print("This script uses the enhanced scoring system instead of the placeholder logic.")

if __name__ == "__main__":
    compare_scoring_methods()
    demonstrate_data_storage_alternatives()
    recommend_improvements()
    create_improved_scoring_script()
