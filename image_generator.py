from PIL import Image, ImageDraw, ImageFont

def generate_crypto_image(crypto_name, price, market_cap, volume_24h, circulating_supply, sentiment):
    # Create an image canvas
    width, height = 500, 300
    image = Image.new("RGB", (width, height), color=(0, 0, 0))  # Black background
    
    # Initialize drawing context
    draw = ImageDraw.Draw(image)
    
    # Load font (ensure the font file path is correct or use a system-default font)
    try:
        font = ImageFont.truetype("arial.ttf", size=20)
    except:
        font = ImageFont.load_default()  # Fallback to default font
    
    # Add text
    title = f"Crypto: {crypto_name.capitalize()}"
    price_text = f"Price: ${price}"
    market_cap_text = f"Market Cap: ${market_cap}"
    volume_24h_text = f"24h Volume: ${volume_24h}"
    circulating_supply_text = f"Supply: {circulating_supply}"
    sentiment_text = f"Sentiment: {sentiment}"

    # Position of the text on the image
    text_y = 20
    draw.text((20, text_y), title, fill="yellow", font=font)
    text_y += 30
    draw.text((20, text_y), price_text, fill="yellow", font=font)
    text_y += 30
    draw.text((20, text_y), market_cap_text, fill="yellow", font=font)
    text_y += 30
    draw.text((20, text_y), volume_24h_text, fill="yellow", font=font)
    text_y += 30
    draw.text((20, text_y), circulating_supply_text, fill="yellow", font=font)
    text_y += 30
    draw.text((20, text_y), sentiment_text, fill="yellow", font=font)  # Display sentiment
    
    # Save the image
    image_path = f"{crypto_name}_price_sentiment.png"
    image.save(image_path)
    return image_path
