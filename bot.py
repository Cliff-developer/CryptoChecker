import requests
from textblob import TextBlob
from telegram import Update
from telegram.ext import Application, CommandHandler, CallbackContext
from config import TELEGRAM_BOT_TOKEN
from image_generator import generate_crypto_image  # Import the image generator

# Function to fetch crypto price and additional data
def get_crypto_data(crypto_name):
    url = f"https://api.coingecko.com/api/v3/coins/{crypto_name}"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        price = data['market_data']['current_price']['usd']
        market_cap = data['market_data']['market_cap']['usd']
        volume_24h = data['market_data']['total_volume']['usd']
        circulating_supply = data['market_data']['circulating_supply']
        
        # Placeholder for sentiment analysis: analyze a news or social media source here
        sentiment = analyze_sentiment(f"Current news for {crypto_name}: The market is bullish for {crypto_name}.")  # Example placeholder sentence

        return price, market_cap, volume_24h, circulating_supply, sentiment
    return None, None, None, None, None

# Function to perform sentiment analysis using TextBlob
def analyze_sentiment(text):
    blob = TextBlob(text)
    sentiment_score = blob.sentiment.polarity  # Sentiment score: ranges from -1 (negative) to 1 (positive)
    if sentiment_score > 0:
        sentiment = "Positive"
    elif sentiment_score < 0:
        sentiment = "Negative"
    else:
        sentiment = "Neutral"
    return sentiment

# Command handler for the /crypto command
async def crypto(update: Update, context: CallbackContext):
    if len(context.args) > 0:
        crypto_name = context.args[0].lower()
        
        # Get data from the API
        price, market_cap, volume_24h, circulating_supply, sentiment = get_crypto_data(crypto_name)
        
        if price is None:
            await update.message.reply_text("Invalid cryptocurrency name. Please try again.")
        else:
            # Generate image with the crypto data
            image_path = generate_crypto_image(crypto_name, price, market_cap, volume_24h, circulating_supply, sentiment)
            
            # Send the image
            with open(image_path, "rb") as img:
                await update.message.reply_photo(photo=img)
    else:
        await update.message.reply_text("Please provide a cryptocurrency name (e.g., /crypto bitcoin)")

# Main function to start the bot
def main():
    # Create the bot application
    application = Application.builder().token(TELEGRAM_BOT_TOKEN).build()

    # Add command handler
    application.add_handler(CommandHandler("crypto", crypto))

    # Run the bot
    application.run_polling()

# Entry point
if __name__ == "__main__":
    main()
