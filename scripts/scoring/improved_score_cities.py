#!/usr/bin/env python3
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
    print("\nNormalized Scores (0-100 scale):")
    print(normalized_df)
    print("\nOverall Weighted Scores and Ranks:")
    print(overall_df)
    
    # Save results
    normalized_df.to_csv('improved_normalized_scores.csv')
    overall_df.to_csv('improved_overall_scores.csv')
    
    print("\nResults saved to improved_normalized_scores.csv and improved_overall_scores.csv")

if __name__ == "__main__":
    main()
