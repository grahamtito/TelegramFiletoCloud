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
   
async def aparatUPPer(file, client, bot, s_time):
    file_size = size(os.path.getsize(file))
    file_name = file.split('/')[-1]
    await client.edit_message_text(
        chat_id=bot.from_user.id,
        message_id=bot.message_id,
        text="Uploading to yor aparat"+"\n\n"+file_name+"\n"+file_size
    )
    try:
        r1 = requests.get('https://www.aparat.com/etc/api/uploadform/luser/drassat/ltoken/b067158e925e3d66f6753dab558db550')
        y = json.loads(r1.text)
        stat='=========load json:'+r1.text+'======================='
        furl=y['uploadform']['frm-id']
        faction=y['uploadform']['formAction']
        #datas={"frm-id":furl,"data[title]":'غلوش1',"data[category]":'17',"data[tags]":'uitggf-ggggg-ggggggv',"data[descr]":'hhh hhjj fj',"data[video_pass]":'false'}
        fields = {"frm-id":str(furl),"data[title]":"mmmmioijjj",
            "data[category]":str(17),
            "data[tags]":"uitggf-ggggg-ggggggv",
            "data[descr]":"hhh hhjj fj",
            "data[video_pass]":"false",
            "video": "@"+file
            }
        command=['curl',faction]
        for field in fields:
            command.append('-F')
            command.append(field+'='+fields[field])
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
            f.write(t_response.text)
            f.close()
        except Exception as e:
            await client.edit_message_text(
                chat_id=bot.from_user.id,
                message_id=bot.message_id,
                text=f"{e}"+e_response)
            os.remove(file)
            f = open("/app/bot/demofile.html", "w")
            f.write(e_response.text)
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
        if dlj['uploadpost']['type'] =="success":
            dl = dlj['uploadpost']['uid']
        else:
            dl = dlj['uploadpost']['text']
            
        await client.edit_message_text(
                chat_id=bot.from_user.id,
                message_id=bot.message_id,
                text=f"Uploaded...100% in {time_data(s_time)} \n\n https://www.aparat.com/v/{dl} \n\n\n\t {file} {os.path.basename(file)} , {what_the_mime(os.path.splitext(file)[1].lower())}"
            )
        
        await client.send_message(
                chat_id=bot.chat.id,
                text=(
                    f"File Name: <code>{file_name}</code>"
                    f"\nFile Size: <code>{file_size}</code>  https://www.aparat.com/v/{dl}"
                ),
                reply_markup=completedKeyboard("https://www.aparat.com/v/"+dl)
            )
        
    except client_except as e:
        await client.edit_message_text(
            chat_id=bot.from_user.id,
            message_id=bot.message_id,
            text=f"{e}"
        )
        os.remove(file)
        LOGGER.info(f"{bot.from_user.id} - aparat - file_size - {e}")
