import pandas as pd

pm25_data = pd.read_csv("deaths-from-PM2.5.csv")
health_data = pd.read_csv("pm25-air-pollution.csv")

merged_data = pd.merge(pm25_data, health_data, on=['Year', 'Entity'])

print(merged_data.head())
print(merged_data.columns)

# Saving the merged data
merged_data.to_csv("pm25-trends.csv", index=False)