import requests

def get_crypto_news(crypto_name):
    # api_key = '310fe3ac07e744b1a41832459ddc1c79'
    url = f'https://newsapi.org/v2/everything?q={crypto_name}&apiKey={api_key}'
    response = requests.get(url)
    
    if response.status_code == 200:
        news_data = response.json()
        articles = news_data.get('articles', [])
        return articles[:3]  # Get the top 3 articles
    else:
        return []
