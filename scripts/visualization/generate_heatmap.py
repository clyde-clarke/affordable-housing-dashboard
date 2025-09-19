import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the normalized scores data
normalized_scores_df = pd.read_csv("normalized_scores.csv", index_col=0)

# Create the heatmap
plt.figure(figsize=(14, 10))
sns.heatmap(normalized_scores_df, annot=True, cmap="YlGnBu", fmt=".1f", linewidths=.5)
plt.title("Normalized Affordable Housing Scores by City and Category")
plt.xlabel("Indicator Category")
plt.ylabel("City")
plt.tight_layout()

# Save the heatmap
plt.savefig("normalized_scores_heatmap.png")
print("Heatmap saved to normalized_scores_heatmap.png")


