
from telethon import TelegramClient, sync
from telethon import TelegramClient, events
from Crypto.Cipher import AES
import base64
from time import sleep
import sys

from pyfiglet import Figlet
f = Figlet(font='slant')
print(f.renderText('TG-Encrypter'))

## Use your own api id and hash
api_id = 123456
api_hash = 'abcdef01234567890'
key = '1234567890123456'
cipher = AES.new(key, AES.MODE_ECB)

try:
    client = TelegramClient('rec_session', api_id, api_hash)
    client.start()


    me = client.get_me()
    user = client.get_entity(sys.argv[1])


    def receive():
        @client.on(events.NewMessage)
        async def my_event_handler(event):
            if(event.original_update.user_id == user.id):
                raw = event.raw_text
                decoded = cipher.decrypt(base64.b64decode(raw))
                msg = decoded.decode('utf-8').lstrip()
                if(event.message.out == False):
                    print(user.username+"<< "+msg)
                else:
                    print(me.username+">> "+msg)
                #if msg == "{quit}":
                #    print(user.username +" left the conversation, Exiting!! ")
                #    client.disconnect()
                #    quit()

        client.start()
        client.run_until_disconnected()


    receive()

finally:
    client.disconnect()
