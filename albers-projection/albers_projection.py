import json
import math

def albers_formula(bbox, coords):
  min_lon = math.radians(bbox[0])
  min_lat = math.radians(bbox[1])
  max_lon = math.radians(bbox[2])
  max_lat = math.radians(bbox[3])

  lon = math.radians(coords[0])
  lat = math.radians(coords[1])  

  # What is this value? TBC
  radius = 1

  # reference longitude and latitude
  lambda_0 = (min_lon + max_lon) / 2
  phi_0 = (min_lat + max_lat) / 2

  # standard parallels
  phi_1 = 15 # (phi_0 + max_lat) / 2
  phi_2 = 45 # (phi_0 + min_lat) / 2

  n = (1/2) * (math.sin(phi_1) + math.sin(phi_2))

  # TODO
  # if (math.sin(phi_1) + math.sin(phi_2)):
  #   Deal with this

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

  # iterate through the country's features (i.e. states, provinces, etc.)
  for i, feature in enumerate(geojson_data['features']):

    # iterate through the feature's polgyons (contained inside a MultiPolygon)
    # if len(polygon) > 1: 2nd polygon onwards are holes
    for j, polygon_with_hole in enumerate(feature['geometry']['coordinates']):

      # iterate through the polygon_with_hole's polygon_or_hole objects
      for k, polygon_or_hole in enumerate(polygon_with_hole):

        # iterate through the coordinates of the polygon_or_hole
        for l, coords in enumerate(polygon_or_hole):
          new_coords = albers_formula(bbox, coords) # coords = [lon, lat]
          new_geojson_data['features'][i]['geometry']['coordinates'][j][k][l] = new_coords

  with open('data-converted/' + file_name.split('.')[0] + '_converted.geojson', 'w') as new_geojson_file:
    json.dump(new_geojson_data, new_geojson_file)


dir = './data/'
# file_name = 'angola.geojson'
# file_name = 'israel.geojson'
# file_name = 'singapore_pa.geojson'
# file_name = 'belgium.geojson'
# file_name = 'world.geojson'
# file_name = 'russia.geojson'
file_name = 'russia_modified.geojson'
albers_projection(dir, file_name)