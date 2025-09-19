import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Read the complete data
df = pd.read_csv('complete_normalized_scores_with_citations.csv')

# Set the city names as index
df.set_index('City', inplace=True)

# Remove the Overall Score column for the heatmap
heatmap_data = df.drop('Overall Score', axis=1)

# Create the heatmap using matplotlib
fig, ax = plt.subplots(figsize=(14, 18))

# Create the heatmap
im = ax.imshow(heatmap_data.values, cmap='RdYlGn', aspect='auto', vmin=0, vmax=100)

# Set ticks and labels
ax.set_xticks(range(len(heatmap_data.columns)))
ax.set_yticks(range(len(heatmap_data.index)))
ax.set_xticklabels(heatmap_data.columns, rotation=45, ha='right', fontsize=10)
ax.set_yticklabels(heatmap_data.index, fontsize=9)

# Add text annotations
for i in range(len(heatmap_data.index)):
    for j in range(len(heatmap_data.columns)):
        text = ax.text(j, i, f'{heatmap_data.iloc[i, j]:.1f}',
                      ha="center", va="center", color="black", fontsize=8)

# Add colorbar
cbar = plt.colorbar(im, ax=ax)
cbar.set_label('Score (0-100)', rotation=270, labelpad=20)

# Set title and labels
plt.title('Complete Affordable Housing Indicators Across Major US Cities\n(Updated with Corrected Funding Data and Complete NYC/LA Data)', 
          fontsize=16, fontweight='bold', pad=20)
plt.xlabel('Indicator Categories', fontsize=12, fontweight='bold')
plt.ylabel('Cities', fontsize=12, fontweight='bold')

# Adjust layout to prevent label cutoff
plt.tight_layout()

# Save the heatmap
plt.savefig('complete_normalized_scores_heatmap.png', dpi=300, bbox_inches='tight')
plt.show()

print("Complete heatmap saved as 'complete_normalized_scores_heatmap.png'")

# Create a summary table showing the changes
print("\n" + "="*100)
print("COMPLETE DATA CORRECTIONS SUMMARY")
print("="*100)
print(f"{'City':<20} {'Old Overall':<12} {'New Overall':<12} {'Change':<10} {'New Rank':<8}")
print("-" * 80)

# Calculate old overall scores (with 0 funding for all cities)
old_funding = [0] * len(df)
old_overall = []
for i, row in df.iterrows():
    old_score = (old_funding[0] * 0.25 + 
                row['Housing Supply'] * 0.25 + 
                row['Resident Stability'] * 0.20 + 
                row['Policy Implementation'] * 0.20 + 
                row['Transparency/Data Access'] * 0.10)
    old_overall.append(old_score)

new_overall = df['Overall Score'].values

# Sort by new overall score for ranking
df_sorted = df.sort_values('Overall Score', ascending=False)
rankings = {city: i+1 for i, city in enumerate(df_sorted.index)}

for i, city in enumerate(df.index):
    change = new_overall[i] - old_overall[i]
    rank = rankings[city]
    print(f"{city:<20} {old_overall[i]:<12.2f} {new_overall[i]:<12.2f} +{change:<9.2f} {rank:<8}")

print("\n" + "="*100)
print("FINAL RANKINGS WITH COMPLETE DATA")
print("="*100)

for i, (city, row) in enumerate(df_sorted.iterrows(), 1):
    print(f"{i:2d}. {city:<20} {row['Overall Score']:.2f}")

print(f"\nTotal cities analyzed: {len(df)}")
print("\nKey Changes:")
print("- NYC and LA now have complete data across all categories")
print("- Funding scores reflect actual budget commitments and investments")
print("- All data includes proper citations and sources for validation")
print("- Rankings significantly changed with corrected funding data")

