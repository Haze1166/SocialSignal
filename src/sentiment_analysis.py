# src/sentiment_analysis.py
from transformers import pipeline

sentiment_pipeline = pipeline("sentiment-analysis")

def get_sentiment(text):
    result = sentiment_pipeline(text)[0]
    if result['label'] == 'POSITIVE':
        return {'label': 'positive', 'score': result['score']}
    elif result['label'] == 'NEGATIVE':
        return {'label': 'negative', 'score': result['score']}
    else:
        return {'label': 'neutral', 'score': result['score']} # Added a return for the else statement