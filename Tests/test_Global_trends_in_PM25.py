import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
import numpy as np

def load_data(file_path):
    # Load dataset from the file path.
    return pd.read_csv(file_path)

def aggregate_data(df):
    # Aggregate PM2.5 levels and deaths globally by year.
    global_pm25 = df.groupby("Year")["PM2.5 Levels"].mean().reset_index()
    global_deaths = df.groupby("Year")["Deaths from PM2.5"].sum().reset_index()
    return pd.merge(global_pm25, global_deaths, on="Year")

def forecast_trends(data, target_column, future_years_range):
    # Forecast trends using linear regression.
    model = LinearRegression()
    years = data["Year"].values.reshape(-1, 1)
    future_years = np.array(future_years_range).reshape(-1, 1)
    all_years = np.vstack((years, future_years))
    
    model.fit(years, data[target_column])
    return all_years, model.predict(all_years)

def plot_trends(merged_data, forecast_pm25, forecast_deaths, all_years, output_path):
    # Plot historical and forecasted PM2.5 levels and deaths.
    fig, ax1 = plt.subplots(figsize=(12, 7))

    # Plot historical PM2.5 Levels as a line chart
    ax1.set_title("Global Trends and Forecasts: PM2.5 Levels and Caused Deaths", fontsize=16)
    ax1.set_xlabel("Year", fontsize=15)
    ax1.set_ylabel("PM2.5 Levels (µg/m³)", fontsize=15, color="tab:blue")
    ax1.plot(merged_data["Year"], merged_data["PM2.5 Levels"], marker="o", label="PM2.5 Levels (Historical)", color="tab:blue", linewidth=2)
    ax1.plot(all_years.flatten(), forecast_pm25, "--", label="PM2.5 Levels (Forecast)", color="tab:blue", alpha=0.6)

    # Create a secondary Y-axis for deaths
    ax2 = ax1.twinx()
    ax2.set_ylabel("Deaths from PM2.5 (millions)", fontsize=15, color="tab:red")
    ax2.bar(merged_data["Year"], merged_data["Deaths from PM2.5"] / 1_000_000, label="Deaths from PM2.5 (Historical)", color="tab:red", alpha=0.6, width=0.8)
    ax2.plot(all_years.flatten(), forecast_deaths / 1_000_000, "--", label="Deaths from PM2.5 (Forecast)", color="tab:red", alpha=0.6)

    # Add legends
    ax1.legend(loc="upper left", fontsize=10)
    ax2.legend(loc="upper right", fontsize=10)

    plt.grid(axis="y", linestyle="--", alpha=0.6)
    plt.tight_layout()

    # Save the figure
    plt.savefig(output_path, bbox_inches='tight')

def main():
    # Main function to orchestrate data processing, forecasting, and visualization.
    
    # Load data
    file_path = "Datasets/MAIN_pm25-trends.csv"
    pm25_df = load_data(file_path)

    # Aggregate data
    merged_data = aggregate_data(pm25_df)

    # Forecast trends
    future_years_range = range(2022, 2031)
    all_years_pm25, forecast_pm25 = forecast_trends(merged_data, "PM2.5 Levels", future_years_range)
    all_years_deaths, forecast_deaths = forecast_trends(merged_data, "Deaths from PM2.5", future_years_range)

    # Plot trends
    output_path = 'Visualisations/Global Trends in PM25.png'
    plot_trends(merged_data, forecast_pm25, forecast_deaths, all_years_pm25, output_path)

if __name__ == "__main__":
    main()
