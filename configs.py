from dotenv import load_dotenv
import os


load_dotenv()
bot_token = os.getenv("BOT_TOKEN")
trakteer_api_key = os.getenv("TRAKTEER_API_KEY")
webhook_url = os.getenv("WEBHOOK_URL")
webhook_url = f"{webhook_url}/telegram"
host = os.getenv("HOST", "0.0.0.0")
if port := os.getenv("PORT", 8000):
    port = int(port)
if channel_id := os.getenv("CHANNEL_ID"):
    channel_id = int(channel_id)
