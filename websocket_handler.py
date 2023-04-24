import asyncio
from websockets import connect
import aiofiles
import time
from misc import load_config


date = time.strftime("%Y%m%d")

async def orderbook_download(pair, data_warehouse_path):
    
    pair_lower = pair.lower()
    wss_url = f'wss://stream.binance.com:9443/ws/{pair_lower}@depth@100ms'
    timestamp = time.strftime("%Y%m%d%H%M%S")
    
    async with connect(wss_url) as websocket:
        while True:
            data = await websocket.recv()
            
            async with aiofiles.open(f'{data_warehouse_path}/{date}/{pair}/updates/{timestamp}', mode='a') as f:
                await f.write(data + '\n')
    




if __name__ == '__main__':
    
    config = load_config()
    data_warehouse_path  = config['data_warehouse_path']
    
    for pair in config['symbols']:
        asyncio.run(orderbook_download(pair, data_warehouse_path))



#handling automatic disconnects, after 24 hours automatically reconnect! kil lthe old websocket and open another one
#take multiple snapshots, like every 10 minutes or so
#take snapshots manually when there is an event
