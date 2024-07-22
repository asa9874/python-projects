import requests
import json
import pprint
import time
import asyncio

headers = {'User-Agent': 'Mozilla/5.0'} 
user='45e71a76e949e16a34764deb962f9d9f'#아야츠노 유니
url='https://api.chzzk.naver.com/service/v1/channels/'+user


async def checking():
    last_check=0
    check=0
    while True:
        print("탐색")
        r= requests.get(url,headers=headers)
        if(r.json()['content']['openLive'] == True): check= 1
        else: check=0
        if check != last_check:
            if check == 0: print("뱅오프~")
            else: print("뱅온")
        last_check=check
        await asyncio.sleep(3)


asyncio.run(checking())