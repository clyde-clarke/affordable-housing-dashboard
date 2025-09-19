#!/usr/bin/env python3
"""
Improved scoring system for affordable housing indicators.
Extracts meaningful quantitative data from markdown files and calculates proper scores.
"""

import re
import pandas as pd
import os
from typing import Dict, List, Tuple, Optional
from dataclasses import dataclass

@dataclass
class ExtractedData:
    """Container for extracted data from markdown files."""
    dollar_amounts: List[float]
    unit_counts: List[int]
    percentages: List[float]
    years: List[int]
    keywords: List[str]
    raw_text: str

class ImprovedScoringSystem:
    """Enhanced scoring system that extracts meaningful data from markdown files."""
    
    def __init__(self):
        self.category_weights = {
            "Funding": 0.25,
            "Housing Supply": 0.25,
            "Resident Stability": 0.20,
            "Policy Implementation": 0.20,
            "Transparency/Data Access": 0.10
        }
        
        # Category-specific scoring criteria
        self.scoring_criteria = {
            "Funding": {
                "budget_keywords": ["budget", "allocation", "funding", "investment", "bond", "trust fund"],
                "dollar_weight": 0.4,
                "per_capita_weight": 0.3,
                "programs_weight": 0.3
            },
            "Housing Supply": {
                "unit_keywords": ["units", "homes", "apartments", "housing", "construction"],
                "production_weight": 0.4,
                "pipeline_weight": 0.3,
                "targets_weight": 0.3
            },
            "Resident Stability": {
                "stability_keywords": ["eviction", "displacement", "assistance", "voucher", "prevention"],
                "eviction_weight": 0.4,
                "assistance_weight": 0.3,
                "protection_weight": 0.3
            },
            "Policy Implementation": {
                "policy_keywords": ["policy", "ordinance", "zoning", "regulation", "enforcement"],
                "inclusionary_weight": 0.4,
                "rent_control_weight": 0.3,
                "enforcement_weight": 0.3
            },
            "Transparency/Data Access": {
                "transparency_keywords": ["dashboard", "open data", "portal", "dataset", "reporting"],
                "dashboard_weight": 0.4,
                "data_quality_weight": 0.3,
                "frequency_weight": 0.3
            }
        }
    
    def extract_data_from_content(self, content: str) -> ExtractedData:
        """Extract structured data from markdown content."""
        # Extract dollar amounts
        dollar_pattern = r'\$[\d,]+(?:\.\d+)?\s*(?:million|billion|thousand)?'
        dollar_matches = re.findall(dollar_pattern, content, re.IGNORECASE)
        dollar_amounts = []
        for match in dollar_matches:
            # Convert to numeric value
            amount_str = re.sub(r'[$,]', '', match.lower())
            if 'billion' in amount_str:
                amount = float(re.findall(r'[\d.]+', amount_str)[0]) * 1_000_000_000
            elif 'million' in amount_str:
                amount = float(re.findall(r'[\d.]+', amount_str)[0]) * 1_000_000
            elif 'thousand' in amount_str:
                amount = float(re.findall(r'[\d.]+', amount_str)[0]) * 1_000
            else:
                amount = float(re.findall(r'[\d.]+', amount_str)[0])
            dollar_amounts.append(amount)
        
        # Extract unit counts
        unit_pattern = r'(\d+(?:,\d{3})*(?:\.\d+)?)\s*(?:units?|homes?|apartments?|housing)'
        unit_matches = re.findall(unit_pattern, content, re.IGNORECASE)
        unit_counts = [int(re.sub(r'[,]', '', match)) for match in unit_matches]
        
        # Extract percentages
        percent_pattern = r'(\d+(?:\.\d+)?)%'
        percent_matches = re.findall(percent_pattern, content)
        percentages = [float(match) for match in percent_matches]
        
        # Extract years
        year_pattern = r'\b(19|20)\d{2}\b'
        year_matches = re.findall(year_pattern, content)
        years = [int(match) for match in year_matches]
        
        # Extract relevant keywords
        keywords = []
        for category, criteria in self.scoring_criteria.items():
            for keyword in criteria.get("keywords", []):
                if keyword in content.lower():
                    keywords.append(keyword)
        
        return ExtractedData(
            dollar_amounts=dollar_amounts,
            unit_counts=unit_counts,
            percentages=percentages,
            years=years,
            keywords=keywords,
            raw_text=content
        )
    
    def calculate_funding_score(self, data: ExtractedData) -> float:
        """Calculate funding score based on budget allocations and investments."""
        score = 0
        
        # Score based on total dollar amounts
        if data.dollar_amounts:
            total_funding = sum(data.dollar_amounts)
            # Scale: $0-100M = 0-50 points, $100M-1B = 50-80 points, $1B+ = 80-100 points
            if total_funding < 100_000_000:
                score += (total_funding / 100_000_000) * 50
            elif total_funding < 1_000_000_000:
                score += 50 + ((total_funding - 100_000_000) / 900_000_000) * 30
            else:
                score += 80 + min(20, (total_funding - 1_000_000_000) / 1_000_000_000 * 20)
        
        # Score based on per capita investment (if population data available)
        per_capita_keywords = ["per capita", "population", "residents"]
        if any(keyword in data.raw_text.lower() for keyword in per_capita_keywords):
            # Look for per capita calculations in text
            per_capita_pattern = r'(\$[\d,]+(?:\.\d+)?)\s*per\s*capita'
            per_capita_matches = re.findall(per_capita_pattern, data.raw_text, re.IGNORECASE)
            if per_capita_matches:
                per_capita = float(re.sub(r'[$,]', '', per_capita_matches[0]))
                # Scale: $0-100 = 0-30 points, $100-500 = 30-60 points, $500+ = 60-100 points
                if per_capita < 100:
                    score += (per_capita / 100) * 30
                elif per_capita < 500:
                    score += 30 + ((per_capita - 100) / 400) * 30
                else:
                    score += 60 + min(40, (per_capita - 500) / 500 * 40)
        
        # Score based on program diversity
        program_keywords = ["trust fund", "bond", "tax credit", "subsidy", "grant"]
        program_count = sum(1 for keyword in program_keywords if keyword in data.raw_text.lower())
        score += min(20, program_count * 4)  # Max 20 points for program diversity
        
        return min(100, max(0, score))
    
    def calculate_housing_supply_score(self, data: ExtractedData) -> float:
        """Calculate housing supply score based on units created and pipeline."""
        score = 0
        
        # Score based on annual unit production
        if data.unit_counts:
            annual_units = max(data.unit_counts)  # Take the highest number mentioned
            # Scale: 0-1000 units = 0-40 points, 1000-5000 = 40-70 points, 5000+ = 70-100 points
            if annual_units < 1000:
                score += (annual_units / 1000) * 40
            elif annual_units < 5000:
                score += 40 + ((annual_units - 1000) / 4000) * 30
            else:
                score += 70 + min(30, (annual_units - 5000) / 5000 * 30)
        
        # Score based on pipeline units
        pipeline_keywords = ["pipeline", "planned", "approved", "under construction"]
        if any(keyword in data.raw_text.lower() for keyword in pipeline_keywords):
            score += 20  # Bonus for having pipeline data
        
        # Score based on target achievement
        target_keywords = ["target", "goal", "plan", "requirement"]
        if any(keyword in data.raw_text.lower() for keyword in target_keywords):
            # Look for target achievement language
            if "surpassed" in data.raw_text.lower() or "exceeded" in data.raw_text.lower():
                score += 20
            elif "met" in data.raw_text.lower() or "achieved" in data.raw_text.lower():
                score += 15
            else:
                score += 10
        
        return min(100, max(0, score))
    
    def calculate_resident_stability_score(self, data: ExtractedData) -> float:
        """Calculate resident stability score based on eviction rates and assistance programs."""
        score = 0
        
        # Score based on eviction data availability and rates
        eviction_keywords = ["eviction", "filing", "rate"]
        if any(keyword in data.raw_text.lower() for keyword in eviction_keywords):
            # Look for eviction rate percentages
            if data.percentages:
                eviction_rate = min(data.percentages)  # Take lowest rate mentioned
                # Lower eviction rates = higher scores
                if eviction_rate < 1:
                    score += 40
                elif eviction_rate < 3:
                    score += 30
                elif eviction_rate < 5:
                    score += 20
                else:
                    score += 10
            else:
                score += 15  # Bonus for having eviction data
        
        # Score based on assistance programs
        assistance_keywords = ["assistance", "voucher", "prevention", "support"]
        assistance_count = sum(1 for keyword in assistance_keywords if keyword in data.raw_text.lower())
        score += min(30, assistance_count * 6)  # Max 30 points for assistance programs
        
        # Score based on spending on housing services
        if data.dollar_amounts:
            # Look for assistance-related spending
            assistance_spending = sum(data.dollar_amounts)  # Simplified - would need better context
            if assistance_spending > 0:
                score += min(30, assistance_spending / 1_000_000 * 2)  # Scale based on spending
        
        return min(100, max(0, score))
    
    def calculate_policy_implementation_score(self, data: ExtractedData) -> float:
        """Calculate policy implementation score based on ordinances and enforcement."""
        score = 0
        
        # Score based on inclusionary zoning
        inclusionary_keywords = ["inclusionary", "zoning", "mandatory", "affordable"]
        inclusionary_count = sum(1 for keyword in inclusionary_keywords if keyword in data.raw_text.lower())
        score += min(40, inclusionary_count * 8)  # Max 40 points for inclusionary policies
        
        # Score based on rent control/stabilization
        rent_control_keywords = ["rent control", "rent stabilization", "rent regulation"]
        if any(keyword in data.raw_text.lower() for keyword in rent_control_keywords):
            score += 30
        
        # Score based on enforcement
        enforcement_keywords = ["enforcement", "audit", "compliance", "oversight"]
        enforcement_count = sum(1 for keyword in enforcement_keywords if keyword in data.raw_text.lower())
        score += min(30, enforcement_count * 6)  # Max 30 points for enforcement
        
        return min(100, max(0, score))
    
    def calculate_transparency_score(self, data: ExtractedData) -> float:
        """Calculate transparency score based on data availability and quality."""
        score = 0
        
        # Score based on dashboard availability
        dashboard_keywords = ["dashboard", "portal", "open data", "dataset"]
        dashboard_count = sum(1 for keyword in dashboard_keywords if keyword in data.raw_text.lower())
        score += min(50, dashboard_count * 10)  # Max 50 points for dashboards
        
        # Score based on reporting frequency
        frequency_keywords = ["annual", "quarterly", "monthly", "regular", "updated"]
        frequency_count = sum(1 for keyword in frequency_keywords if keyword in data.raw_text.lower())
        score += min(30, frequency_count * 6)  # Max 30 points for reporting frequency
        
        # Score based on data quality indicators
        quality_keywords = ["audit", "verification", "independent", "transparent"]
        quality_count = sum(1 for keyword in quality_keywords if keyword in data.raw_text.lower())
        score += min(20, quality_count * 5)  # Max 20 points for data quality
        
        return min(100, max(0, score))
    
    def calculate_category_score(self, content: str, category: str) -> float:
        """Calculate score for a specific category."""
        data = self.extract_data_from_content(content)
        
        if category == "Funding":
            return self.calculate_funding_score(data)
        elif category == "Housing Supply":
            return self.calculate_housing_supply_score(data)
        elif category == "Resident Stability":
            return self.calculate_resident_stability_score(data)
        elif category == "Policy Implementation":
            return self.calculate_policy_implementation_score(data)
        elif category == "Transparency/Data Access":
            return self.calculate_transparency_score(data)
        else:
            return 0.0
    
    def normalize_scores(self, scores: Dict[str, Dict[str, float]]) -> Dict[str, Dict[str, float]]:
        """Normalize scores to 0-100 scale within each category."""
        normalized = {}
        
        for city, categories in scores.items():
            normalized[city] = {}
            for category, score in categories.items():
                # For now, return raw scores (normalization would be done across all cities)
                normalized[city][category] = score
        
        return normalized
    
    def calculate_overall_scores(self, normalized_scores: Dict[str, Dict[str, float]]) -> Dict[str, float]:
        """Calculate weighted overall scores for each city."""
        overall_scores = {}
        
        for city, categories in normalized_scores.items():
            weighted_score = 0
            for category, score in categories.items():
                weight = self.category_weights.get(category, 0)
                weighted_score += score * weight
            overall_scores[city] = weighted_score
        
        return overall_scores

def main():
    """Test the improved scoring system."""
    scorer = ImprovedScoringSystem()
    
    # Test with a sample file
    test_file = "/Users/clydeclarke/Downloads/Major US Cities List/chicago_housing_funding.md"
    if os.path.exists(test_file):
        with open(test_file, 'r') as f:
            content = f.read()
        
        score = scorer.calculate_category_score(content, "Funding")
        print(f"Chicago Funding Score: {score:.2f}")
        
        # Test data extraction
        data = scorer.extract_data_from_content(content)
        print(f"Extracted dollar amounts: {data.dollar_amounts}")
        print(f"Extracted unit counts: {data.unit_counts}")
        print(f"Extracted keywords: {data.keywords}")

if __name__ == "__main__":
    main()
