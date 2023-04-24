from misc import load_config
from directory_handler import check_directory_structure
from websocket_handler import download_all_pairs
import asyncio



config = load_config()

data_warehouse_path = config['data_warehouse_path']
symbols = config['symbols']

check_directory_structure(config['data_warehouse_path'], config['symbols'])

asyncio.run(download_all_pairs(data_warehouse_path, symbols))



# for pair in config['symbols']:
#     orderbook_download(pair, config['data_warehouse_path'])