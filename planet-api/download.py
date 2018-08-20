import os
import requests
from multiprocessing.dummy import Pool as ThreadPool


ativadores = [
    "https://api.planet.com/data/v1/download?token=eyJhbGciOiJIUzUxMiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiJQSEYwUnVzWlFpOUQwbWloMGxRVjF0Z2tnb3U2TTVWYVZpb2s5RXk3TkZSRCswelBSeVNvelRCS3FtSjVYSGpDMjh0RXdjS0ZVTmpydlpUNnk2TWhDZz09IiwiaXRlbV90eXBlX2lkIjoiUFNTY2VuZTRCYW5kIiwidG9rZW5fdHlwZSI6InR5cGVkLWl0ZW0iLCJleHAiOjE1MzM1NzEyNjIsIml0ZW1faWQiOiIyMDE3MDgzMV8xNTE0MzFfMTA0ZSIsImFzc2V0X3R5cGUiOiJhbmFseXRpYyJ9.r35SC5Bp3rMynFWLKiDWURkjMbRvuCKAXZUpgipuXWhGCtJ3QdXRyI5WB6RI37G9uwApGcRNasfBPa-_N7lDfQ",
    "https://api.planet.com/data/v1/download?token=eyJhbGciOiJIUzUxMiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiJVaTRMZEVDeHZLM3lIODYyUDJUcmJPNm0zSFhoMVp4M3BpRXFSclVoNi9uYVhFOC93MjJpTUpESHo0c0FyMjVsRWgyVkpUdlJJNzFCaXBzUU9vUlgyUT09IiwiaXRlbV90eXBlX2lkIjoiUFNTY2VuZTRCYW5kIiwidG9rZW5fdHlwZSI6InR5cGVkLWl0ZW0iLCJleHAiOjE1MzM1NzEyNjQsIml0ZW1faWQiOiIyMDE3MDgzMV8xNTE0MzZfMTA0ZSIsImFzc2V0X3R5cGUiOiJhbmFseXRpYyJ9.OG7Ah6hR93SwNo4CyUm4Cw0bM9Dx4i4owARn9gArDXUyzWvfZcVf3uDXIgcrPxOXWFXASOx-FeQcfyIoZoyGzQ",
    "https://api.planet.com/data/v1/download?token=eyJhbGciOiJIUzUxMiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiIzZEZwRlFnbXR2cytMR3ppdUJ4TExHdzF5alExTnV4T2ZFVGNMMFovY0ZXUk1wWnVmaDE1RUM2Y2Fqd3ArVEY0TExKYUhmMWJ3bW1LcFRFejVoVmt6dz09IiwiaXRlbV90eXBlX2lkIjoiUFNTY2VuZTRCYW5kIiwidG9rZW5fdHlwZSI6InR5cGVkLWl0ZW0iLCJleHAiOjE1MzM1NzEyNjYsIml0ZW1faWQiOiIyMDE3MDgzMV8xNTE0MjVfMTA0ZSIsImFzc2V0X3R5cGUiOiJhbmFseXRpYyJ9.SFQOYoB2sBIkxw8Dm49yOrC95HH9yrDu2MdZq7vCeG-sFuhHE8ondJB64Uk3wvr0KaJ5ZQBHmpuxsJAwx1vGhQ"
]
item_ids = [
    "20170919_151553_1052",
    "20170919_151555_1052",
    "20170919_151556_1052",
    "20170919_151559_1052",
    "20170919_151552_1052",
    "20170919_151558_1052",
    "20170919_151554_1052",
    "20170919_151557_1052",
    "20170919_151600_1052",
    "20170919_151210_1051",
    "20170919_151222_1051",
    "20170919_151218_1051",
    "20170919_151217_1051",
    "20170919_151209_1051",
    "20170919_151216_1051"
]
# for download in ativadores:
    
#     os.system("wget " + download)

def down_wget(item):
    
    os.system("wget " + item + " -O /home/diego-silva/Documentos/planet-api/" + item_ids[ativadores.index(item)])

map(down_wget,ativadores)
