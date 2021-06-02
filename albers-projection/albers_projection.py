import json

def albers_formula():
  pass

def albers_projection(file_name):
  file = open(file_name)
  geojson_data = json.load(file)

  for feature in geojson_data['features']:
    for multipolygon in feature['geometry']['coordinates']:
      # If len(multipolygon) > 1: 2nd polygon onwards are holes
      for polygon in multipolygon:
        for coords in polygon:
          pass


file_name = './data/angola.geojson'

print(albers_projection(file_name))