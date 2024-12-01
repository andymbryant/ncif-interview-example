import pandas as pd
from database_utils import create_tables, populate_data

# Path to the input Excel file
EXCEL_FILE_PATH = "data/20241125 Case Study for Position SE_Data.xlsx"

def process_excel_to_db(file_path):
    """
    Process the provided Excel file and populate SQLite database.
    :param file_path: Path to the input Excel file
    """
    # Load sheets from Excel file
    air_quality_data = pd.read_excel(file_path, sheet_name='AirQuality_EPA_IL')[['census_tract', 'arithmetic_mean']]
    sod_data = pd.read_excel(file_path, sheet_name='SOD_IL_2024')[['census_tract']].assign(branch_type="Bank")
    ncua_data = pd.read_excel(file_path, sheet_name='NCUA_IL_Q2_2024')[['census tract']].rename(columns={'census tract': 'census_tract'}).assign(branch_type="Credit Union")

    # Rename columns for consistency
    air_quality_data = air_quality_data.rename(columns={'arithmetic_mean': 'PM25'})

    # Merge SOD and NCUA to calculate branch count
    branches = pd.concat([sod_data, ncua_data], ignore_index=True)
    branch_density = branches.groupby('census_tract').size().reset_index(name='branch_count')

    # Merge with air quality data
    merged_data = pd.merge(air_quality_data, branch_density, on='census_tract', how='left')
    merged_data.fillna({'branch_count': 0}, inplace=True)

    # Initialize and populate database
    create_tables()
    populate_data(merged_data)
    print("Database populated successfully.")

# Example Usage
if __name__ == "__main__":
    process_excel_to_db(EXCEL_FILE_PATH)
