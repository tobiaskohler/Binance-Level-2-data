import websocket
import json

def on_message(ws, message):
    trade = json.loads(message)
    print(trade)

def on_error(ws, error):
    print(error)

def on_close(ws):
    print("Connection closed")

def on_open(ws):
    print("Connection opened")
    # Subscribe to trades for symbol BTCUSDT
    ws.send('{"method": "SUBSCRIBE", "params": ["adausdt@trade"], "id": 1}')

if __name__ == "__main__":
    # Connect to the Binance trade websocket
    ws = websocket.WebSocketApp("wss://stream.binance.com:9443/ws",
                                on_message = on_message,
                                on_error = on_error,
                                on_close = on_close)
    ws.on_open = on_open

    # Run the websocket client
    ws.run_forever()
