'''
This script is used to download trade updates from Binance via websockets.

The script is designed to be run as a background process, and will download trade updates for all symbols in the config file.

IMPORTANT:
To account for automatic disconnects from binance websockets (automatically after 24hours of streaming), schedule this script via CRON job to run for (24*60*60)-30 seconds = 86370 seconds. This will ensure that the script is restarted before the 24 hour limit is reached.

Use shell script to run this script in the background:
'''



import asyncio
from websockets import connect
from websockets import ConnectionClosedError, InvalidStatusCode, InvalidHandshake
import aiofiles
import time
from misc import load_config
from directory_handler import check_directory_structure

date = time.strftime("%Y%m%d")

async def orderbook_download(pair, data_warehouse_path):
    
    config = load_config()
    websocket_timeout = config['websocket_timeout']
    pair_lower = pair.lower()
    trade_url = f'wss://stream.binance.com:9443/ws/{pair_lower}@trade'
    timestamp = time.strftime("%Y%m%d%H%M%S")
    
    print(f'Listening to {trade_url} ...')
    
    
    async with connect(trade_url) as trade_websocket:
        while True:
            try:
                trade_data = await trade_websocket.recv()
                
                async with aiofiles.open(f'{data_warehouse_path}/{date}/{pair}/trades/{timestamp}.txt', mode='a') as f:
                    await f.write(trade_data + '\n')
                    
            except ConnectionClosedError as e:
                print('Connection closed, reconnecting...')
                print(e)
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