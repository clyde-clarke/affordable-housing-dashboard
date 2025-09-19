import pandas as pd
import matplotlib.pyplot as plt

# Load the overall scores data
overall_scores_df = pd.read_csv("overall_scores.csv", index_col=0)

# Sort the DataFrame by 'Overall Score' in descending order
overall_scores_df = overall_scores_df.sort_values(by='Overall Score', ascending=False)

# Create the bar chart
plt.figure(figsize=(12, 8))
plt.barh(overall_scores_df.index, overall_scores_df["Overall Score"], color='skyblue')
plt.xlabel("Overall Score")
plt.ylabel("City")
plt.title("Overall Affordable Housing Scores by City")
plt.gca().invert_yaxis() # Invert y-axis to have the highest score at the top
plt.tight_layout()

# Save the chart
plt.savefig("overall_scores_bar_chart.png")
print("Bar chart saved to overall_scores_bar_chart.png")


