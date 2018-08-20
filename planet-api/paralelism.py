import os
import requests
from multiprocessing.dummy import Pool as ThreadPool

# setup auth
session = requests.Session()
session.auth = (os.environ['PL_API_KEY'], '')
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

asset_type = "analytic"
def activate_item(item_id):
    print "activating: " + item_id + '\n'
    item_type = typeImages[2]

    # request an item
    # item = session.get(("https://api.planet.com/data/v1/item-types/" +"{}/items/{}/assets/").format(typeImages[2], item_id))
    # # item = \
    # # session.get(
    # #     ("https://api.planet.com/data/v1/item-types/" +
    # #     "{}/items/{}/assets/").format(item_type, item_id))
    # print item.json()
    # # request activation
    # session.post(item.json()["analytic"]["_links"]["activate"])
    item = \
        session.get(
            ("https://api.planet.com/data/v1/item-types/" +
            "{}/items/{}/assets/").format(item_type, item_id))

# extract the activation url from the item for the desired asset
    item_activation_url = item.json()[asset_type]["_links"]["activate"]


# An easy way to parallise I/O bound operations in Python
# is to use a ThreadPool.
parallelism = 3
thread_pool = ThreadPool(parallelism)

# Open up a file of ids that we have already retrieved from a search
with open('/home/diego-silva/Documentos/planet-api/search_count_terras.txt') as f:
    item_ids = f.read().splitlines()[:100] # only grab 100

# In this example, all items will be sent to the `activate_item` function
# but only 5 will be running at once
thread_pool.map(activate_item, item_ids)
