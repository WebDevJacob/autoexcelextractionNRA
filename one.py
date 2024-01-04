import xml.etree.ElementTree as ET
import csv


def extract_rows_with_value(xml_files, output_csv, columns, filter_column, filter_value, xml_field):
    with open(output_csv, 'w', newline='', encoding='utf-8') as csvfile:
        csv_writer = csv.writer(csvfile)

        # Write header with column names
        csv_writer.writerow(columns)

        # Process each XML file
        for xml_file in xml_files:
            tree = ET.parse(xml_file)
            root = tree.getroot()

            # Extract data for specified columns and apply filter
            for item in root.findall(f'.//{xml_field}'):
                row = [item.find(column).text if item.find(
                    column) is not None else '' for column in columns]

                # Check if the filter column is present in the item
                filter_element = item.find(filter_column)
                if filter_element is not None and filter_element.text == filter_value:
                    row = [item.find(column).text if item.find(
                        column) is not None else '' for column in columns]
                    csv_writer.writerow(row)


# 2002 - 2015
# selected_columns = ['COD_EST', 'FECHA', 'T_MED', 'LLUVIA']
# xml_field = "Diario"

# filter for location
# filter_column = 'COD_EST'
# filter_value = 'AL008' # id of weather station location

# output_csv_path = 'dataforspecifiedlocation0215.csv'


# 2016 - 2017
# selected_columns = ['cod_est', 'FECHA', 'T_Med', 'Lluvia']
# xml_field = "Diario_OpenData"

# # filter for location
# filter_column = 'cod_est'
# filter_value = 'AL008'  # id of weather station location

# output_csv_path = 'dataforspecifiedlocation1617.csv'


# 2018 - 2019
# selected_columns = ['cod_est', 'FECHA', 'T_Med', 'SumaDeLluvia']
# xml_field = "Cns_OpenData"

# # filter for location
# filter_column = 'cod_est'
# filter_value = 'AL008'  # id of weather station location

# output_csv_path = 'dataforspecifiedlocation1819.csv'


# 2020 - 2022 (or 2023)
selected_columns = ['cod_est', 'FECHA', 'T_Med', 'Lluvia_acum']
xml_field = "Cns_OpenData"

# filter for location
filter_column = 'cod_est'
filter_value = 'AL008'  # id of weather station location

output_csv_path = 'dataforspecifiedlocation2022.csv'

start_year = 2020
end_year = 2022

xml_files_list = []
for i in range(start_year, end_year + 1):
    xml_files_list.append(f"Clim_Diario_{i}.xml")


extract_rows_with_value(xml_files_list, output_csv_path,
                        selected_columns, filter_column, filter_value, xml_field)
