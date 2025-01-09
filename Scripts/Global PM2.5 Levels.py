import pandas as pd
import geopandas as gpd
import matplotlib.pyplot as plt

# Load the dataset
pm25_df = pd.read_csv("Datasets/MAIN_pm25-trends.csv")

# Load a world shapefile
world = gpd.read_file('ne_110m_admin_0_countries')

# Filter data for the year 2021
pm25_df_filtered = pm25_df[pm25_df["Year"] == 2021]

# Aggregate PM2.5 levels by country
country_pm25 = pm25_df_filtered.groupby("Country")["PM2.5 Levels"].mean().reset_index()

# Merge the PM2.5 data with the world GeoDataFrame
world_pm25 = world.merge(country_pm25, left_on="ADMIN", right_on="Country", how="left")

# Plot a choropleth map of PM2.5 levels
fig, ax = plt.subplots(1, 1, figsize=(13, 8))
world_pm25.boundary.plot(ax=ax, linewidth=1, color='black') 
world_pm25.plot(column="PM2.5 Levels", cmap="OrRd", legend=True, 
                legend_kwds={'label': "PM2.5 Levels (µg/m³)"},
                missing_kwds={"color": "lightgrey", "label": "No data"},
                ax=ax)
ax.set_title("Global PM2.5 Levels by Country in 2021", fontsize=16)
ax.axis("off")
plt.tight_layout()

# Saving the figure
plt.savefig('Visualisations/Global PM2.5 Levels.png', bbox_inches='tight')
