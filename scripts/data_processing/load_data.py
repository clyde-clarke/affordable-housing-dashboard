import os
import pandas as pd

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

# Function to read data from markdown files
def load_data_from_files():
    data = {}
    for city in cities:
        data[city] = {}
        for category in indicator_categories:
            # Sanitize city name for file path
            city_filename = city.lower().replace(" ", "_").replace(".", "")
            category_filename = category.lower().replace(" ", "_").replace("/", "_")
            file_path = f"/home/ubuntu/{city_filename}_{category_filename}.md"
            
            if os.path.exists(file_path):
                with open(file_path, 'r') as f:
                    data[city][category] = f.read()
            else:
                data[city][category] = ""
    return data

# Load the data
loaded_data = load_data_from_files()

# For now, just print the loaded data to verify
for city, indicators in loaded_data.items():
    print(f"--- {city} ---")
    for indicator, content in indicators.items():
        print(f"- {indicator}: {len(content)} bytes")



