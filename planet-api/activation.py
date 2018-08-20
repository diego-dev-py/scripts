import os
import requests
from retrying import retry
from multiprocessing.dummy import Pool as ThreadPool



typeImages = {
1:"MYD09GQ"       ,
2:"PSScene4Band",
3:"SkySatScene",
4:"PSScene3Band",
5:"Sentinel1",
6:"REScene",
7:"REOrthoTile",
8:"Sentinel2L1C",
9:"MOD09GA",
10:"MYD09GA",
11:"SkySatCollect",
12:"PSOrthoTile",
13:"Landsat8L1G",
14:"MOD09GQ"

}
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

item_type = typeImages[2]
asset_type = "analytic"

# setup auth
session = requests.Session()
session.auth = (os.environ['PL_API_KEY'], '')

@retry(
		wait_exponential_multiplier=1000,
		wait_exponential_max=10000)

def activate_item(item_id):
			
		print "activating: " + item_id + '\n'
# request an item
		item = \
			session.get(
				("https://api.planet.com/data/v1/item-types/" +
				"{}/items/{}/assets/").format(item_type, item_id))

		if item.status_code == 429:
					raise Exception("rate limit error")

		# extract the activation url from the item for the desired asset
		item_activation_url = item.json()[asset_type]["_links"]["activate"]


# request activation
		response = session.post(item_activation_url)

		if response.status_code == 429:
				raise Exception("rate limit error")
		 
		# print 'status code' + response.status_code 
		print "activation succeeded for item " + item_id
		
# with open('/home/diego-silva/Documentos/planet-api/september.txt') as f:
# 	item_ids = f.read().splitlines()


parallelism = 5
thread_pool = ThreadPool(parallelism)
thread_pool.map(activate_item, item_ids)
