from fastapi import APIRouter, Request
from aiogram import types

import configs
from core.bot import dp, bot


router = APIRouter()


@router.post("/trakteer")
async def trakteer_webhook(request: Request):
    data = await request.json()
    text = f"""Donasi Baru!
Donatur: {data["supporter_name"]}
Pesan: {data["supporter_message"]}
Jumlah: {data["quantity"]} {data["unit"]} (Rp {data["price"]})

Terima kasih atas donasinya yaa!
"""
    await bot.send_message(configs.channel_id, text)
    return {"status": "ok"}


@router.post("/telegram")
async def telegram_webhook(request: Request):
    data = await request.json()
    tele_update = types.Update(**data)
    await dp.feed_webhook_update(bot, tele_update)
    return {"status": "ok"}
