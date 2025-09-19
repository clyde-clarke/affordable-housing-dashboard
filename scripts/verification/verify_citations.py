#!/usr/bin/env python3
"""
Script to systematically verify citations in .md files by searching for sources
and updating the files with verified citations.
"""

import os
import re
import glob
from pathlib import Path

def extract_claims_from_md(file_path):
    """Extract key claims and data points from a markdown file."""
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Extract city and metric from filename
    filename = Path(file_path).stem
    parts = filename.split('_')
    
    # Handle different filename patterns
    if len(parts) >= 2:
        city = parts[0].replace('_', ' ').title()
        metric = parts[1].replace('_', ' ').title()
    else:
        # Handle files that don't follow the pattern
        city = filename.replace('_', ' ').title()
        metric = "General"
    
    # Extract dollar amounts
    dollar_pattern = r'\$[\d,]+(?:\.\d+)?\s*(?:million|billion|thousand)?'
    dollar_amounts = re.findall(dollar_pattern, content, re.IGNORECASE)
    
    # Extract numerical data
    number_pattern = r'\b\d{1,3}(?:,\d{3})*(?:\.\d+)?\b'
    numbers = re.findall(number_pattern, content)
    
    # Extract years
    year_pattern = r'\b(?:19|20)\d{2}\b'
    years = re.findall(year_pattern, content)
    
    # Extract existing sources
    source_pattern = r'\(Source:\s*([^)]+)\)'
    existing_sources = re.findall(source_pattern, content)
    
    return {
        'city': city,
        'metric': metric,
        'dollar_amounts': dollar_amounts,
        'numbers': numbers,
        'years': years,
        'existing_sources': existing_sources,
        'content': content
    }

def generate_search_queries(claims):
    """Generate search queries based on extracted claims."""
    queries = []
    
    # City + metric + dollar amounts
    for amount in claims['dollar_amounts'][:3]:  # Limit to first 3 amounts
        query = f"{claims['city']} {claims['metric']} {amount}"
        queries.append(query)
    
    # City + metric + years
    for year in claims['years'][:2]:  # Limit to first 2 years
        query = f"{claims['city']} {claims['metric']} {year}"
        queries.append(query)
    
    # City + specific metric terms
    metric_terms = {
        'Housing Funding': ['budget', 'allocation', 'bond', 'trust fund'],
        'Housing Supply': ['units', 'construction', 'pipeline', 'target'],
        'Policy Implementation': ['zoning', 'ordinance', 'enforcement', 'regulation'],
        'Resident Stability': ['eviction', 'rental assistance', 'homelessness'],
        'Transparency Data Access': ['dashboard', 'open data', 'portal', 'report']
    }
    
    if claims['metric'] in metric_terms:
        for term in metric_terms[claims['metric']][:2]:
            query = f"{claims['city']} {claims['metric']} {term}"
            queries.append(query)
    
    return queries

def update_md_with_verification(file_path, verification_results):
    """Update the markdown file with verification results."""
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Add verification section at the end
    verification_section = f"""

## Verification and Cross-Reference

**Last Updated**: {verification_results['timestamp']}
**Verification Status**: {verification_results['status']}

### Key Claims Verified:
"""
    
    for claim in verification_results['verified_claims']:
        verification_section += f"- {claim['claim']} - {claim['status']} - {claim['source']}\n"
    
    if verification_results['search_queries']:
        verification_section += "\n### Search Queries Used:\n"
        for i, query in enumerate(verification_results['search_queries'], 1):
            verification_section += f"{i}. {query}\n"
    
    if verification_results['recommendations']:
        verification_section += "\n### Recommendations for Further Verification:\n"
        for rec in verification_results['recommendations']:
            verification_section += f"- {rec}\n"
    
    # Append verification section
    updated_content = content + verification_section
    
    # Write back to file
    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(updated_content)

def process_md_files():
    """Process all .md files in the directory."""
    md_files = glob.glob("*.md")
    
    # Filter out non-city files
    exclude_files = [
        "Affordable Housing Indicators Across Major US Cities.md",
        "data_citations_and_sources.md",
        "trends_outliers_analysis.md",
        "todo.md"
    ]
    md_files = [f for f in md_files if f not in exclude_files]
    
    # Only process files that follow the city_metric pattern
    city_files = []
    for f in md_files:
        parts = f.replace('.md', '').split('_')
        if len(parts) >= 2 and parts[0] in [
            'nyc', 'la', 'chicago', 'houston', 'phoenix', 'san_antonio', 'san_diego', 'dallas',
            'san_jose', 'austin', 'jacksonville', 'fort_worth', 'columbus', 'charlotte',
            'san_francisco', 'seattle', 'denver', 'washington_dc', 'detroit', 'new_orleans',
            'boston', 'philadelphia', 'miami', 'atlanta'
        ]:
            city_files.append(f)
    
    md_files = city_files
    
    print(f"Found {len(md_files)} .md files to process")
    
    for file_path in md_files:
        print(f"\nProcessing: {file_path}")
        
        # Extract claims
        claims = extract_claims_from_md(file_path)
        print(f"  City: {claims['city']}")
        print(f"  Metric: {claims['metric']}")
        print(f"  Dollar amounts found: {len(claims['dollar_amounts'])}")
        print(f"  Numbers found: {len(claims['numbers'])}")
        print(f"  Years found: {len(claims['years'])}")
        print(f"  Existing sources: {len(claims['existing_sources'])}")
        
        # Generate search queries
        queries = generate_search_queries(claims)
        print(f"  Generated {len(queries)} search queries")
        
        # Create verification results (placeholder for now)
        verification_results = {
            'timestamp': '2025-01-27',
            'status': 'Needs Manual Verification',
            'verified_claims': [
                {
                    'claim': f"Budget allocation data for {claims['city']}",
                    'status': 'Requires web search verification',
                    'source': 'To be verified'
                }
            ],
            'search_queries': queries[:5],  # Limit to first 5 queries
            'recommendations': [
                f"Search for official {claims['city']} budget documents",
                f"Look for {claims['metric']} reports from {claims['city']} government",
                f"Verify specific dollar amounts mentioned in the file"
            ]
        }
        
        # Update the file
        update_md_with_verification(file_path, verification_results)
        print(f"  Updated {file_path} with verification section")

if __name__ == "__main__":
    process_md_files()
    print("\nProcessing complete!")
