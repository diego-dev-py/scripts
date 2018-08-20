# the geo json geometry object we got from geojson.io
geo_json_geometry = {
  "type": "Polygon",
  "coordinates": [
                [
                    [-55.5, -30.0],
                    [-54.0, -30.0],
                    [-54.0, -31.0],
                    [-55.5, -31.0],
                    [-55.5, -30.0]
                ]
            ]
}

# filter for items the overlap with our chosen geometry
geometry_filter = {
  "type": "GeometryFilter",
  "field_name": "geometry",
  "config": geo_json_geometry
}

# filter images acquired in a certain date range
date_range_filter = {
  "type": "DateRangeFilter",
  "field_name": "acquired",
  "config": {
    "gte": "2017-09-01T00:00:00.000Z",
    "lte": "2017-09-30T23:59:00.000Z"
  }
}

# filter any images which are more than 50% clouds
cloud_cover_filter = {
  "type": "RangeFilter",
  "field_name": "cloud_cover",
  "config": {
    "lte": 0.5
  }
}

# create a filter that combines our geo and date filters
# could also use an "OrFilter"
redding_reservoir = {
  "type": "AndFilter",
  "config": [geometry_filter, date_range_filter, cloud_cover_filter]
}