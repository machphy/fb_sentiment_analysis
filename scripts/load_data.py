import pandas as pd
import os

def load_data(filepath):
    """Load dataset from a CSV file."""
    abs_filepath = os.path.abspath(filepath)
    if not os.path.isfile(abs_filepath):
        raise FileNotFoundError(f"No such file or directory: '{abs_filepath}'")
    return pd.read_csv(abs_filepath)

if __name__ == "__main__":
    filepath = '../../data/fb_scrapped_data.csv'  

    
    abs_filepath = os.path.abspath(filepath)
    print("Absolute file path:", abs_filepath)

  
    if os.path.isfile(abs_filepath):
        df = load_data(filepath)
        print(df.head())
    else:
        print(f"File not found: {abs_filepath}")
