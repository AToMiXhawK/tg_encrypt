from telethon import TelegramClient, sync
from telethon import TelegramClient, events
from Crypto.Cipher import AES
import base64
import sys

## Use your own api id and hash
api_id = 123456
api_hash = 'abcdef01234567890'
key = '1234567890123456'
cipher = AES.new(key,AES.MODE_ECB)

try:
    client = TelegramClient('send_session', api_id, api_hash)
    client.start()

    me = client.get_me()
    #print(me.stringify())
    user = client.get_entity(sys.argv[1])
    #print(user.stringify())

    #client.send_message(user.username, 'Hello World from Telethon!')
    while(True):
        msg = input()
        raw = msg.rjust(32)
        encoded = base64.b64encode(cipher.encrypt(raw))
        client.send_message(user.id, encoded.decode('utf-8'))
finally:
    client.disconnect()
