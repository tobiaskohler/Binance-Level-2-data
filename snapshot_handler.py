'''
This script is used to take snapshots of the orderbook from Binance.

It is designed to be run as a background process (CRON job), and will take snapshots of the orderbook for all symbols in the config file.

IMPORTANT:
Schedule this script via CRON job to run every n-seconds, where n is your desired interval in seconds.

This allows for taking single snapshots of the orderbook before special events or at arbitrary times.
'''


import asyncio
import aiofiles
import time
import httpx
from misc import load_config
from directory_handler import check_directory_structure

date = time.strftime("%Y%m%d")

async def get_snapshot(pair, data_warehouse_path, orderbook_depth):
    
    rest_url = f'https://api.binance.com/api/v3/depth'
    
    rest_params = {
        "symbol": pair.upper(),
        "limit": orderbook_depth,
    }
    
    timestamp = time.strftime("%Y%m%d%H%M%S")

    async with httpx.AsyncClient() as client:
        snapshot = await client.get(rest_url, params=rest_params)

    async with aiofiles.open(f'{data_warehouse_path}/{date}/{pair}/orderbook_snapshots/{timestamp}.txt', mode='w') as f:
        await f.write(snapshot.text + '\n')
        
    print(f'Took snapshot of {pair} at {timestamp}')


if __name__ == '__main__':
        
        config = load_config()
        #check_directory_structure(config['data_warehouse_path'], config['symbols'])
    
        data_warehouse_path = config['data_warehouse_path']
        symbols = config['symbols']
        orderbook_depth = config['orderbook_depth']
        snapshot_interval = config['snapshot_interval']
    
        for pair in symbols:
            asyncio.run(get_snapshot(pair, data_warehouse_path, orderbook_depth))
