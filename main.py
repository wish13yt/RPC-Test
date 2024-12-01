from pypresence import Presence
import time
client_id = "1312584606637101156"
RPC = Presence(client_id)
RPC.connect()
h = "Hello World!"
RPC.update(state="RPC test!")
print("Hello World!")
while True:
    time.sleep(15)