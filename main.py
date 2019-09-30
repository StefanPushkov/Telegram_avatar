from telethon import TelegramClient, sync
from config import *
from telethon.tl.functions.photos import UploadProfilePhotoRequest, DeletePhotosRequest
from datetime import datetime
from utils import *
import time
import socks
import urllib3
import socket
from telethon import TelegramClient, sync
api_id=937111
api_hash='0af7f3258d8a092d89f08a13031d7245'

socks.set_default_proxy(socks.SOCKS5, "localhost")
socket.socket = socks.socksocket

urllib3.proxy_from_url("https://my.telegram.org")


client = TelegramClient('first_session', api_id, api_hash, proxy=(socks.SOCKS5, 'PROXYHOST', 'PROXYUSERNAME', 'PROXYUSERNAMEPASS'))  # ИМЯ СЕССИИ можете выбрать любое, на свое усмотрение (например, «ананас»)
client.start()

prev_update_time = ""

while True:
    if time_has_changed(prev_update_time):
        prev_update_time = convert_time_to_string(datetime.now())
        client(DeletePhotosRequest(client.get_profile_photos('me')))
        file = client.upload_file(f"time_images/{prev_update_time}.jpg")
        client(UploadProfilePhotoRequest(file))

    time.sleep(1)