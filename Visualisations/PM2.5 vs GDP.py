import pandas as pd
import matplotlib.pyplot as plt

# Load the dataset
pm25_df = pd.read_csv("Datasets/MAIN_pm25-trends.csv")

# Clean the GDP column and convert it to numeric
pm25_df["GDP per Capita"] = pm25_df["GDP per Capita"].replace({',': ''}, regex=True).astype(float)

# Group by PM2.5 Levels ranges (binning)
pm25_df["PM2.5 Group"] = pd.cut(pm25_df["PM2.5 Levels"], bins=10, labels=False)

# Aggregate GDP per capita by PM2.5 group
line_data = pm25_df.groupby("PM2.5 Group")[["PM2.5 Levels", "GDP per Capita"]].mean().dropna()

# Plot the line chart
plt.figure(figsize=(10, 6))
plt.plot(line_data["PM2.5 Levels"], line_data["GDP per Capita"], marker="o", color="green", label="GDP per Capita")

# Add labels, title, and legend
plt.title("PM2.5 Levels vs GDP per Capita", fontsize=14)
plt.xlabel("PM2.5 Levels (µg/m³, Aggregated)", fontsize=12)
plt.ylabel("GDP per Capita (USD)", fontsize=12)
plt.legend(fontsize=10)
plt.grid(alpha=0.5)

plt.tight_layout()
plt.show()





