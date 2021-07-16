import settings
import handlers.base_handler
import csv

class CartogramHandler(handlers.base_handler.BaseCartogramHandler):

    def get_name(self):
        return "Chile"

    def get_gen_file(self):
        return "{}/chl_processedmap.json".format(settings.CARTOGRAM_DATA_DIR)
    
    def validate_values(self, values):

        if len(values) != 16:
            return False
        
        for v in values:
            if type(v) != float:
                return False

        return True
    
    def gen_area_data(self, values):
        return """cartogram_id,Region Data,Region Name,Inset
1,{},Aisen del General Carlos Ibanez del Campo,L
2,{},Antofagasta,L
3,{},Araucania,L
4,{},Arica y Parinacota,L
5,{},Atacama,L
6,{},Biobio,L
7,{},Coquimbo,L
8,{},Libertador General Bernardo O'Higgins,R
9,{},Los Lagos,R
10,{},Los Rios,R
11,{},Magallanes y Antartica Chilena,R
12,{},Maule,R
13,{},Nuble,R
14,{},Region Metropolitana de Santiago,R
15,{},Tarapaca,R
16,{},Valparaiso,R""".format(*values)
    
    def expect_geojson_output(self):
        return True

    def csv_to_area_string_and_colors(self, csvfile):

        return self.order_by_example(csv.reader(csvfile), "Region", 0, 1, 2, 3, ["Aisen del General Carlos Ibanez del Campo","Antofagasta","Araucania","Arica y Parinacota","Atacama","Biobio","Coquimbo","Libertador General Bernardo O'Higgins","Los Lagos","Los Rios","Magallanes y Antartica Chilena","Maule","Nuble","Region Metropolitana de Santiago","Tarapaca","Valparaiso"], [0.0 for i in range(0,16)], {"Aisen del General Carlos Ibanez del Campo":"1","Antofagasta":"2","Araucania":"3","Arica y Parinacota":"4","Atacama":"5","Biobio":"6","Coquimbo":"7","Libertador General Bernardo O'Higgins":"8","Los Lagos":"9","Los Rios":"10","Magallanes y Antartica Chilena":"11","Maule":"12","Nuble":"13","Region Metropolitana de Santiago":"14","Tarapaca":"15","Valparaiso":"16"})
