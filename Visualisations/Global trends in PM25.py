import pandas as pd
import matplotlib.pyplot as plt

emissions_df = pd.read_csv("Datasets/MAIN_pm25-trends.csv")

# Plotting the headline figure
fig, ax1 = plt.subplots(figsize=(10, 6))

# Plot PM2.5 Levels as a line chart
ax1.set_title("Global Trends in PM2.5 Levels and Health Impacts", fontsize=14)
ax1.set_xlabel("Year", fontsize=12)
ax1.set_ylabel("PM2.5 Levels (µg/m³)", fontsize=12, color="tab:blue")
line1 = ax1.plot(emissions_df["Year"], emissions_df["PM2.5 levels"], label="PM2.5 Levels", color="tab:blue", linewidth=2)

# Create a secondary Y-axis for deaths
ax2 = ax1.twinx()
ax2.set_ylabel("Deaths from PM2.5 (millions)", fontsize=12, color="tab:red")
bar2 = ax2.bar(emissions_df["Year"], [d / 1_000_000 for d in emissions_df["Deaths from PM2.5"]], 
               label="Deaths from PM2.5", color="tab:red", alpha=0.6, width=3)

# Add legends
ax1.legend(loc="upper left", fontsize=10)
ax2.legend(loc="upper right", fontsize=10)

# Enhance layout
plt.grid(axis="y", linestyle="--", alpha=0.6)
plt.tight_layout()

# Show the plot
plt.show()
