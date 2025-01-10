import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
import numpy as np

# Loading the dataset
pm25_df = pd.read_csv("Datasets/MAIN_pm25-trends.csv")

# Aggregate PM2.5 levels and disease burden globally
aggregated_data = pm25_df.groupby("Country")[["PM2.5 Levels", "Disease Burden (DALYs)"]].mean().dropna()

# Prepare data for regression analysis
X = aggregated_data["PM2.5 Levels"].values.reshape(-1, 1)
y = aggregated_data["Disease Burden (DALYs)"].values

# Fit a linear regression model
model = LinearRegression()
model.fit(X, y)

# Generate regression line
x_range = np.linspace(X.min(), X.max(), 100).reshape(-1, 1)
y_pred = model.predict(x_range)

# Plot the scatter plot with regression line
plt.figure(figsize=(10, 6))
plt.scatter(aggregated_data["PM2.5 Levels"], aggregated_data["Disease Burden (DALYs)"], alpha=0.7, label="Data Points")
plt.plot(x_range, y_pred, color="red", linewidth=2, label=f"Regression Line")

# Add labels, title, and legend
plt.title("PM2.5 Levels vs Disease Burden (DALYs)", fontsize=14)
plt.xlabel("PM2.5 Levels (µg/m³)", fontsize=12)
plt.ylabel("Disease Burden (DALYs)", fontsize=12)
plt.legend(fontsize=10)
plt.grid(alpha=0.5)
plt.tight_layout()

# Saving the figure
plt.savefig('Visualisations/PM25 and its Health impacts.png', bbox_inches='tight')