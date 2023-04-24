from snapshot_handler import get_snapshots_manually
import asyncio
from misc import load_config
from directory_handler import check_directory_structure

    
config = load_config()
data_warehouse_path = config['data_warehouse_path']
symbols = config['symbols']
orderbook_depth = config['orderbook_depth']
check_directory_structure(config['data_warehouse_path'], config['symbols'])

asyncio.run(get_snapshots_manually(data_warehouse_path, symbols, orderbook_depth))