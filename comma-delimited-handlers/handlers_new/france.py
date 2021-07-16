import settings
import handlers.base_handler
import csv

class CartogramHandler(handlers.base_handler.BaseCartogramHandler):

    def get_name(self):
        return "France"

    def get_gen_file(self):
        return "{}/fra_processedmap.json".format(settings.CARTOGRAM_DATA_DIR)
    
    def validate_values(self, values):

        if len(values) != 13:
            return False
        
        for v in values:
            if type(v) != float:
                return False

        return True
    
    def gen_area_data(self, values):
        return """cartogram_id,Region Data,Region Name,Inset
1,{},Auvergne-Rhone-Alpes,L
2,{},Bourgogne-Franche-Comte,L
3,{},Brittany,L
4,{},Centre-Val de Loire,L
5,{},Corsica,L
6,{},Grand Est,L
7,{},Hauts-de-France,R
8,{},Ile-de-France,R
9,{},Normandy,R
10,{},Nouvelle-Aquitaine,R
11,{},Occitanie,R
12,{},Pays de la Loire,R
13,{},Provence-Alpes-Cote d'Azur,R""".format(*values)
    
    def expect_geojson_output(self):
        return True

    def csv_to_area_string_and_colors(self, csvfile):

        return self.order_by_example(csv.reader(csvfile), "Region", 0, 1, 2, 3, ["Auvergne-Rhone-Alpes","Bourgogne-Franche-Comte","Brittany","Centre-Val de Loire","Corsica","Grand Est","Hauts-de-France","Ile-de-France","Normandy","Nouvelle-Aquitaine","Occitanie","Pays de la Loire","Provence-Alpes-Cote d'Azur"], [0.0 for i in range(0,13)], {"Auvergne-Rhone-Alpes":"1","Bourgogne-Franche-Comte":"2","Brittany":"3","Centre-Val de Loire":"4","Corsica":"5","Grand Est":"6","Hauts-de-France":"7","Ile-de-France":"8","Normandy":"9","Nouvelle-Aquitaine":"10","Occitanie":"11","Pays de la Loire":"12","Provence-Alpes-Cote d'Azur":"13"})
