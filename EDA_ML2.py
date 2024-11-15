import pandas as pd
from sklearn.preprocessing import LabelEncoder

def clean_encode_and_round_data(input_file, output_file):
    """
    Cleans, encodes categorical variables, rounds numerical columns to appropriate decimal places, 
    and saves the transformed data to a CSV file.
    
    Parameters:
    - input_file: Path to the CSV file containing the raw data.
    - output_file: Path where the cleaned, encoded, and rounded data will be saved as a CSV file.
    """
    
    # Step 1: Load data
    data = pd.read_csv(input_file)
    
    # Step 2: Basic Data Cleaning
    
    # Standardize column names (lowercase, replace spaces and hyphens with underscores)
    data.columns = data.columns.str.strip().str.lower().str.replace(" ", "_").str.replace("-", "_")

    # Handle missing values:
    # - For numeric columns: Fill with median
    # - For categorical columns: Fill with mode
    for col in data.columns:
        if data[col].dtype in ['float64', 'int64']:
            data[col].fillna(data[col].median(), inplace=True)
        else:
            data[col].fillna(data[col].mode()[0], inplace=True)

    # Remove duplicate rows
    data = data.drop_duplicates()

    # Step 3: Encode Categorical Variables

    # Binary categorical columns - Label Encode as 0/1
    binary_columns = ['gender', 'fam_hist_o', 'favc', 'smoke', 'scc']
    for col in binary_columns:
        if col in data.columns:
            data[col] = LabelEncoder().fit_transform(data[col])

    # Multi-category columns - Label Encode with unique integer for each category
    multi_category_columns = ['mtrans', 'obesity_level', 'caec', 'calc']
    for col in multi_category_columns:
        if col in data.columns:
            data[col] = LabelEncoder().fit_transform(data[col])

    # Step 4: Feature Engineering - BMI calculation (if weight and height are present)
    if 'weight' in data.columns and 'height' in data.columns:
        data['bmi'] = data['weight'] / (data['height'] ** 2)

    # Remove irrelevant columns (e.g., 'patient_id' or any other ID columns if they exist)
    if 'patient_id' in data.columns:
        data = data.drop(columns=['patient_id'])

    # Step 5: Rounding and Converting to Integers for Specific Columns

    # Round 'age' to the nearest integer
    if 'age' in data.columns:
        data['age'] = data['age'].round(0).astype(int)

    # Columns that represent counts, so we convert them to integers
    count_columns = ['fcvc', 'ncp', 'faf', 'tue']
    for col in count_columns:
        if col in data.columns:
            data[col] = data[col].round(0).astype(int)
    
    # Round 'ch2o' to 1 decimal place if it represents continuous data (e.g., water intake)
    if 'ch2o' in data.columns:
        data['ch2o'] = data['ch2o'].round(1)

    # Round 'height', 'weight', and 'bmi' to 2 decimal places if they exist
    decimal_columns = ['height', 'weight', 'bmi']
    for col in decimal_columns:
        if col in data.columns:
            data[col] = data[col].round(2)

    # Step 6: Save the Cleaned, Encoded, and Rounded Data
    data.to_csv(output_file, index=False)
    
    print(f"Data cleaning, encoding, and rounding completed. Saved to {output_file}")

# Usage example:
input_file = "MS_2_Scenario_data.csv"  # Path to the raw data file
output_file = "Cleaned_Encoded_Rounded_MS_2_Scenario_data.csv"  # Path where processed data will be saved
clean_encode_and_round_data(input_file, output_file)
