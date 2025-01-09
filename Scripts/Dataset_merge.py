import pandas as pd

pm25_data = pd.read_csv("Datasets/pm25-air-pollution.csv")
health_data = pd.read_csv("Datasets/deaths-from-PM2.5.csv")
gdp_data = pd.read_csv("Datasets/air-pollution-gdp.csv")
disease_data = pd.read_csv("Datasets/pm25-disease-burden.csv")
emission_data = pd.read_csv("Datasets/air-pollution-emissions.csv")

# merging the datasets
merged_data = pd.merge(pm25_data, health_data, on=['Country', 'Year'], how='outer')
merged_data = pd.merge(merged_data, gdp_data, on=['Country', 'Year'], how='outer')
merged_data = pd.merge(merged_data, disease_data, on=['Country', 'Year'], how='outer')
merged_data = pd.merge(merged_data, emission_data, on=['Country', 'Year'], how='outer')

# Renaming the columns
merged_data.rename(columns={'Absolute deaths from ambient PM2.5 air pollution- State of Global Air': 'Deaths from PM2.5', }, inplace=True)

# dropping the unnecessary columns and rows
merged_data = merged_data.drop(columns="Code")
merged_data = merged_data.dropna(subset=['Deaths from PM2.5', 'PM2.5 Levels','GDP per Capita'], how='all')

# Saving the merged data
merged_data.to_csv("Datasets/MAIN_pm25-trends.csv", index=False)