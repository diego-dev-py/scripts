import os
import requests
import json
from requests.auth import HTTPBasicAuth



# our demo filter that filters by geometry, date and cloud cover
from demo_filters import redding_reservoir

# Stats API request object
stats_endpoint_request = {
  "interval": "day",
  "item_types": ["REOrthoTile"],
  "filter": redding_reservoir
}

# fire off the POST request
result = \
  requests.post(
    'https://api.planet.com/data/v1/stats',
    auth=HTTPBasicAuth(os.environ['PL_API_KEY'], ''),
    json=stats_endpoint_request)
arq = open('/home/diego-silva/Documentos/planet-api/json-teste2.txt','w')
arq.writelines(result)
arq.close()

# print result.txt
