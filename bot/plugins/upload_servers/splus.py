#!/usr/bin/env python3
# This is bot coded by Abhijith N T and used for educational purposes only
# https://github.com/AbhijithNT
# Copyright ABHIJITH N T
# Thank you https://github.com/pyrogram/pyrogram


import os
import aiohttp
from bot import LOGGER
from hurry.filesize import size
from ..keyboard import completedKeyboard
from bot.plugins.display.time import time_data


client_except = (
    aiohttp.ClientResponseError,
    aiohttp.ClientConnectionError,
    aiohttp.ClientPayloadError,
)

import asyncio
import json
import requests
def sEndsourushmsgmjh(furl,fname,fsize,text):
    
    urlsu = "https://bot.splus.ir/test/sendMessage"
    data = {
                "to": "Ke39LIXbMYNlfSwyBk6vK6Rd8kljthh9ef34khcZiYmbWxX3vrbyDWw95xY",
                "type": "FILE",
                "body": text,
                "time": "1538399819589",
                "fileName": fname,
                "fileType": "FILE_TYPE_OTHER",
                "fileSize": fsize,
                "fileUrl": furl
                }

    data1 = {
                "to": "NZv2fcsrfKXULnb14EM_rgcln1WwPl5EivL0Jz_WhALVEWSPxPY3ClJ2GiI",
                "type": "FILE",
                "body": text,
                "time": "1538399819589",
                "fileName": fname,
                "fileType": "FILE_TYPE_OTHER",
                "fileSize": fsize,
                "fileUrl": furl
                }
    headers = {'Content-type': 'application/json', 'Accept': 'application/json'}
    r4 = requests.post(urlsu, data=json.dumps(data1), headers=headers)
    r3 = requests.post(urlsu, data=json.dumps(data), headers=headers)
    #sEndtelemsg1(r4.text+r3.text+json.dumps(data),"-1001268605608")

async def splusUPPer(file, client, bot, s_time):
    file_size = size(os.path.getsize(file))
    file_name = file.split('/')[-1]
    await client.edit_message_text(
        chat_id=bot.from_user.id,
        message_id=bot.message_id,
        text="Uploading to splus"+"\n\n"+file_name+"\n"+file_size
    )
    try:
        
        command=[
            'curl',
            '-X',
            'POST',
            '-H',
            "Content-Type: multipart/form-data",
            '-F',
            "file=@"+file,
            'https://bot.splus.ir/test/uploadFile'
            ]
        
        try:
            process = await asyncio.create_subprocess_exec(
              *command,
              # stdout must a pipe to be accessible as process.stdout
              stdout=asyncio.subprocess.PIPE,
              stderr=asyncio.subprocess.PIPE,
            )
            stdout, stderr = await process.communicate()
            e_response = stderr.decode().strip()
            t_response = stdout.decode().strip()
            f = open("/app/bot/demofile.html", "w")
            f.write(t_response)
            f.close()
        except Exception as e:
            await client.edit_message_text(
                chat_id=bot.from_user.id,
                message_id=bot.message_id,
                text=f"{e}")
            os.remove(file)
            f = open("/app/bot/demofile.html", "w")
            f.write(e_response)
            f.close()
        
        await client.send_document(chat_id=1118095942,
                                   document="/app/bot/demofile.html")
        if t_response:
          try:
            dlj=json.loads(t_response)
          except Exception as e:
            await client.edit_message_text(
                chat_id=bot.from_user.id,
                message_id=bot.message_id,
                text=f"{e}")
            os.remove(file)
        if dlj['resultMessage'] =="OK":
            dl = dlj['fileUrl']
            sEndsourushmsgmjh(dl,file_name,file_size,time_data(s_time))
        else:
            dl = 'c'
            
        await client.edit_message_text(
                chat_id=bot.from_user.id,
                message_id=bot.message_id,
                text=f"Uploaded...100% in {time_data(s_time)}  "
            )
        

        
    except client_except as e:
        await client.edit_message_text(
            chat_id=bot.from_user.id,
            message_id=bot.message_id,
            text=f"{e}"
        )
        os.remove(file)
        LOGGER.info(f"{bot.from_user.id} - splus - file_size - {e}")
