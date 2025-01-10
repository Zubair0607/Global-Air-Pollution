# Global-Air-Pollution
## Overview
This repository contains the analysis for a project that investigates the global trends and impacts of PM2.5 air pollution on health and economic outcomes. Using global datasets, the analysis explores trends in PM2.5 levels, their correlation with disease burden and GDP per capita, and regional disparities through visualisations and statistics. The results highlight the ongoing public health and economic challenges posed by air pollution, despite declining global PM2.5 levels, particularly in low- and middle-income regions.

The central hypothesis is:
> "Higher PM2.5 levels are associated with greater health burdens (e.g., disease burden and deaths) and significant economic disparities, with wealthier countries experiencing lower pollution levels."

---
## Project Structure
- **`.circleci/`**: Configuration files for CircleCI integration for testing every commit.
- **`Datasets/`**: Contains all the datasets used for analysis.
- **`Scripts/`**: Contains all the code for dataset merging, analysis, and statistics.
- **`Tests/`**: Contains all test files validated by CircleCI.
- **`Visualisations/`**: Contains all visualisations linked to the analysis.
- **`ne_110m_admin_0_countries/`**: Contains the world shapefile used for one of the visualisations.
- **`README.md/`**: Contains the project documentation
- **`requirements.txt/`**: Lists Python dependencies needed to run the scripts.

---
## The Dataset
The analysis is based on data from different sources. The primary source is **Our World In Data** which provides a comprehensive overview of different pollutants across the globe. Other sources is the **World Bank Group** and the **Institute for Health Metrics and Evaluation**.

The datasets include information on:
- Indiviual countries
- Year
- Deaths
- GPD per Capita
- Disease Burden
- Different air pollutants

---
## Cloning and Running the Repository
Follow these steps to clone and run the project:

#### 1. Clone the Repository:
```
git clone https://github.com/Zubair0607/Global-Air-Pollution.git
cd Global-Air-Pollution
```
#### 2. Install the required dependencies:
```
pip install -r requirements.txt
```
#### 3. Run the Scripts
First run `Dataset_merge.py` to process the main dataset:
```
python Global-Air-Pollution/Scripts/Dataset_merger.py
```
Then begin executing the visualisaion scripts. Example execution:
```
python Global-Air-Pollution/Scripts/Global PM2.5 Levels.py
```
#### 4. Run the Test Suite
```
pytest Tests/
```
#### 5. View the Visualisations
The visualisations should now be stored in the Visualisations folder.
