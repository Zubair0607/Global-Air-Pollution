import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
import numpy as np

# Load the dataset
pm25_df = pd.read_csv("Datasets/MAIN_pm25-trends.csv")

# Aggregate PM2.5 levels and deaths globally by year
global_pm25 = pm25_df.groupby("Year")["PM2.5 Levels"].mean().reset_index()
global_deaths = pm25_df.groupby("Year")["Deaths from PM2.5"].sum().reset_index()

# Merge the aggregated data
merged_data = pd.merge(global_pm25, global_deaths, on="Year")

# Add Forecasts using Linear Regression
model_pm25 = LinearRegression()
model_deaths = LinearRegression()

# Prepare data for forecasting
years = merged_data["Year"].values.reshape(-1, 1)
future_years = np.array(range(2022, 2031)).reshape(-1, 1)
all_years = np.vstack((years, future_years))

# Fit models
model_pm25.fit(years, merged_data["PM2.5 Levels"])
model_deaths.fit(years, merged_data["Deaths from PM2.5"])

# Generate predictions
forecast_pm25 = model_pm25.predict(all_years)
forecast_deaths = model_deaths.predict(all_years)

# Plotting the updated figure
fig, ax1 = plt.subplots(figsize=(12, 7))

# Plot historical PM2.5 Levels as a line chart
ax1.set_title("Global Trends and Forecasts: PM2.5 Levels and Health Impacts", fontsize=16)
ax1.set_xlabel("Year", fontsize=12)
ax1.set_ylabel("PM2.5 Levels (µg/m³)", fontsize=12, color="tab:blue")
ax1.plot(merged_data["Year"], merged_data["PM2.5 Levels"], marker="o", label="PM2.5 Levels (Historical)", color="tab:blue", linewidth=2)
ax1.plot(all_years.flatten(), forecast_pm25, "--", label="PM2.5 Levels (Forecast)", color="tab:blue", alpha=0.6)

# Create a secondary Y-axis for deaths
ax2 = ax1.twinx()
ax2.set_ylabel("Deaths from PM2.5 (millions)", fontsize=12, color="tab:red")
ax2.bar(merged_data["Year"], merged_data["Deaths from PM2.5"] / 1_000_000, label="Deaths from PM2.5 (Historical)", color="tab:red", alpha=0.6, width=0.8)
ax2.plot(all_years.flatten(), forecast_deaths / 1_000_000, "--", label="Deaths from PM2.5 (Forecast)", color="tab:red", alpha=0.6)

# Add legends
ax1.legend(loc="upper left", fontsize=10)
ax2.legend(loc="upper right", fontsize=10)

# Enhance layout
plt.grid(axis="y", linestyle="--", alpha=0.6)
plt.tight_layout()

# Show the plot
plt.show()