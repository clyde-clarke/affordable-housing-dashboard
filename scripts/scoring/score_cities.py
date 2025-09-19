import pandas as pd
import os

# Define the cities and indicator categories
cities = [
    "New York City", "Los Angeles", "Chicago", "Houston", "Phoenix",
    "San Antonio", "San Diego", "Dallas", "San Jose", "Austin",
    "Jacksonville", "Fort Worth", "Columbus", "Charlotte", "San Francisco",
    "Seattle", "Denver", "Washington, D.C.", "Detroit", "New Orleans",
    "Boston", "Philadelphia", "Miami", "Atlanta"
]

indicator_categories = [
    "Funding", "Housing Supply", "Resident Stability",
    "Policy Implementation", "Transparency/Data Access"
]

# Define weights for each category
category_weights = {
    "Funding": 0.25,
    "Housing Supply": 0.25,
    "Resident Stability": 0.20,
    "Policy Implementation": 0.20,
    "Transparency/Data Access": 0.10
}

# Function to extract a numerical score from the content of a markdown file
def extract_score_from_content(content, category):
    # This is a placeholder for actual NLP/text analysis.
    # For now, we will assign a dummy score based on content length or presence of keywords.
    # In a real scenario, this would involve more sophisticated parsing.
    score = 0
    if content:
        # Example: simple scoring based on length of content (more content = higher score)
        # This needs to be replaced with actual scoring logic based on the project framework.
        score = min(len(content) / 100, 100) # Scale to 0-100, max 100 for very long content

        # Add some keyword-based scoring for demonstration
        if "historic investment" in content.lower() or "significant funding" in content.lower():
            score += 10
        if "shortage" in content.lower() or "crisis" in content.lower():
            score -= 5
        if "dashboard" in content.lower() or "open data" in content.lower():
            score += 10
        if "eviction" in content.lower() or "displacement" in content.lower():
            score -= 5
        if "policy" in content.lower() or "ordinance" in content.lower():
            score += 5

    return max(0, min(100, score)) # Ensure score is between 0 and 100

# Function to read data from markdown files and extract scores
def load_and_score_data():
    city_scores = {}
    for city in cities:
        city_scores[city] = {}
        for category in indicator_categories:
            city_filename = city.lower().replace(" ", "_").replace(".", "").replace(",", "")
            category_filename = category.lower().replace(" ", "_").replace("/", "_")
            file_path = f"/home/ubuntu/{city_filename}_{category_filename}.md"
            
            content = ""
            if os.path.exists(file_path):
                with open(file_path, 'r') as f:
                    content = f.read()
            
            score = extract_score_from_content(content, category)
            city_scores[city][category] = score
    return city_scores

# Load and score the data
data = load_and_score_data()

# Create a DataFrame to store the scores
scores_df = pd.DataFrame(index=cities, columns=indicator_categories)

# Populate the DataFrame with raw scores
for city, indicators in data.items():
    for indicator, score in indicators.items():
        scores_df.loc[city, indicator] = score

# Normalize scores for each indicator category
normalized_scores_df = scores_df.copy()
for indicator in indicator_categories:
    min_val = scores_df[indicator].min()
    max_val = scores_df[indicator].max()
    if max_val == min_val:
        normalized_scores_df[indicator] = 0 # All scores are the same, normalize to 0
    else:
        normalized_scores_df[indicator] = scores_df[indicator].apply(lambda x: ((x - min_val) / (max_val - min_val)) * 100)

# Calculate overall weighted score for each city
overall_scores = {}
for city in cities:
    weighted_score = 0
    for indicator, weight in category_weights.items():
        weighted_score += normalized_scores_df.loc[city, indicator] * weight
    overall_scores[city] = weighted_score

overall_scores_df = pd.DataFrame.from_dict(overall_scores, orient='index', columns=['Overall Score'])
overall_scores_df = overall_scores_df.sort_values(by='Overall Score', ascending=False)

print("Normalized Scores (0-100 scale):")
print(normalized_scores_df)
print("\nOverall Weighted Scores and Ranks:")
print(overall_scores_df)

# Save results to a file
normalized_scores_df.to_csv('normalized_scores.csv')
overall_scores_df.to_csv('overall_scores.csv')

print("\nResults saved to normalized_scores.csv and overall_scores.csv")


