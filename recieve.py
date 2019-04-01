from telethon import TelegramClient, sync
from telethon import TelegramClient, events
from Crypto.Cipher import AES
import base64

api_id = 861186
api_hash = '1532b2f926884763e13a689abff7708d'
key = '1234567890123456'
cipher = AES.new(key,AES.MODE_ECB)


client = TelegramClient('elekdra', api_id, api_hash)
client.start()

me = client.get_me()
#print(me.stringify())
user = client.get_entity('atomixhawk')
#print(user.stringify())

#client.send_message(user.username, 'Hello World from Telethon!')

@client.on(events.NewMessage)
async def my_event_handler(event):
   #print(event.stringify())
    if(event.message.from_id == user.id):
        raw = event.raw_text
        decoded = cipher.decrypt(base64.b64decode(raw))
        print(decoded.decode('utf-8'))
    #if 'hello' in event.raw_text:
    #    await event.reply('hi!')


client.start()
client.run_until_disconnected()