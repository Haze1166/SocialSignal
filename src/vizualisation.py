# src/visualization.py
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
from wordcloud import WordCloud


def plot_sentiment_distribution(df):
    sentiment_counts = df['sentiment_label'].value_counts()
    plt.figure(figsize=(8, 6))
    sns.barplot(x=sentiment_counts.index, y=sentiment_counts.values)
    plt.title('Overall Sentiment Distribution')
    plt.xlabel('Sentiment')
    plt.ylabel('Number of Tweets')
    plt.savefig("data/processed/sentiment_distribution.png")  # Save the plot
    plt.close() #close the plot


def plot_sentiment_over_time(df):
    df['created_at'] = pd.to_datetime(df['created_at'])
    sentiment_over_time = df.groupby([pd.Grouper(key='created_at', freq='D'), 'sentiment_label']).size().unstack(fill_value=0)
    plt.figure(figsize=(12, 6))
    sentiment_over_time.plot(kind='line')
    plt.title('Sentiment Over Time')
    plt.xlabel('Date')
    plt.ylabel('Number of Tweets')
    plt.legend(title='Sentiment')
    plt.savefig("data/processed/sentiment_over_time.png")  # Save the plot
    plt.close()

def generate_wordcloud(df, sentiment_label, filename):
    text = " ".join(df[df['sentiment_label'] == sentiment_label]['processed_text'])
    wordcloud = WordCloud(width=800, height=400, background_color='white').generate(text)
    plt.figure(figsize=(10, 5))
    plt.imshow(wordcloud, interpolation='bilinear')
    plt.axis('off')
    plt.title(f"{sentiment_label.capitalize()} Sentiment Word Cloud")
    plt.savefig(f"data/processed/{filename}")
    plt.close()