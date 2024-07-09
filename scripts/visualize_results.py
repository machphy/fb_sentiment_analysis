import matplotlib.pyplot as plt

def visualize_results(df):
    """Visualize sentiment analysis results."""
    sentiment_counts = df['sentiment_category'].value_counts()
    sentiment_counts.plot(kind='bar', color=['green', 'red', 'blue'])
    plt.title('Sentiment Analysis of Facebook Posts')
    plt.xlabel('Sentiment')
    plt.ylabel('Number of Posts')
    plt.show()

if __name__ == "__main__":
    from sentiment_analysis import perform_sentiment_analysis, preprocess_data, load_data
    
    filepath = '../data/facebook_dataset.xlsx'
    df = load_data(filepath)
    df = preprocess_data(df)
    df = perform_sentiment_analysis(df)
    visualize_results(df)
