import os
from scripts.load_data import load_data
from scripts.preprocess_data import preprocess_data
from scripts.sentiment_analysis import perform_sentiment_analysis
from scripts.visualize_results import visualize_results

def main():
    filepath = 'data/fb_scrapped_data.csv' 

    
    print("Current working directory:", os.getcwd())
    
    
    abs_filepath = os.path.abspath(filepath)
    print("Absolute file path:", abs_filepath)

    if not os.path.isfile(abs_filepath):
        raise FileNotFoundError(f"No such file or directory: '{abs_filepath}'")
    
    df = load_data(filepath)
    df = preprocess_data(df)
    df = perform_sentiment_analysis(df)
    visualize_results(df)

if __name__ == "__main__":
    main()
