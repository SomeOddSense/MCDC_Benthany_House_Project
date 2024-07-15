*****NOTE**** ****THIS WILL BE UPDATED WEEKLY******
# MCDC_Benthany_House_Project
MCDC Project 
# Bethany House Residents Data Analysis

## Overview
This Python script analyzes and visualizes data from the Bethany House residents CSV file. It processes information about residents' stay durations, countries of origin, age distributions, and move-in/move-out patterns.

## Requirements
- Python 3.6+
- pandas
- matplotlib
- seaborn

## Installation
1. Ensure Python 3.6 or higher is installed on your system.
2. Install required libraries:

## Usage
1. Place the script in the same directory as your CSV file named 'Bethany House residents.xlsx - with length of stay.csv'.
2. Run the script:

## Features
The script performs the following analyses:

1. Calculates and corrects 'Length of Stay' for each resident.
2. Generates visualizations:
- Distribution of Length of Stay
- Top 10 Countries of Origin
- Move-ins and Move-outs over time
- Age Distribution at Move-in
- Correlation between Age and Length of Stay
3. Provides additional statistics about the residents.

## Output
The script generates:
1. Five PNG files with visualizations:
- length_of_stay_distribution.png
- top_10_countries.png
- moves_over_time.png
- age_distribution.png
- age_vs_stay_correlation.png
2. Printed statistics in the console, including:
- Total number of residents
- Average and median length of stay
- Longest and shortest stays
- Most common country of origin
- Average age at move-in

## Data Privacy
This script processes potentially sensitive resident information. Ensure you have the necessary permissions to access and analyze this data, and handle the output with appropriate care.

## Troubleshooting
- If you encounter date parsing errors, check the date formats in your CSV file.
- For any missing visualizations, ensure the script has write permissions in the directory.

## Contributing
For any improvements or bug fixes, please open an issue or submit a pull request.

## License
[Specify your license here, e.g., MIT, GPL, etc.]
