import json
import csv

def gen_file_json_script(input_dir, input_json, input_csv):

  # area_data (CSV)
  area_data = ""
  area_data += ",".join(next(csv.reader(open(input_dir + input_csv)))) + "\n"

  csv_data = csv.DictReader(open(input_dir + input_csv))
  for row in csv_data:
    area_data += ",".join(row.values()) + "\n"

  gen_file_data = {}
  gen_file_data['area_data'] = area_data
  gen_file_data['key'] = 'random_string'

  # gen_file (JSON)
  json_file = open(input_dir + input_json)
  json_data = json.load(json_file)
  gen_file_data['gen_file'] = json.dumps(json_data).replace('"', '\"')

  with open('./output/' + input_json, 'w') as new_json_file:
    json.dump(gen_file_data, new_json_file, indent=2)

input_dir = './input/'
input_json = 'singapore_re.json'
input_csv = 'singapore_re.csv'
gen_file_json_script(input_dir, input_json, input_csv)