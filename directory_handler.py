import yaml
import os
import time
from misc import load_config



date = time.strftime("%Y%m%d")


def check_directory_structure(data_warehouse_path, symbols):
    
    for symbol in symbols:
        
        if not os.path.exists(f'{data_warehouse_path}/{date}'):
            os.makedirs(f'{data_warehouse_path}/{date}')

        if not os.path.exists(f'{data_warehouse_path}/{date}/{symbol}'):
            os.makedirs(f'{data_warehouse_path}/{date}/{symbol}')
            
        if not os.path.exists(f'{data_warehouse_path}/{date}/{symbol}/snapshots'):
            os.makedirs(f'{data_warehouse_path}/{date}/{symbol}/snapshots')
            
        if not os.path.exists(f'{data_warehouse_path}/{date}/{symbol}/updates'):
            os.makedirs(f'{data_warehouse_path}/{date}/{symbol}/updates')
            
        print(f'Directory structure for {symbol} at {data_warehouse_path}{date}/{symbol}/snapshots and {data_warehouse_path}{date}/{symbol}/updates')


if __name__ == '__main__':
    
    config = load_config()
    
    check_directory_structure(config['data_warehouse_path'], config['symbols'])