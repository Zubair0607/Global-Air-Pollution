import pandas as pd
import geopandas as gpd
import matplotlib.pyplot as plt

# Load your dataset
pm25_df = pd.read_csv("Datasets/MAIN_pm25-trends.csv", sep="\t")

# Load a world shapefile (geopandas provides built-in datasets)
world = gpd.read_file('ne_110m_admin_0_countries')


print(world["ADMIN"].unique())  # GeoPandas world dataset
print(pm25_df['Country'].unique())