import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

# Read the updated data
df = pd.read_csv('updated_normalized_scores.csv')

# Set the city names as index
df.set_index('City', inplace=True)

# Remove the Overall Score column for the heatmap
heatmap_data = df.drop('Overall Score', axis=1)

# Create the heatmap
plt.figure(figsize=(12, 16))
sns.heatmap(heatmap_data, 
            annot=True, 
            fmt='.1f', 
            cmap='RdYlGn', 
            vmin=0, 
            vmax=100,
            cbar_kws={'label': 'Score (0-100)'},
            linewidths=0.5)

plt.title('Updated Affordable Housing Indicators Across Major US Cities\n(Normalized Scores with Corrected Funding Data)', 
          fontsize=16, fontweight='bold', pad=20)
plt.xlabel('Indicator Categories', fontsize=12, fontweight='bold')
plt.ylabel('Cities', fontsize=12, fontweight='bold')

# Rotate x-axis labels for better readability
plt.xticks(rotation=45, ha='right')
plt.yticks(rotation=0)

# Adjust layout to prevent label cutoff
plt.tight_layout()

# Save the heatmap
plt.savefig('updated_normalized_scores_heatmap.png', dpi=300, bbox_inches='tight')
plt.show()

print("Updated heatmap saved as 'updated_normalized_scores_heatmap.png'")

# Also create a summary table showing the changes
print("\n" + "="*80)
print("FUNDING SCORE CORRECTIONS SUMMARY")
print("="*80)
print(f"{'City':<20} {'Old Funding':<12} {'New Funding':<12} {'Change':<10}")
print("-" * 60)

# Original funding scores were all 0
old_funding = [0] * len(df)
new_funding = df['Funding'].values

for i, city in enumerate(df.index):
    change = new_funding[i] - old_funding[i]
    print(f"{city:<20} {old_funding[i]:<12} {new_funding[i]:<12} +{change:<9}")

print("\n" + "="*80)
print("UPDATED OVERALL RANKINGS")
print("="*80)

# Sort by overall score
df_sorted = df.sort_values('Overall Score', ascending=False)
for i, (city, row) in enumerate(df_sorted.iterrows(), 1):
    print(f"{i:2d}. {city:<20} {row['Overall Score']:.2f}")

print(f"\nTotal cities analyzed: {len(df)}")
print("Note: Funding scores now reflect actual budget commitments and funding levels")

