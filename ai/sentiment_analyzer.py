from textblob import TextBlob

def analyze_sentiment(text):

    sentiment = TextBlob(text).sentiment.polarity

    if sentiment > 0.2:
        return "Bullish"
    elif sentiment < -0.2:
        return "Bearish"
    else:
        return "Neutral"
