import asyncio
from websockets import connect
from websockets import ConnectionClosedError, InvalidStatusCode, InvalidHandshake
import aiofiles
import time
from misc import load_config
from directory_handler import check_directory_structure

import threading

date = time.strftime("%Y%m%d")

async def orderbook_download(pair, data_warehouse_path):
    config = load_config()
    websocket_timeout = config['websocket_timeout']
    
    pair_lower = pair.lower()
    wss_url = f'wss://stream.binance.com:9443/ws/{pair_lower}@depth@100ms'
    timestamp = time.strftime("%Y%m%d%H%M%S")
    
    async with connect(wss_url) as websocket:
        while True:
            try:
                data = await websocket.recv()
                
                async with aiofiles.open(f'{data_warehouse_path}/{date}/{pair}/updates/{timestamp}.txt', mode='a') as f:
                    await f.write(data + '\n')
                    
            except ConnectionClosedError:
                print('Connection closed, reconnecting...')
                await asyncio.sleep(websocket_timeout)

            except InvalidStatusCode as e:
                print(f'Invalid status code: {e}')
                await asyncio.sleep(websocket_timeout)

            except InvalidHandshake as e:
                print(f'Invalid handshake: {e}')
                await asyncio.sleep(websocket_timeout)
                
            except Exception as e:
                print(f'Unhandled exception: {e}')
                break
    

async def download_all_pairs(data_warehouse_path, symbols):
    
    tasks = []
    for pair in symbols:
        tasks.append(orderbook_download(pair, data_warehouse_path))
        
    await asyncio.gather(*tasks)
    

if __name__ == '__main__':
    
    config = load_config()
    check_directory_structure(config['data_warehouse_path'], config['symbols'])

    data_warehouse_path = config['data_warehouse_path']
    symbols = config['symbols']

    asyncio.run(download_all_pairs(data_warehouse_path, symbols))


#handling automatic disconnects, after 24 hours automatically reconnect! kil lthe old websocket and open another one
#take multiple snapshots, like every 10 minutes or so
#take snapshots manually when there is an event
