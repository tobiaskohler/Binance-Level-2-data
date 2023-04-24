



rest_url = f'https://api.binance.com/api/v3/depth'
    
rest_params = {
    "symbol": pair.upper(),
    "limit": 5000,
}

    
async with httpx.AsyncClient() as client:
    snapshot = await client.get(rest_url, params=rest_params)

snapshot = snapshot.ujson()
snapshot['time'] = time.time()


async with aiofiles.open(f'{pair_lower}_updates_{timestamp}.txt', mode='w') as f:
    await f.write(snapshot.text + '\n')

