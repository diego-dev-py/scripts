import json
import ogr
# path = '/mnt/auxiliar/BASE_DADOS/FIM-PANAMA/limites-panama/mask_panama/mask_panama.shp'
driver = ogr.GetDriverByName('ESRI Shapefile')
shp_path = r'/mnt/auxiliar/backup_documentos/cartas_divididas/nextgenmap_grids/nextgenmap_grids.shp'
data_source = driver.Open(shp_path, 0)

fc = {
    'type': 'FeatureCollection',
    'features': []
    }

lyr = data_source.GetLayer(0)

for feature in lyr:    
    fc['features'].append(feature.ExportToJson(as_object=True))


with open('grids-ngm.json', 'wb') as f:
    json.dump(fc, f)