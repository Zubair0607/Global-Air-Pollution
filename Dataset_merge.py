import pandas as pd

pm25_data = pd.read_csv("deaths-from-PM2.5.csv")
health_data = pd.read_csv("pm25-air-pollution.csv")
gdp_data = pd.read_csv("air-pollution-gdp.csv")

# merging the datasets
merged_data = pd.merge(pm25_data, health_data, on=['Country', 'Year'], how='outer')
merged_data = pd.merge(merged_data, gdp_data, on=['Country', 'Year'], how='outer')

# Renaming the columns
merged_data.rename(columns={'Absolute deaths from ambient PM2.5 air pollution- State of Global Air': 'Deaths from PM2.5', 
                            'Concentrations of fine particulate matter (PM2.5) - Residence area type: Total': 'PM2.5 levels'}, inplace=True)

# dropping the unnecessary columns
merged_data = merged_data.drop(columns=["Code_x", "Code_y"])

# Saving the merged data
merged_data.to_csv("pm25-trends.csv", index=False)