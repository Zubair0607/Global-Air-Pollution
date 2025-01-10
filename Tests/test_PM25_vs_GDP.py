import pandas as pd
import matplotlib.pyplot as plt

def load_and_clean_data(file_path):
    # Load and clean the dataset.
    pm25_df = pd.read_csv(file_path)
    pm25_df["GDP per Capita"] = pm25_df["GDP per Capita"].replace({',': ''}, regex=True).astype(float)
    return pm25_df

def group_by_pm25_levels(df, bins=10):
    # Group the dataset by PM2.5 Levels ranges and calculate aggregated GDP per capita.
    df["PM2.5 Group"] = pd.cut(df["PM2.5 Levels"], bins=bins, labels=False)
    return df.groupby("PM2.5 Group")[["PM2.5 Levels", "GDP per Capita"]].mean().dropna()

def plot_pm25_vs_gdp(line_data, output_path):
    # Plot a line chart of PM2.5 Levels vs GDP per Capita.
    plt.figure(figsize=(10, 6))
    plt.plot(line_data["PM2.5 Levels"], line_data["GDP per Capita"], marker="o", color="green", label="GDP per Capita")

    # Add labels, title, and legend
    plt.title("PM2.5 Levels vs GDP per Capita", fontsize=14)
    plt.xlabel("PM2.5 Levels (µg/m³, Aggregated)", fontsize=12)
    plt.ylabel("GDP per Capita (USD)", fontsize=12)
    plt.legend(fontsize=10)
    plt.grid(alpha=0.5)
    plt.tight_layout()

    # Save the figure
    plt.savefig(output_path, bbox_inches='tight')

def main():
    # Main function to orchestrate data loading, processing, and visualization.
    
    # Load and clean data
    file_path = "Datasets/MAIN_pm25-trends.csv"
    pm25_df = load_and_clean_data(file_path)

    # Group data by PM2.5 Levels
    line_data = group_by_pm25_levels(pm25_df, bins=10)

    # Plot and save the line chart
    output_path = 'Visualisations/PM25 vs GDP.png'
    plot_pm25_vs_gdp(line_data, output_path)

if __name__ == "__main__":
    main()
