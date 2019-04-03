from telethon import TelegramClient, sync
from telethon import TelegramClient, events
from Crypto.Cipher import AES
import base64

## Use your own api id and hash
api_id = 123456
api_hash = 'abcdef01234567890'
key = '1234567890123456'
cipher = AES.new(key, AES.MODE_ECB)


client = TelegramClient('send_session', api_id, api_hash)
client.start()
