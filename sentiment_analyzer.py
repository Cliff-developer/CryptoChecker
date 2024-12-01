from textblob import TextBlob

def analyze_sentiment(news_articles):
    sentiment_score = 0
    for article in news_articles:
        text = article['title'] + " " + article['description'] if article['description'] else article['title']
        
        blob = TextBlob(text)
        
        sentiment_score += blob.sentiment.polarity
    
    # Calculate average sentiment score
    average_sentiment = sentiment_score / len(news_articles) if news_articles else 0

    # Determine the sentiment classification
    if average_sentiment > 0:
        return "Positive"
    elif average_sentiment < 0:
        return "Negative"
    else:
        return "Neutral"
