def preprocess_data(df):
    """Preprocess the data."""
    
    df.dropna(subset=['post_text'], inplace=True)  
    return df

if __name__ == "__main__":
    from load_data import load_data
    
    filepath = '../data/facebook_dataset.xlsx'
    df = load_data(filepath)
    df = preprocess_data(df)
    print(df.head())
