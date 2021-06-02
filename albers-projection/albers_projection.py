import json
import math

def albers_formula():

  pass

def albers_projection(dir, file_name):
  file = open(dir + file_name)
  geojson_data = json.load(file)

  # Earth's radius / latitude
  radius = 57

  # bbox = [min_lon, min_lat, max_lon, max_lat]
  bbox = geojson_data['bbox']

  # reference longitude and latitude
  lambda_0 = (bbox[0] + bbox[2]) / 2
  phi_0 = (bbox[1] + bbox[3]) / 2

  # standard parallels
  phi_1 = (phi_0 + bbox[3]) / 2
  phi_2 = (phi_0 + bbox[1]) / 2

  n = (1/2) * (math.sin(phi_1) + math.sin(phi_2))
  # theta = n * ()

  new_geojson_data = geojson_data
  # iterate through GeoJSON coords
  for feature in geojson_data['features']:
    for multipolygon in feature['geometry']['coordinates']:
      # if len(multipolygon) > 1: 2nd polygon onwards are holes
      for polygon in multipolygon:
        for coords in polygon:
          # albers_formula(coords)
          pass

  with open('data_converted/' + file_name.split('.')[0] + '_converted.geojson', 'w') as new_geojson_file:
    json.dump(new_geojson_data, new_geojson_file)


dir = './data/'
file_name = 'angola.geojson'
albers_projection(dir, file_name)