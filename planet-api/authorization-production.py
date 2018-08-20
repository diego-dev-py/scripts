import os
import requests
import json
from requests.auth import HTTPBasicAuth

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


for asset in item_ids:
    
    command =  """curl -L -H "Authorization: api-key $PL_API_KEY" 'https://api.planet.com/data/v1/item-types/PSScene4Band/items/""" \
                +asset+"""/assets/'"""\
                """| jq .analytic.location>auth_sptember3.txt"""
    
    print command
    os.system(command)

    with open('/home/diego-silva/Documentos/planet-api/auth_sptember3.txt') as f:
        
        item_id = f.read().splitlines()
        print item_id 
        os.system("wget " + item_id[0] + " -O /home/diego-silva/Documentos/planet-api/" + asset)

    
    
