from aiohttp import ClientSession
import configs

headers = {
    "key": configs.trakteer_api_key,
    "Accept": "application/json",
    "X-Requested-With": "XMLHttpRequest",
}
base_url = "https://api.trakteer.id/v1/public"


async def get_balance():
    async with ClientSession(headers=headers) as s, s.get(
        f"{base_url}/current-balance"
    ) as r:
        data = await r.json()
        balance = data["result"]
        return int(balance)
