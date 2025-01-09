import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
import numpy as np

def load_data(file_path):
    # Load the dataset from the file path.
    return pd.read_csv(file_path)

def aggregate_data(df):
    # Aggregate PM2.5 levels and disease burden globally by country.
    return df.groupby("Country")[["PM2.5 Levels", "Disease Burden (DALYs)"]].mean().dropna()

def perform_regression(aggregated_data):
    # Perform linear regression analysis between PM2.5 Levels and Disease Burden (DALYs).
    X = aggregated_data["PM2.5 Levels"].values.reshape(-1, 1)
    y = aggregated_data["Disease Burden (DALYs)"].values

    model = LinearRegression()
    model.fit(X, y)

    x_range = np.linspace(X.min(), X.max(), 100).reshape(-1, 1)
    y_pred = model.predict(x_range)

    return model, x_range, y_pred

def plot_regression(aggregated_data, x_range, y_pred, output_path):
    # Plot scatter plot and regression line.
    plt.figure(figsize=(10, 6))
    plt.scatter(aggregated_data["PM2.5 Levels"], aggregated_data["Disease Burden (DALYs)"], alpha=0.7, label="Data Points")
    plt.plot(x_range, y_pred, color="red", linewidth=2, label="Regression Line")

    plt.title("PM2.5 Levels vs Disease Burden (DALYs)", fontsize=14)
    plt.xlabel("PM2.5 Levels (µg/m³)", fontsize=12)
    plt.ylabel("Disease Burden (DALYs)", fontsize=12)
    plt.legend(fontsize=10)
    plt.grid(alpha=0.5)
    plt.tight_layout()

    plt.savefig(output_path, bbox_inches='tight')

def main():
    # Main function to load data, perform regression analysis, and plot results.
    
    # Load data
    file_path = "Datasets/MAIN_pm25-trends.csv"
    pm25_df = load_data(file_path)

    # Aggregate data
    aggregated_data = aggregate_data(pm25_df)

    # Perform regression
    model, x_range, y_pred = perform_regression(aggregated_data)

    # Plot results
    output_path = 'Visualisations/PM25 and its Health impacts.png'
    plot_regression(aggregated_data, x_range, y_pred, output_path)

if __name__ == "__main__":
    main()