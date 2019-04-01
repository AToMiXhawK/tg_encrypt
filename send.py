from telethon import TelegramClient, sync
from telethon import TelegramClient, events
from Crypto.Cipher import AES
import base64

api_id = 861186
api_hash = '1532b2f926884763e13a689abff7708d'
key = '1234567890123456'
cipher = AES.new(key,AES.MODE_ECB)


client = TelegramClient('elekdra_send', api_id, api_hash)
client.start()

me = client.get_me()
#print(me.stringify())
user = client.get_entity('atomixhawk')
#print(user.stringify())

#client.send_message(user.username, 'Hello World from Telethon!')
while(True):
    msg = input("Enter Message: ")
    raw = msg.rjust(32)
    encoded = base64.b64encode(cipher.encrypt(raw))
    client.send_message(user.id, encoded.decode('utf-8'))