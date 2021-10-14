#!/usr/bin/env python3
# This is bot coded by Abhijith N T and used for educational purposes only
# https://github.com/AbhijithNT
# Copyright ABHIJITH N T
# Thank you https://github.com/pyrogram/pyrogram


from bot.plugins.display.time import time_data
import time
import asyncio

async def progress(current, total, up_msg, message, start_time):
    

    try:
        diff = int(time.time() - start_time)
        if (int(time.time()) % 5 == 0) or (cur == tot):
            await asyncio.sleep(2)
            await message.edit(
                 text=f"{up_msg} {current * 100 / total:.1f}% in {time_data(start_time)}"
                )
    except Exception as e:
        await message.edit(
            text=f"ERROR: {e}"
        )

