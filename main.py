import uvicorn
from fastapi import FastAPI
from routes import webhook
import configs
from core.bot import dp, bot

app = FastAPI()
app.include_router(webhook.router)


@app.get("/")
async def index():
    return {"status": "ok"}


@app.on_event("startup")
async def startup():
    webhook_info = await bot.get_webhook_info()
    if webhook_info.url != configs.webhook_url:
        await bot.delete_webhook()
        await bot.set_webhook(configs.webhook_url)
    print("Bot started")
    me = await bot.get_me()
    print(f"Bot username: {me.username}")


if __name__ == "__main__":
    uvicorn.run("main:app", host=configs.host, port=configs.port, reload=True)
