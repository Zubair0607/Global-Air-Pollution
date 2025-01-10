import pandas as pd

def load_data(file_paths):
    # Load datasets from the file path
    dataframes = {}
    for name, path in file_paths.items():
        dataframes[name] = pd.read_csv(path)
    return dataframes

def merge_datasets(dataframes, keys):
    # Merge multiple datasets on common keys.
    merged_data = None
    for df in dataframes.values():
        if merged_data is None:
            merged_data = df
        else:
            merged_data = pd.merge(merged_data, df, on=keys, how='outer')
    return merged_data

def clean_data(df):
    # Clean the merged dataset by renaming, dropping unnecessary columns, and filtering rows.
    df.rename(columns={'Absolute deaths from ambient PM2.5 air pollution- State of Global Air': 'Deaths from PM2.5'}, inplace=True)
    df = df.drop(columns="Code", errors='ignore')
    df = df.dropna(subset=['Deaths from PM2.5', 'PM2.5 Levels', 'GDP per Capita'], how='all')
    return df

def save_data(df, output_path):
    # Save the cleaned DataFrame to a CSV file.
    df.to_csv(output_path, index=False)

def main():
    # Main function to orchestrate data loading, merging, cleaning, and saving.
    file_paths = {
        'pm25_data': "Datasets/pm25-air-pollution.csv",
        'health_data': "Datasets/deaths-from-PM2.5.csv",
        'gdp_data': "Datasets/air-pollution-gdp.csv",
        'disease_data': "Datasets/pm25-disease-burden.csv",
        'emission_data': "Datasets/air-pollution-emissions.csv"
    }

    # Load datasets
    dataframes = load_data(file_paths)

    # Merge datasets
    merged_data = merge_datasets(dataframes, keys=['Country', 'Year'])

    # Clean merged dataset
    cleaned_data = clean_data(merged_data)

    # Save cleaned dataset
    save_data(cleaned_data, "Datasets/MAIN_pm25-trends.csv")

if __name__ == "__main__":
    main()