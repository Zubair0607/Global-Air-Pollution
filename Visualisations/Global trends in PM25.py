import pandas as pd
import matplotlib.pyplot as plt

# Load the dataset
pm25_df = pd.read_csv("Datasets/MAIN_pm25-trends.csv")

# Aggregate PM2.5 levels globally by year
global_pm25 = pm25_df.groupby("Year")["PM2.5 Levels"].mean().reset_index()

# Aggregate deaths globally by year
global_deaths = pm25_df.groupby("Year")["Deaths from PM2.5"].sum().reset_index()

# Merge the aggregated data
merged_data = pd.merge(global_pm25, global_deaths, on="Year")

# Plotting the dual-axis figure
fig, ax1 = plt.subplots(figsize=(10, 6))

# Plot PM2.5 Levels as a line chart
ax1.set_title("Global Trends in PM2.5 Levels and Health Impacts", fontsize=14)
ax1.set_xlabel("Year", fontsize=12)
ax1.set_ylabel("PM2.5 Levels (µg/m³)", fontsize=12, color="tab:blue")
line1 = ax1.plot(merged_data["Year"], merged_data["PM2.5 Levels"], marker="o", label="PM2.5 Levels", color="tab:blue", linewidth=2)

# Create a secondary Y-axis for deaths
ax2 = ax1.twinx()
ax2.set_ylabel("Deaths from PM2.5 (millions)", fontsize=12, color="tab:red")
bar2 = ax2.bar(merged_data["Year"], merged_data["Deaths from PM2.5"] / 1_000_000, 
               label="Deaths from PM2.5", color="tab:red", alpha=0.6, width=0.8)

# Add legends
ax1.legend(loc="upper left", fontsize=10)
ax2.legend(loc="upper right", fontsize=10)

plt.grid(axis="y", linestyle="--", alpha=0.6)
plt.tight_layout()
plt.show()