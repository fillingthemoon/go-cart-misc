import json

def albers_formula():

  pass

def albers_projection(file_name):
  file = open(file_name)
  geojson_data = json.load(file)

  # bbox = [min_lon, min_lat, max_lon, max_lat]
  bbox = geojson_data['bbox']

  # references
  ref_lon = (bbox[0] + bbox[2]) / 2
  ref_lat = (bbox[1] + bbox[3]) / 2

  # standard parallels
  lat_parallel_1 = (ref_lat + bbox[3]) / 2
  lat_parallel_2 = (ref_lat + bbox[1]) / 2

  # iterate through GeoJSON coords
  for feature in geojson_data['features']:
    for multipolygon in feature['geometry']['coordinates']:
      # if len(multipolygon) > 1: 2nd polygon onwards are holes
      for polygon in multipolygon:
        for coords in polygon:
          # albers_formula(coords)
          pass


file_name = './data/angola.geojson'

albers_projection(file_name)