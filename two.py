import csv
from collections import defaultdict
from datetime import datetime
import pandas as pd


def process_csv(input_csv, output_csv, temp_field, precip_field):
    # Dictionary to store monthly aggregated values
    monthly_data = defaultdict(lambda: {temp_field: [], precip_field: []})

    with open(input_csv, 'r') as csv_file:
        csv_reader = csv.DictReader(csv_file)
        for row in csv_reader:
            fecha = row['FECHA']
            fecha_datetime = datetime.strptime(fecha, "%Y-%m-%dT%H:%M:%S")
            # Get the full month name in English
            month_key = fecha_datetime.strftime("%B")

            # Append temperature and precipitation data
            monthly_data[month_key][temp_field].append(float(row[temp_field]))
            monthly_data[month_key][precip_field].append(
                float(row[precip_field] or 0.0))

    # Order months chronologically
    months_in_order = ['January', 'February', 'March', 'April', 'May', 'June',
                       'July', 'August', 'September', 'October', 'November', 'December']

    # Calculate averages and totals for each month
    monthly_aggregates = {}
    for month in months_in_order:
        data = monthly_data[month]
        temperature_avg = sum(data[temp_field]) / \
            len(data[temp_field]) if data[temp_field] else 0.0

        precipitation_total = sum(
            data[precip_field]) / number_of_years if data[precip_field] else 0.0

        monthly_aggregates[month] = {
            temp_field: round(temperature_avg, 1), precip_field: round(precipitation_total, 1)}

    # Convert the aggregated data to a DataFrame
    df = pd.DataFrame(monthly_aggregates).transpose()

    # Rename columns for the desired output
    df.columns = ['Temperature (°C)', 'Precipitation (mm)']

    # Write to CSV file
    df.to_csv(output_csv, index_label='Month')


# TODO: Ändern je nach Jahr
input_csv_path = 'dataforspecifiedlocation2022.csv'
output_csv_path = 'climatedata2022.csv'
number_of_years = 3
temp_field = "T_Med"
precip_field = "Lluvia_acum"

process_csv(input_csv_path, output_csv_path, temp_field, precip_field)
