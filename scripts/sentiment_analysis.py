from textblob import TextBlob

def get_sentiment(text):
    """Get sentiment polarity from text."""
    blob = TextBlob(text)
    return blob.sentiment.polarity

def classify_sentiment(polarity):
    """Classify the sentiment polarity."""
    if polarity > 0:
        return 'Positive'
    elif polarity < 0:
        return 'Negative'
    else:
        return 'Neutral'

def perform_sentiment_analysis(df):
    """Perform sentiment analysis on the dataframe."""
    df['sentiment'] = df['post_text'].apply(get_sentiment)
    df['sentiment_category'] = df['sentiment'].apply(classify_sentiment)
    return df

if __name__ == "__main__":
    from preprocess_data import preprocess_data, load_data
    
    filepath = '../data/facebook_dataset.xlsx'
    df = load_data(filepath)
    df = preprocess_data(df)
    df = perform_sentiment_analysis(df)
    print(df.head())
