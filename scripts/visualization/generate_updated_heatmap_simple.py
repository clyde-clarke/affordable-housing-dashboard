import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Read the updated data
df = pd.read_csv('updated_normalized_scores.csv')

# Set the city names as index
df.set_index('City', inplace=True)

# Remove the Overall Score column for the heatmap
heatmap_data = df.drop('Overall Score', axis=1)

# Create the heatmap using matplotlib
fig, ax = plt.subplots(figsize=(12, 16))

# Create the heatmap
im = ax.imshow(heatmap_data.values, cmap='RdYlGn', aspect='auto', vmin=0, vmax=100)

# Set ticks and labels
ax.set_xticks(range(len(heatmap_data.columns)))
ax.set_yticks(range(len(heatmap_data.index)))
ax.set_xticklabels(heatmap_data.columns, rotation=45, ha='right')
ax.set_yticklabels(heatmap_data.index)

# Add text annotations
for i in range(len(heatmap_data.index)):
    for j in range(len(heatmap_data.columns)):
        text = ax.text(j, i, f'{heatmap_data.iloc[i, j]:.1f}',
                      ha="center", va="center", color="black", fontsize=8)

# Add colorbar
cbar = plt.colorbar(im, ax=ax)
cbar.set_label('Score (0-100)', rotation=270, labelpad=20)

# Set title and labels
plt.title('Updated Affordable Housing Indicators Across Major US Cities\n(Normalized Scores with Corrected Funding Data)', 
          fontsize=16, fontweight='bold', pad=20)
plt.xlabel('Indicator Categories', fontsize=12, fontweight='bold')
plt.ylabel('Cities', fontsize=12, fontweight='bold')

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

