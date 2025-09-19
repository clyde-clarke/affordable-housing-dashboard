#!/usr/bin/env python3
"""
Enhanced city scoring system that properly extracts and scores data from markdown files.
This replaces the oversimplified extract_score_from_content function.
"""

import re
import pandas as pd
import os
import json
from typing import Dict, List, Tuple, Optional, Any
from dataclasses import dataclass, asdict
from pathlib import Path

@dataclass
class CityData:
    """Structured data extracted from markdown files."""
    city: str
    category: str
    dollar_amounts: List[float]
    unit_counts: List[int]
    percentages: List[float]
    years: List[int]
    key_metrics: Dict[str, Any]
    raw_text: str
    file_path: str

class EnhancedCityScorer:
    """Enhanced scoring system with proper data extraction and category-specific logic."""
    
    def __init__(self):
        self.category_weights = {
            "Funding": 0.25,
            "Housing Supply": 0.25,
            "Resident Stability": 0.20,
            "Policy Implementation": 0.20,
            "Transparency/Data Access": 0.10
        }
        
        # Define scoring thresholds and criteria for each category
        self.scoring_config = {
            "Funding": {
                "budget_thresholds": {
                    "excellent": 500_000_000,  # $500M+
                    "good": 100_000_000,      # $100M-$500M
                    "fair": 25_000_000,       # $25M-$100M
                    "poor": 5_000_000         # $5M-$25M
                },
                "per_capita_thresholds": {
                    "excellent": 1000,        # $1000+ per capita
                    "good": 500,              # $500-$1000 per capita
                    "fair": 200,              # $200-$500 per capita
                    "poor": 50                # $50-$200 per capita
                },
                "program_bonus": {
                    "trust_fund": 10,
                    "bond_measure": 15,
                    "tax_credit": 8,
                    "federal_funding": 12
                }
            },
            "Housing Supply": {
                "annual_units_thresholds": {
                    "excellent": 5000,        # 5000+ units/year
                    "good": 2000,             # 2000-5000 units/year
                    "fair": 500,              # 500-2000 units/year
                    "poor": 100               # 100-500 units/year
                },
                "pipeline_bonus": 15,
                "target_achievement_bonus": 20,
                "preservation_bonus": 10
            },
            "Resident Stability": {
                "eviction_rate_thresholds": {
                    "excellent": 1.0,         # <1% eviction rate
                    "good": 2.0,              # 1-2% eviction rate
                    "fair": 4.0,              # 2-4% eviction rate
                    "poor": 6.0               # 4-6% eviction rate
                },
                "assistance_programs": {
                    "rental_assistance": 15,
                    "voucher_program": 12,
                    "homelessness_prevention": 10,
                    "tenant_protection": 8
                }
            },
            "Policy Implementation": {
                "inclusionary_zoning": {
                    "mandatory": 25,
                    "voluntary": 15,
                    "density_bonus": 10
                },
                "rent_control": {
                    "strong": 20,
                    "moderate": 12,
                    "weak": 6
                },
                "enforcement": {
                    "robust": 15,
                    "moderate": 8,
                    "weak": 3
                }
            },
            "Transparency/Data Access": {
                "dashboard_availability": {
                    "comprehensive": 30,
                    "basic": 20,
                    "limited": 10
                },
                "data_quality": {
                    "excellent": 25,
                    "good": 15,
                    "fair": 8,
                    "poor": 3
                },
                "update_frequency": {
                    "real_time": 20,
                    "monthly": 15,
                    "quarterly": 10,
                    "annually": 5
                }
            }
        }
    
    def extract_city_data(self, file_path: str) -> CityData:
        """Extract structured data from a markdown file."""
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Extract city and category from filename
        filename = Path(file_path).stem
        parts = filename.split('_')
        city = parts[0].replace('_', ' ').title()
        
        # Map the category properly
        if len(parts) >= 3:
            if parts[1] == 'housing' and parts[2] == 'funding':
                category = 'Funding'
            elif parts[1] == 'housing' and parts[2] == 'supply':
                category = 'Housing Supply'
            elif parts[1] == 'resident' and parts[2] == 'stability':
                category = 'Resident Stability'
            elif parts[1] == 'policy' and parts[2] == 'implementation':
                category = 'Policy Implementation'
            elif parts[1] == 'transparency' and parts[2] == 'data' and len(parts) > 3 and parts[3] == 'access':
                category = 'Transparency/Data Access'
            else:
                category = parts[1].replace('_', ' ').title()
        else:
            category = parts[1].replace('_', ' ').title()
        
        # Extract dollar amounts with proper scaling
        dollar_amounts = self._extract_dollar_amounts(content)
        
        # Extract unit counts
        unit_counts = self._extract_unit_counts(content)
        
        # Extract percentages
        percentages = self._extract_percentages(content)
        
        # Extract years
        years = self._extract_years(content)
        
        # Extract key metrics specific to category
        key_metrics = self._extract_key_metrics(content, category)
        
        return CityData(
            city=city,
            category=category,
            dollar_amounts=dollar_amounts,
            unit_counts=unit_counts,
            percentages=percentages,
            years=years,
            key_metrics=key_metrics,
            raw_text=content,
            file_path=file_path
        )
    
    def _extract_dollar_amounts(self, content: str) -> List[float]:
        """Extract and convert dollar amounts to numeric values."""
        dollar_pattern = r'\$[\d,]+(?:\.\d+)?\s*(?:million|billion|thousand)?'
        matches = re.findall(dollar_pattern, content, re.IGNORECASE)
        
        amounts = []
        for match in matches:
            try:
                # Clean the match
                amount_str = re.sub(r'[$,]', '', match.lower())
                
                # Extract numeric value
                numeric_match = re.search(r'[\d.]+', amount_str)
                if not numeric_match:
                    continue
                
                value = float(numeric_match.group())
                
                # Apply scaling based on unit
                if 'billion' in amount_str:
                    value *= 1_000_000_000
                elif 'million' in amount_str:
                    value *= 1_000_000
                elif 'thousand' in amount_str:
                    value *= 1_000
                
                amounts.append(value)
            except (ValueError, AttributeError):
                continue
        
        return amounts
    
    def _extract_unit_counts(self, content: str) -> List[int]:
        """Extract unit counts from content."""
        unit_pattern = r'(\d+(?:,\d{3})*(?:\.\d+)?)\s*(?:units?|homes?|apartments?|housing)'
        matches = re.findall(unit_pattern, content, re.IGNORECASE)
        
        counts = []
        for match in matches:
            try:
                count = int(re.sub(r'[,]', '', match))
                counts.append(count)
            except ValueError:
                continue
        
        return counts
    
    def _extract_percentages(self, content: str) -> List[float]:
        """Extract percentages from content."""
        percent_pattern = r'(\d+(?:\.\d+)?)%'
        matches = re.findall(percent_pattern, content)
        
        return [float(match) for match in matches]
    
    def _extract_years(self, content: str) -> List[int]:
        """Extract years from content."""
        year_pattern = r'\b(19|20)\d{2}\b'
        matches = re.findall(year_pattern, content)
        
        return [int(match) for match in matches]
    
    def _extract_key_metrics(self, content: str, category: str) -> Dict[str, Any]:
        """Extract category-specific key metrics."""
        metrics = {}
        content_lower = content.lower()
        
        if category == "Funding":
            # Look for per capita calculations
            per_capita_pattern = r'(\$[\d,]+(?:\.\d+)?)\s*per\s*capita'
            per_capita_matches = re.findall(per_capita_pattern, content, re.IGNORECASE)
            if per_capita_matches:
                per_capita = float(re.sub(r'[$,]', '', per_capita_matches[0]))
                metrics['per_capita_investment'] = per_capita
            
            # Count funding programs
            program_keywords = ['trust fund', 'bond', 'tax credit', 'subsidy', 'grant', 'allocation']
            metrics['program_count'] = sum(1 for keyword in program_keywords if keyword in content_lower)
            
        elif category == "Housing Supply":
            # Look for target achievement
            if 'surpassed' in content_lower or 'exceeded' in content_lower:
                metrics['target_achievement'] = 'exceeded'
            elif 'met' in content_lower or 'achieved' in content_lower:
                metrics['target_achievement'] = 'met'
            else:
                metrics['target_achievement'] = 'unknown'
            
            # Check for pipeline data
            pipeline_keywords = ['pipeline', 'planned', 'approved', 'under construction']
            metrics['has_pipeline_data'] = any(keyword in content_lower for keyword in pipeline_keywords)
            
        elif category == "Resident Stability":
            # Extract eviction rates
            eviction_keywords = ['eviction', 'filing', 'rate']
            if any(keyword in content_lower for keyword in eviction_keywords):
                # Look for specific eviction rate numbers
                rate_pattern = r'(\d+(?:\.\d+)?)\s*%?\s*(?:eviction|filing)'
                rate_matches = re.findall(rate_pattern, content_lower)
                if rate_matches:
                    metrics['eviction_rates'] = [float(match) for match in rate_matches]
            
            # Count assistance programs
            assistance_keywords = ['assistance', 'voucher', 'prevention', 'support', 'counseling']
            metrics['assistance_programs'] = sum(1 for keyword in assistance_keywords if keyword in content_lower)
            
        elif category == "Policy Implementation":
            # Check for inclusionary zoning
            inclusionary_keywords = ['inclusionary', 'zoning', 'mandatory', 'affordable']
            metrics['inclusionary_policies'] = sum(1 for keyword in inclusionary_keywords if keyword in content_lower)
            
            # Check for rent control
            rent_control_keywords = ['rent control', 'rent stabilization', 'rent regulation']
            metrics['has_rent_control'] = any(keyword in content_lower for keyword in rent_control_keywords)
            
        elif category == "Transparency/Data Access":
            # Count dashboards and data sources
            dashboard_keywords = ['dashboard', 'portal', 'open data', 'dataset']
            metrics['data_sources'] = sum(1 for keyword in dashboard_keywords if keyword in content_lower)
            
            # Check update frequency
            if 'real-time' in content_lower or 'live' in content_lower:
                metrics['update_frequency'] = 'real_time'
            elif 'monthly' in content_lower:
                metrics['update_frequency'] = 'monthly'
            elif 'quarterly' in content_lower:
                metrics['update_frequency'] = 'quarterly'
            elif 'annually' in content_lower:
                metrics['update_frequency'] = 'annually'
            else:
                metrics['update_frequency'] = 'unknown'
        
        return metrics
    
    def calculate_category_score(self, data: CityData) -> float:
        """Calculate score for a specific category based on extracted data."""
        category = data.category
        
        if category == "Funding":
            return self._calculate_funding_score(data)
        elif category == "Housing Supply":
            return self._calculate_housing_supply_score(data)
        elif category == "Resident Stability":
            return self._calculate_resident_stability_score(data)
        elif category == "Policy Implementation":
            return self._calculate_policy_implementation_score(data)
        elif category == "Transparency/Data Access":
            return self._calculate_transparency_score(data)
        else:
            return 0.0
    
    def _calculate_funding_score(self, data: CityData) -> float:
        """Calculate funding score based on budget allocations and investments."""
        score = 0
        config = self.scoring_config["Funding"]
        
        # Score based on total funding amount
        if data.dollar_amounts:
            # Filter out very small amounts that are likely per capita values
            significant_amounts = [amt for amt in data.dollar_amounts if amt > 1000]
            if significant_amounts:
                total_funding = sum(significant_amounts)
                thresholds = config["budget_thresholds"]
                
                if total_funding >= thresholds["excellent"]:
                    score += 50
                elif total_funding >= thresholds["good"]:
                    score += 40
                elif total_funding >= thresholds["fair"]:
                    score += 25
                elif total_funding >= thresholds["poor"]:
                    score += 10
                else:
                    score += 5  # Some funding is better than none
        
        # Score based on per capita investment
        if 'per_capita_investment' in data.key_metrics:
            per_capita = data.key_metrics['per_capita_investment']
            thresholds = config["per_capita_thresholds"]
            
            if per_capita >= thresholds["excellent"]:
                score += 30
            elif per_capita >= thresholds["good"]:
                score += 25
            elif per_capita >= thresholds["fair"]:
                score += 15
            elif per_capita >= thresholds["poor"]:
                score += 8
            else:
                score += 3  # Some per capita investment is better than none
        
        # Bonus for program diversity
        if 'program_count' in data.key_metrics:
            program_count = data.key_metrics['program_count']
            score += min(20, program_count * 3)
        else:
            # Fallback: count program keywords in text
            program_keywords = ['trust fund', 'bond', 'tax credit', 'subsidy', 'grant', 'allocation', 'program']
            program_count = sum(1 for keyword in program_keywords if keyword in data.raw_text.lower())
            score += min(20, program_count * 2)
        
        return min(100, max(0, score))
    
    def _calculate_housing_supply_score(self, data: CityData) -> float:
        """Calculate housing supply score based on units created and pipeline."""
        score = 0
        config = self.scoring_config["Housing Supply"]
        
        # Score based on annual unit production
        if data.unit_counts:
            max_units = max(data.unit_counts)
            thresholds = config["annual_units_thresholds"]
            
            if max_units >= thresholds["excellent"]:
                score += 50
            elif max_units >= thresholds["good"]:
                score += 40
            elif max_units >= thresholds["fair"]:
                score += 25
            elif max_units >= thresholds["poor"]:
                score += 10
            else:
                score += 5  # Some units are better than none
        else:
            # Fallback: look for unit numbers in text
            unit_keywords = ['units', 'homes', 'apartments', 'housing']
            unit_mentions = sum(1 for keyword in unit_keywords if keyword in data.raw_text.lower())
            score += min(20, unit_mentions * 3)
        
        # Bonus for pipeline data
        if data.key_metrics.get('has_pipeline_data', False):
            score += config["pipeline_bonus"]
        else:
            # Fallback: check for pipeline keywords
            pipeline_keywords = ['pipeline', 'planned', 'approved', 'under construction']
            if any(keyword in data.raw_text.lower() for keyword in pipeline_keywords):
                score += config["pipeline_bonus"] * 0.5
        
        # Bonus for target achievement
        target_achievement = data.key_metrics.get('target_achievement', 'unknown')
        if target_achievement == 'exceeded':
            score += config["target_achievement_bonus"]
        elif target_achievement == 'met':
            score += config["target_achievement_bonus"] * 0.7
        else:
            # Fallback: check for target language
            if 'surpassed' in data.raw_text.lower() or 'exceeded' in data.raw_text.lower():
                score += config["target_achievement_bonus"]
            elif 'met' in data.raw_text.lower() or 'achieved' in data.raw_text.lower():
                score += config["target_achievement_bonus"] * 0.7
        
        return min(100, max(0, score))
    
    def _calculate_resident_stability_score(self, data: CityData) -> float:
        """Calculate resident stability score based on eviction rates and assistance programs."""
        score = 0
        config = self.scoring_config["Resident Stability"]
        
        # Score based on eviction rates
        if 'eviction_rates' in data.key_metrics and data.key_metrics['eviction_rates']:
            eviction_rate = min(data.key_metrics['eviction_rates'])  # Take lowest rate
            thresholds = config["eviction_rate_thresholds"]
            
            if eviction_rate <= thresholds["excellent"]:
                score += 50
            elif eviction_rate <= thresholds["good"]:
                score += 40
            elif eviction_rate <= thresholds["fair"]:
                score += 25
            elif eviction_rate <= thresholds["poor"]:
                score += 10
        
        # Score based on assistance programs
        if 'assistance_programs' in data.key_metrics:
            program_count = data.key_metrics['assistance_programs']
            score += min(30, program_count * 5)
        
        # Score based on spending on housing services
        if data.dollar_amounts:
            # Look for assistance-related spending (simplified)
            assistance_spending = sum(data.dollar_amounts) / 1_000_000  # Convert to millions
            score += min(20, assistance_spending * 0.5)
        
        return min(100, max(0, score))
    
    def _calculate_policy_implementation_score(self, data: CityData) -> float:
        """Calculate policy implementation score based on ordinances and enforcement."""
        score = 0
        config = self.scoring_config["Policy Implementation"]
        
        # Score based on inclusionary zoning
        if 'inclusionary_policies' in data.key_metrics:
            policy_count = data.key_metrics['inclusionary_policies']
            score += min(40, policy_count * 8)
        
        # Score based on rent control
        if data.key_metrics.get('has_rent_control', False):
            score += config["rent_control"]["strong"]
        
        # Score based on enforcement (simplified)
        enforcement_keywords = ['enforcement', 'audit', 'compliance', 'oversight']
        enforcement_count = sum(1 for keyword in enforcement_keywords if keyword in data.raw_text.lower())
        score += min(20, enforcement_count * 4)
        
        return min(100, max(0, score))
    
    def _calculate_transparency_score(self, data: CityData) -> float:
        """Calculate transparency score based on data availability and quality."""
        score = 0
        config = self.scoring_config["Transparency/Data Access"]
        
        # Score based on data sources
        if 'data_sources' in data.key_metrics:
            source_count = data.key_metrics['data_sources']
            if source_count >= 5:
                score += config["dashboard_availability"]["comprehensive"]
            elif source_count >= 3:
                score += config["dashboard_availability"]["basic"]
            elif source_count >= 1:
                score += config["dashboard_availability"]["limited"]
        else:
            # Fallback: count dashboard keywords
            dashboard_keywords = ['dashboard', 'portal', 'open data', 'dataset', 'reporting']
            source_count = sum(1 for keyword in dashboard_keywords if keyword in data.raw_text.lower())
            if source_count >= 5:
                score += config["dashboard_availability"]["comprehensive"]
            elif source_count >= 3:
                score += config["dashboard_availability"]["basic"]
            elif source_count >= 1:
                score += config["dashboard_availability"]["limited"]
        
        # Score based on update frequency
        if 'update_frequency' in data.key_metrics:
            frequency = data.key_metrics['update_frequency']
            if frequency in config["update_frequency"]:
                score += config["update_frequency"][frequency]
        else:
            # Fallback: check for frequency keywords
            if 'real-time' in data.raw_text.lower() or 'live' in data.raw_text.lower():
                score += config["update_frequency"]["real_time"]
            elif 'monthly' in data.raw_text.lower():
                score += config["update_frequency"]["monthly"]
            elif 'quarterly' in data.raw_text.lower():
                score += config["update_frequency"]["quarterly"]
            elif 'annually' in data.raw_text.lower():
                score += config["update_frequency"]["annually"]
        
        # Score based on data quality indicators
        quality_keywords = ['audit', 'verification', 'independent', 'transparent', 'quality']
        quality_count = sum(1 for keyword in quality_keywords if keyword in data.raw_text.lower())
        score += min(25, quality_count * 5)
        
        # Base score for having any transparency data
        if score == 0 and len(data.raw_text) > 100:
            score = 10  # Minimum score for having data
        
        return min(100, max(0, score))
    
    def process_all_cities(self, data_directory: str = ".") -> Dict[str, Dict[str, float]]:
        """Process all city markdown files and calculate scores."""
        scores = {}
        
        # Find all city markdown files
        city_files = []
        for file_path in Path(data_directory).glob("*_housing_*.md"):
            city_files.append(file_path)
        
        # Group files by city
        city_data = {}
        for file_path in city_files:
            try:
                data = self.extract_city_data(str(file_path))
                if data.city not in city_data:
                    city_data[data.city] = {}
                city_data[data.city][data.category] = data
            except Exception as e:
                print(f"Error processing {file_path}: {e}")
                continue
        
        # Calculate scores for each city and category
        for city, categories in city_data.items():
            scores[city] = {}
            for category, data in categories.items():
                score = self.calculate_category_score(data)
                scores[city][category] = score
        
        return scores
    
    def normalize_scores(self, scores: Dict[str, Dict[str, float]]) -> Dict[str, Dict[str, float]]:
        """Normalize scores to 0-100 scale within each category across all cities."""
        normalized = {}
        
        # Get all categories
        all_categories = set()
        for city_scores in scores.values():
            all_categories.update(city_scores.keys())
        
        # Normalize each category separately
        for category in all_categories:
            category_scores = []
            for city_scores in scores.values():
                if category in city_scores:
                    category_scores.append(city_scores[category])
            
            if not category_scores:
                continue
            
            min_score = min(category_scores)
            max_score = max(category_scores)
            
            # Normalize to 0-100 scale
            for city, city_scores in scores.items():
                if category in city_scores:
                    if city not in normalized:
                        normalized[city] = {}
                    
                    if max_score == min_score:
                        normalized[city][category] = 0
                    else:
                        normalized[city][category] = ((city_scores[category] - min_score) / (max_score - min_score)) * 100
        
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
    """Test the enhanced scoring system."""
    scorer = EnhancedCityScorer()
    
    # Test with a sample file
    test_file = "/Users/clydeclarke/Downloads/Major US Cities List/chicago_housing_funding.md"
    if os.path.exists(test_file):
        data = scorer.extract_city_data(test_file)
        score = scorer.calculate_category_score(data)
        
        print(f"City: {data.city}")
        print(f"Category: {data.category}")
        print(f"Score: {score:.2f}")
        print(f"Dollar amounts: {data.dollar_amounts}")
        print(f"Unit counts: {data.unit_counts}")
        print(f"Key metrics: {data.key_metrics}")
        
        # Test processing all cities
        print("\nProcessing all cities...")
        all_scores = scorer.process_all_cities()
        normalized_scores = scorer.normalize_scores(all_scores)
        overall_scores = scorer.calculate_overall_scores(normalized_scores)
        
        print("\nOverall Scores:")
        for city, score in sorted(overall_scores.items(), key=lambda x: x[1], reverse=True):
            print(f"{city}: {score:.2f}")

if __name__ == "__main__":
    main()
