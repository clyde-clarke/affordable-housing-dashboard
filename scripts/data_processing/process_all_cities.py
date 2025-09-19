#!/usr/bin/env python3
"""
Process all city .md files for comprehensive verification.
"""

import os
import re
import glob
from pathlib import Path

def extract_verifiable_claims(content):
    """Extract claims that can be verified from markdown content."""
    claims = []
    
    # Extract dollar amounts with context
    dollar_pattern = r'(\$[\d,]+(?:\.\d+)?\s*(?:million|billion|thousand)?[^.]*\.)'
    dollar_claims = re.findall(dollar_pattern, content, re.IGNORECASE)
    claims.extend(dollar_claims)
    
    # Extract percentage claims
    percent_pattern = r'(\d+(?:\.\d+)?%[^.]*\.)'
    percent_claims = re.findall(percent_pattern, content, re.IGNORECASE)
    claims.extend(percent_claims)
    
    # Extract unit counts
    unit_pattern = r'(\d+(?:,\d{3})*(?:\.\d+)?\s*(?:units?|homes?|apartments?)[^.]*\.)'
    unit_claims = re.findall(unit_pattern, content, re.IGNORECASE)
    claims.extend(unit_claims)
    
    # Extract year-specific claims
    year_pattern = r'((?:In|During|By)\s+(?:19|20)\d{2}[^.]*\.)'
    year_claims = re.findall(year_pattern, content, re.IGNORECASE)
    claims.extend(year_claims)
    
    return claims[:5]  # Limit to first 5 claims

def generate_search_queries(claims, city, metric):
    """Generate specific search queries for verification."""
    queries = []
    
    for claim in claims:
        # Create specific queries based on claim content
        if '$' in claim:
            # Extract dollar amount
            dollar_match = re.search(r'\$[\d,]+(?:\.\d+)?\s*(?:million|billion|thousand)?', claim)
            if dollar_match:
                amount = dollar_match.group()
                queries.append(f'"{city}" "{metric}" "{amount}"')
                queries.append(f'"{city}" budget "{amount}"')
        
        if any(word in claim.lower() for word in ['units', 'homes', 'apartments']):
            queries.append(f'"{city}" "{metric}" units')
            queries.append(f'"{city}" housing production')
        
        if re.search(r'\b(?:19|20)\d{2}\b', claim):
            year_match = re.search(r'\b(19|20)\d{2}\b', claim)
            if year_match:
                year = year_match.group()
                queries.append(f'"{city}" "{metric}" {year}')
    
    # Add general queries
    queries.extend([
        f'"{city}" "{metric}" budget',
        f'"{city}" government "{metric}"',
        f'"{city}" "{metric}" official report',
        f'site:{city.lower().replace(" ", "")}.gov "{metric}"'
    ])
    
    return list(set(queries))[:8]  # Remove duplicates and limit

