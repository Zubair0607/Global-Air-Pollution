import pandas as pd
import geopandas as gpd
import matplotlib.pyplot as plt

# Load your dataset
pm25_df = pd.read_csv("Datasets/MAIN_pm25-trends.csv", sep="\t")

# Load a world shapefile (geopandas provides built-in datasets)
world = gpd.read_file('ne_110m_admin_0_countries')

# Ensure the country names in both datasets match (standardize naming conventions)
pm25_df["Country"] = pm25_df["Country"].str.strip()
world["name"] = world["name"].str.strip()

# Aggregate PM2.5 levels by country (mean value if multiple records exist per country)
country_pm25 = pm25_df.groupby("Country")["PM2.5 Levels"].mean().reset_index()

# Merge the PM2.5 data with the world GeoDataFrame
world_pm25 = world.merge(country_pm25, left_on="name", right_on="Country", how="left")

# Plot a choropleth map of PM2.5 levels
fig, ax = plt.subplots(1, 1, figsize=(15, 10))
world_pm25.plot(column="PM2.5 Levels", cmap="OrRd", legend=True, 
                legend_kwds={'label': "PM2.5 Levels (µg/m³)"},
                missing_kwds={"color": "lightgrey", "label": "No data"},
                ax=ax)
ax.set_title("Global PM2.5 Levels by Country", fontsize=16)
ax.axis("off")

# Show the plot
plt.tight_layout()
plt.show()
