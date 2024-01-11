import pandas as pd
from collections import defaultdict

# List of CSV file paths
csv_files = ['climatedata0215.csv', 'climatedata1617.csv',
             'climatedata1819.csv',  'climatedata2022.csv']

# Dictionary to store monthly data
monthly_data = defaultdict(lambda: {'Temperature': [], 'Precipitation': []})

# Read data from each CSV file and update the monthly_data dictionary
for csv_file in csv_files:
    df = pd.read_csv(csv_file)
    for index, row in df.iterrows():
        month = row['Month']
        temperature = row['Temperature (°C)']
        precipitation = row['Precipitation (mm)']
        monthly_data[month]['Temperature'].append(temperature)
        monthly_data[month]['Precipitation'].append(precipitation)

# Calculate average temperature and precipitation for each month
average_data = []
for month, data in monthly_data.items():
    avg_temperature = round(
        sum(data['Temperature']) / len(data['Temperature']), 2)
    avg_precipitation = round(
        sum(data['Precipitation']) / len(data['Precipitation']), 2)
    average_data.append([month, avg_temperature, avg_precipitation])

# Create a DataFrame with the average data
result_df = pd.DataFrame(average_data, columns=[
                         'Month', 'Temperature (°C)', 'Precipitation (mm)'])

# Save the result DataFrame to a CSV file
result_df.to_csv('final_climate_data.csv', index=False)
