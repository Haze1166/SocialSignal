# src/main.py
from data_collection import get_tweets, tweets_to_dataframe
from preprocessing import preprocess_tweet
from sentiment_analysis import get_sentiment
from visualization import plot_sentiment_distribution, plot_sentiment_over_time, generate_wordcloud
import pandas as pd
from config import TOPIC # Import the topic



if __name__ == "__main__":

    tweets = get_tweets(TOPIC, count=500)

    if tweets:
      df = tweets_to_dataframe(tweets)
      df['processed_text'] = df['text'].apply(preprocess_tweet)
      df['sentiment'] = df['processed_text'].apply(get_sentiment)
      df['sentiment_label'] = df['sentiment'].apply(lambda x: x['label'])
      df['sentiment_score'] = df['sentiment'].apply(lambda x: x['score'])

      # Generate visualizations and save them
      plot_sentiment_distribution(df)
      plot_sentiment_over_time(df)
      generate_wordcloud(df, 'positive', 'positive_wordcloud.png')
      generate_wordcloud(df, 'negative', 'negative_wordcloud.png')

      print("Analysis complete. Visualizations saved in data/processed/")

    else:
      print("No Tweets Found")