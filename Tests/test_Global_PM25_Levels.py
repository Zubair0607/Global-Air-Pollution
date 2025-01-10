import pandas as pd
import geopandas as gpd
import matplotlib.pyplot as plt

def load_pm25_data(file_path):
    # Load PM2.5 dataset from the file path.
    return pd.read_csv(file_path)

def load_world_shapefile(file_path):
    # Load a world shapefile as a GeoDataFrame.
    return gpd.read_file(file_path)

def filter_data_for_year(df, year):
    # Filter the PM2.5 dataset for a specific year.
    return df[df["Year"] == year]

def aggregate_pm25_by_country(df):
    # Aggregate PM2.5 levels by country.
    return df.groupby("Country")["PM2.5 Levels"].mean().reset_index()

def merge_pm25_with_world(world_gdf, pm25_df):
    # Merge PM2.5 data with the world GeoDataFrame.
    return world_gdf.merge(pm25_df, left_on="ADMIN", right_on="Country", how="left")

def plot_pm25_choropleth(world_pm25, output_path):
    # Plot a choropleth map of PM2.5 levels by country.
    fig, ax = plt.subplots(1, 1, figsize=(13, 8))
    world_pm25.boundary.plot(ax=ax, linewidth=1, color='black') 
    world_pm25.plot(column="PM2.5 Levels", cmap="OrRd", legend=True, 
                    legend_kwds={'label': "PM2.5 Levels (µg/m³)"},
                    missing_kwds={"color": "lightgrey", "label": "No data"},
                    ax=ax)
    ax.set_title("Global PM2.5 Levels by Country in 2021", fontsize=16)
    ax.axis("off")
    plt.tight_layout()
    plt.savefig(output_path, bbox_inches='tight')

def main():
    # Main function to load data, process, and plot the choropleth map.
    pm25_file_path = "Datasets/MAIN_pm25-trends.csv"
    shapefile_path = "ne_110m_admin_0_countries"
    output_path = 'Visualisations/Global PM2.5 Levels.png'

    # Load datasets
    pm25_df = load_pm25_data(pm25_file_path)
    world_gdf = load_world_shapefile(shapefile_path)

    # Process data
    pm25_df_filtered = filter_data_for_year(pm25_df, year=2021)
    country_pm25 = aggregate_pm25_by_country(pm25_df_filtered)
    world_pm25 = merge_pm25_with_world(world_gdf, country_pm25)

    # Plot and save the choropleth map
    plot_pm25_choropleth(world_pm25, output_path)

if __name__ == "__main__":
    main()