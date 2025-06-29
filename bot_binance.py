from binance.client import Client

api_key = '2DaQYHI1r9VOe1kmTcdVk7v7sgGEkgbeYq2o3zKzuW78NZMFECKWOEZUgaqY9onW'
api_secret = 'jCupZTGwz3dK1kJBK0xldtHn5ooIvLea7wur7jN6Kb7VSMDuZtMjjiR2I48FFrR9'

client = Client(api_key, api_secret)

# Consultar el precio actual de BTC/USDT
precio = client.get_symbol_ticker(symbol="BTCUSDT")
print("Precio actual de BTC:", precio['price'])
