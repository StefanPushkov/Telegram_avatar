from telethon import TelegramClient, sync

# Вставляем api_id и api_hash
api_id=937111
api_hash='0af7f3258d8a092d89f08a13031d7245'

client = TelegramClient('session_name', api_id, api_hash)
client.start()

