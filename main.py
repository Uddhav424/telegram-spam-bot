
from telethon.sync import TelegramClient
import time
import os

api_id = int(os.environ['API_ID'])
api_hash = os.environ['API_HASH']
session = os.environ['SESSION_NAME']
target = os.environ['TARGET_USERNAME']
message = os.environ['SPAM_MESSAGE']
count = int(os.environ['SPAM_COUNT'])

client = TelegramClient(session, api_id, api_hash)

with client:
    for i in range(count):
        client.send_message(target, message)
        print(f"✅ Sent message #{i+1}")
        time.sleep(2)
