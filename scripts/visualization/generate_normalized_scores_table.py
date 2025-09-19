import pandas as pd

# Load the normalized scores data
normalized_scores_df = pd.read_csv("normalized_scores.csv", index_col=0)

# Print the table
print("Normalized Scores (0-100 scale) by City and Category:")
print(normalized_scores_df.to_markdown())

# Save the table to a markdown file
with open("normalized_scores_table.md", "w") as f:
    f.write("# Normalized Scores (0-100 scale) by City and Category\n\n")
    f.write(normalized_scores_df.to_markdown())

print("Normalized scores table saved to normalized_scores_table.md")


