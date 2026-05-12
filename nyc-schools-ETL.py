import pandas as pd
import numpy as np
import os

class NYCSchoolsETL:
    def __init__(self):
        # Set root directory; assumed execution from the 'nyc-schools-analysis' folder
        self.root_path = "./" 
        self.data = {}

    def extract_data(self):
        """
        Extract files based on complex user-defined directory mappings
        """
        # Define precise relative paths for each data source
        file_mapping = {
            "high_school_directory": "school_directory_exploration/high-school-directory.csv",
            "school_safety_report": "incident_analysis/school-safety-report.csv",
            "sat_results": "data_population/sat-results.csv"
        }

        for name, relative_path in file_mapping.items():
            full_path = os.path.join(self.root_path, relative_path)
            
            if os.path.exists(full_path):
                # Data Ingestion
                self.data[name] = pd.read_csv(full_path)
                print(f"Successfully loaded: {name} (from {relative_path})")
            else:
                print(f"Error: File not found at {full_path}. Please verify the path.")

    def transform_data(self):
        """
        Data Cleaning and Transformation Logic (Quality Control)
        """
        if 'sat_results' in self.data:
            sat = self.data['sat_results']
            # Convert scores to numeric and calculate aggregate totals
            cols = ['SAT Math Avg. Score', 'SAT Critical Reading Avg. Score', 'SAT Writing Avg. Score']
            for c in cols:
                # Standardize numeric types and handle anomalies (QC)
                sat[c] = pd.to_numeric(sat[c], errors='coerce')
                sat[c] = sat[c].fillna(sat[c].mean())
            sat['total_SAT'] = sat[cols].sum(axis=1)
            self.data['sat_results'] = sat

        if 'high_school_directory' in self.data:
            # Standardize DBN format for downstream relational merging (Interoperability)
            self.data['high_school_directory'].rename(columns={'dbn': 'DBN'}, inplace=True, errors='ignore')

    def run_pipeline(self):
        print("--- Initiating Cross-Directory ETL Pipeline ---")
        self.extract_data()
        self.transform_data()
        print(f"Pipeline complete. {len(self.data)} datasets prepared for analysis.")
        return self.data

# --- Execution ---
pipeline = NYCSchoolsETL()
processed_data = pipeline.run_pipeline()

# --- Validation & Audit Block ---
print("\n" + "="*30)
print("ETL RESULTS AUDIT")
print("="*30)

for name, df in processed_data.items():
    print(f"\n[Dataset: {name}]")
    print(f"- Row count: {len(df)}")
    print(f"- Columns: {list(df.columns[:5])}...") # Shows first 5 columns
    
    # Specific Check for SAT Transformation
    if name == 'sat_results':
        if 'total_SAT' in df.columns:
            print(f"- QC Check: 'total_SAT' created successfully.")
            print(f"- Average Total SAT: {df['total_SAT'].mean():.2f}")
        else:
            print("- QC Check: FAILED. 'total_SAT' column missing.")

    # Specific Check for Directory Standardization
    if name == 'high_school_directory':
        if 'DBN' in df.columns:
            print("- QC Check: 'DBN' standardized to uppercase.")
        else:
            print("- QC Check: FAILED. 'DBN' column missing or lowercase.")
            
    # --- NEW CHECK AT THE BOTTOM ---
if 'sat_results' in processed_data:
    print("\n--- Visual Data Verification ---")
    # This shows the first 5 rows of specific columns
    print(processed_data['sat_results'][['DBN', 'SAT Math Avg. Score', 'total_SAT']].head())
else:
    print("Error: sat_results not found in processed data.")           
     
   