def update_md_with_enhanced_verification(file_path, city, metric, claims):
    """Update the markdown file with enhanced verification section."""
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Remove existing verification section if it exists
    content = re.sub(r'\n## Verification and Cross-Reference.*$', '', content, flags=re.DOTALL)
    
    # Generate search queries
    queries = generate_search_queries(claims, city, metric)
    
    # Add enhanced verification section
    verification_section = f"""

## Verification and Cross-Reference

**Last Updated**: 2025-01-27
**Verification Status**: Enhanced with Specific Search Queries
**City**: {city}
**Metric**: {metric}

### Key Claims Identified for Verification:
"""
    
    for i, claim in enumerate(claims, 1):
        verification_section += f"\n**Claim {i}**: {claim}\n"
        
        # Categorize the claim
        if '$' in claim:
            verification_section += f"- **Type**: Financial/Budget Claim\n"
        elif '%' in claim:
            verification_section += f"- **Type**: Percentage/Statistical Claim\n"
        elif any(word in claim.lower() for word in ['units', 'homes', 'apartments']):
            verification_section += f"- **Type**: Housing Unit Count\n"
        elif re.search(r'\b(19|20)\d{2}\b', claim):
            verification_section += f"- **Type**: Year-Specific Claim\n"
        else:
            verification_section += f"- **Type**: General Claim\n"
        
        verification_section += f"- **Verification Status**: Requires Manual Search\n"
        verification_section += f"- **Priority**: High\n\n"
    
    verification_section += f"""
### Recommended Search Queries for Verification:
"""
    
    for i, query in enumerate(queries, 1):
        verification_section += f"{i}. `{query}`\n"
    
    verification_section += f"""

### Verification Methodology:
1. **Official Sources**: Search for {city} government websites and official documents
2. **Budget Documents**: Look for {city} budget allocations and capital improvement plans
3. **News Sources**: Check local news outlets for {metric} coverage
4. **Federal Data**: Cross-reference with HUD and other federal housing data
5. **Academic Sources**: Look for research papers and studies on {city} housing

### Specific Sources to Check:
- **{city} Official Website**: Look for budget documents and {metric} reports
- **Local News**: Search local newspapers and TV stations for {metric} coverage
- **HUD Data**: Check HUD's database for {city} housing funding and programs
- **State Government**: Look for state-level {metric} programs affecting {city}
- **Nonprofit Reports**: Check housing advocacy organizations for {city} data

### Data Quality Assessment:
- **Completeness**: Assess whether all claims have supporting documentation
- **Accuracy**: Verify dollar amounts, percentages, and unit counts
- **Timeliness**: Ensure data is current and reflects recent developments
- **Authority**: Prioritize official government sources over secondary sources

### Next Steps for Manual Verification:
1. Use the provided search queries to find supporting sources
2. Document all sources found with URLs and publication dates
3. Cross-reference multiple sources to verify accuracy
4. Update this section with verified citations
5. Flag any claims that cannot be verified for further investigation

### Notes:
- This verification section provides a systematic approach to validating the data
- All claims should be cross-checked with multiple independent sources
- Priority should be given to official government documents and recent data
- Any discrepancies between sources should be noted and investigated further
"""
    
    # Append verification section
    updated_content = content + verification_section
    
    # Write back to file
    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(updated_content)

def process_all_city_files():
    """Process all city .md files for verification."""
    # Get all .md files
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
    
    print(f"Processing {len(city_files)} city files for verification...")
    print("=" * 60)
    
    processed_count = 0
    error_count = 0
    
    for file_path in sorted(city_files):
        try:
            # Extract city and metric from filename
            filename = Path(file_path).stem
            parts = filename.split('_')
            
            if len(parts) >= 2:
                city = parts[0].replace('_', ' ').title()
                metric = parts[1].replace('_', ' ').title()
            else:
                continue
            
            # Read file content
            with open(file_path, 'r', encoding='utf-8') as f:
                content = f.read()
            
            # Extract verifiable claims
            claims = extract_verifiable_claims(content)
            
            # Update the file
            update_md_with_enhanced_verification(file_path, city, metric, claims)
            
            print(f"✓ {file_path:<35} | {city:<15} | {metric:<20} | {len(claims)} claims")
            processed_count += 1
            
        except Exception as e:
            print(f"✗ {file_path:<35} | ERROR: {str(e)}")
            error_count += 1
    
    print("=" * 60)
    print(f"Processing complete!")
    print(f"Successfully processed: {processed_count} files")
    print(f"Errors encountered: {error_count} files")
    
    if processed_count > 0:
        print(f"\nAll {processed_count} city files now have comprehensive verification sections.")
        print("Each file contains:")
        print("- Key claims identified for verification")
        print("- Specific search queries for finding sources")
        print("- Detailed verification methodology")
        print("- Source recommendations")
        print("- Data quality assessment framework")

if __name__ == "__main__":
    process_all_city_files()

