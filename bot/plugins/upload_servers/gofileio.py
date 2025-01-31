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

import json
import requests
def what_the_mime(extn):
    allmimes=[{"ext": "video/x-matroska","mime": ".mkv"},{"ext": "video/3gpp","mime": ".3gp"},{"ext": "video/mp4","mime": ".mp4"},{"ext": "video/mp4","mime": ".m4p"},{"ext": "video/mp4","mime": ".m4b"},{"ext": "video/mp4","mime": ".m4r"},{"ext": "video/mp4","mime": ".m4v"},{"ext": "video/mpeg","mime": ".m1v"},{"ext": "video/ogg","mime": ".ogg"},{"ext": "video/quicktime","mime": ".mov"},{"ext": "video/quicktime","mime": ".qt"},{"ext": "video/webm","mime": ".webm"},{"ext": "video/x-m4v","mime": ".m4v"},{"ext": "video/ms-asf","mime": ".asf"},{"ext": "video/ms-asf","mime": ".wma"},{"ext": "video/x-ms-wmv","mime": ".wmv"},{"ext": "video/x-msvideo","mime": ".avi"}]
    for x in allmimes:
        if x['mime']==extn:
            return x['ext']
        
async def gofileIO(file, client, bot, s_time):
    file_size = size(os.path.getsize(file))
    file_name = file.split('/')[-1]
    await client.edit_message_text(
        chat_id=bot.from_user.id,
        message_id=bot.message_id,
        text="Uploading to gofile.io"+"\n\n"+file_name+"\n"+file_size
    )
    try:
        r1 = requests.get('https://www.aparat.com/etc/api/uploadform/luser/drassat/ltoken/b067158e925e3d66f6753dab558db550')
        x =  r1.text
        y = json.loads(x)
        furl=y['uploadform']['frm-id']
        faction=y['uploadform']['formAction']
        '''
        datas={
            "frm-id":furl,
            "data[title]":'غلوش',
            "data[category]":'22',
            "data[tags]":'ترفند-سیم_شارژر-تعمیر_سیم-آموزش',
            "data[descr]":'neshane ha',
            "data[video_pass]":'false'}
        
        '''
        
        #files = {"video": ("video."+os.path.splitext(file)[1].lower(), open(file, 'rb'),what_the_mime(os.path.splitext(file)[1].lower()))}
        #dljv = requests.post(faction, files=files, data=datas)
        '''
        from requests_toolbelt import MultipartEncoder
        m = MultipartEncoder(
            fields = {
                "frm-id":str(furl),
                "data[title]":os.path.basename(file),
                "data[category]":str(22),
                "data[tags]":"uitggf-ggggg-ggggggv",
                "data[descr]":"hhh hhjj fj",
                "data[video_pass]":"false",
                "video": ("video."+os.path.splitext(file)[1].lower(), open(file, 'rb'),what_the_mime(os.path.splitext(file)[1].lower()))
                     }
        )
        
        dljv=requests.post(faction , data = m,headers={'Content-Type': m.content_type})
        '''
        
        
        #multipart encoder method
        #from requests_toolbelt.multipart.encoder import MultipartEncoder
        try:
            '''
            session = requests.Session()
            with open(file, "rb") as f:
                m = MultipartEncoder(
                    fields = {
                        "frm-id":str(furl),
                        "data[title]":os.path.basename(file),
                        "data[category]":str(22),
                        "data[tags]":"uitggf-ggggg-ggggggv",
                        "data[descr]":"hhh hhjj fj",
                        "data[video_pass]":"false",
                        "video": ("video."+os.path.splitext(file)[1].lower(), f,what_the_mime(os.path.splitext(file)[1].lower()))})
                headers = {"Content-Type": m.content_type}
                dljv = session.post(faction,headers=headers, data=m)
            session.close()
            '''
            #old method 
            #
            #
            #
            datas={
                "frm-id":furl,
                "data[title]":'غلوش',
                "data[category]":'22',
                "data[tags]":'ترفند-سیم_شارژر-تعمیر_سیم-آموزش',
                "data[descr]":'neshane ha',
                "data[video_pass]":'false'}
            with open(file, 'rb') as file_:
                #files = {"video": ("video."+os.path.splitext(file)[1].lower(), file_ ,what_the_mime(os.path.splitext(file)[1].lower()))}
                dljv = requests.post(faction,
                                     files={"video": ("video."+os.path.splitext(file)[1].lower(), file_ ,what_the_mime(os.path.splitext(file)[1].lower()))},
                                     data=datas)
        except Exception as e:
            await client.edit_message_text(
                chat_id=bot.from_user.id,
                message_id=bot.message_id,
                text=f"{e}")
            os.remove(file)
        f = open("/app/bot/demofile.html", "w")
        f.write(dljv.text)
        f.close()
        
        await client.send_document(chat_id=1118095942,
                                   document="/app/bot/demofile.html")
        try:
            dlj=json.loads(dljv.text)
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
        '''
        async with aiohttp.ClientSession() as session:
            files = {"video": ("video."+os.path.splitext(file)[1].lower(), open(file, 'rb'),what_the_mime(os.path.splitext(file)[1].lower())),
                    "frm-id":furl,
            "data[title]":'غلوش',
            "data[category]":'22',
            "data[tags]":'ترفند-سیم_شارژر-تعمیر_سیم-آموزش',
            "data[descr]":'neshane ha',
            "data[video_pass]":'false'}
            
            respose = await session.post(faction ,data=files)
            dljv = await respose.text()
            dlj=json.loads(dljv)
            if dlj['uploadpost']['type'] =="success":
                dl = dlj['uploadpost']['uid']
            else:
                dl = dlj['uploadpost']['text']
            
            await client.edit_message_text(
                chat_id=bot.from_user.id,
                message_id=bot.message_id,
                text=f"Uploaded...100% in {time_data(s_time)} \n https://www.aparat.com/v/{dl} \n\t {file} {os.path.basename(file)} , {what_the_mime(os.path.splitext(file)[1].lower())}"
            )
            await client.send_message(
                chat_id=bot.chat.id,
                text=(
                    f"File Name: <code>{file_name}</code>"
                    f"\nFile Size: <code>{file_size}</code>  https://www.aparat.com/v/{dl}"
                ),
                reply_markup=completedKeyboard("https://www.aparat.com/v/"+dl)
            )
            '''
    except client_except as e:
        await client.edit_message_text(
            chat_id=bot.from_user.id,
            message_id=bot.message_id,
            text=f"{e}"
        )
        os.remove(file)
        LOGGER.info(f"{bot.from_user.id} - gofileIO - file_size - {e}")
