# Facebook Sentiment Analysis

This project performs sentiment analysis on Facebook posts using Python. The analysis pipeline involves loading data from a CSV file, preprocessing the data, performing sentiment analysis, and visualizing the results.

## Project Structure

fbsa/
│
├── data/
│ └── fb_scrapped_data.csv # Your CSV dataset file
│
├── scripts/
│ ├── load_data.py # Loads the dataset from CSV
│ ├── preprocess_data.py # Preprocesses the dataset
│ ├── sentiment_analysis.py # Performs sentiment analysis
│ └── visualize_results.py # Visualizes the results
│
├── main.py # Main script to run the analysis pipeline
└── README.md # Project README file

## Project Details

This project is designed to analyze the sentiment of Facebook posts. Sentiment analysis is a natural language processing (NLP) technique used to determine the emotional tone behind a body of text. It is commonly used to understand opinions, attitudes, and emotions expressed in online reviews, social media, and other forms of text.

### Key Features

- **Data Loading**: Loads Facebook post data from a CSV file.
- **Data Preprocessing**: Cleans and preprocesses the data to make it suitable for analysis.
- **Sentiment Analysis**: Analyzes the sentiment of each Facebook post using a sentiment analysis model.
- **Visualization**: Visualizes the distribution of sentiment scores using a histogram.

### Technologies Used

- **Python**: The programming language used for the entire project.
- **Pandas**: A data manipulation and analysis library used to handle the dataset.
- **Matplotlib**: A plotting library used to visualize the results.

Scripts Overview
main.py
The main entry point of the project. It orchestrates data loading, preprocessing, sentiment analysis, and result visualization.

load_data.py
Defines a function to load the dataset from a CSV file.

preprocess_data.py
Defines functions for preprocessing the dataset.

sentiment_analysis.py
Defines functions for performing sentiment analysis.

visualize_results.py
Defines functions for visualizing the results.


### result 

1. **Resulting Graph Image**

   Sentiment analysis sample:

<img src="https://github.com/machphy/fb_sentiment_analysis/blob/main/IMG/Screenshot%202024-07-09%20095042.png?raw=true" width="400" height="300">


