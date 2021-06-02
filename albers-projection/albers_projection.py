import json
import math

def albers_formula(bbox, coords):
  min_lon = bbox[0]
  min_lat = bbox[1]
  max_lon = bbox[2]
  max_lat = bbox[3]

  lon = coords[0]
  lat = coords[1]

  # What is this value? TBC
  radius = 200

  # reference longitude and latitude
  lambda_0 = (min_lon + max_lon) / 2
  phi_0 = (min_lat + max_lat) / 2

  # standard parallels
  phi_1 = (phi_0 + max_lat) / 2
  phi_2 = (phi_0 + min_lat) / 2

  n = (1/2) * (math.sin(phi_1) + math.sin(phi_2))

  theta = n * (lon - lambda_0)
  c = ((math.cos(phi_1)) ** 2) + (2 * n * math.sin(phi_1))
  rho = (radius / n) * math.sqrt(c - (2 * n * math.sin(lat)))
  rho_0 = (radius / n) * math.sqrt(c - (2 * n * math.sin(phi_0)))

  new_lon = rho * math.sin(theta)
  new_lat = rho_0 - (rho * math.cos(theta))

  new_coords = [new_lon, new_lat]

  return new_coords

def albers_projection(dir, file_name):
  file = open(dir + file_name)
  geojson_data = json.load(file)

  # bbox = [min_lon, min_lat, max_lon, max_lat]
  bbox = geojson_data['bbox']

  new_geojson_data = geojson_data

  # iterate through GeoJSON coords
  for i, feature in enumerate(geojson_data['features']):
    for j, multipolygon in enumerate(feature['geometry']['coordinates']):
      # if len(multipolygon) > 1: 2nd polygon onwards are holes
      for k, polygon in enumerate(multipolygon):
        for l, coords in enumerate(polygon):
          new_coords = albers_formula(bbox, coords)
          new_geojson_data['features'][i]['geometry']['coordinates'][j][k][l] = new_coords

  with open('data_converted/' + file_name.split('.')[0] + '_converted.geojson', 'w') as new_geojson_file:
    json.dump(new_geojson_data, new_geojson_file)


dir = './data/'
file_name = 'angola.geojson'
# file_name = 'world.geojson'
albers_projection(dir, file_name)