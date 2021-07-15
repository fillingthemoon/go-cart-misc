import settings
import handlers.base_handler
import csv

class CartogramHandler(handlers.base_handler.BaseCartogramHandler):

    def get_name(self):
        return "Netherlands"

    def get_gen_file(self):
        return "{}/netherlands_processedmap.json".format(settings.CARTOGRAM_DATA_DIR)
    
    def validate_values(self, values):

        if len(values) != 12:
            return False
        
        for v in values:
            if type(v) != float:
                return False

        return True
    
    def gen_area_data(self, values):
        return """cartogram_id,Region Data,Region Name,Inset\n
1,{},Drenthe,L\n
2,{},Flevoland,L\n
3,{},Friesland,L\n
4,{},Gelderland,L\n
5,{},Groningen,L\n
6,{},Limburg,R\n
7,{},Noord-Brabant,R\n
8,{},Noord-Holland,R\n
9,{},Overijssel,R\n
10,{},Utrecht,R\n
11,{},Zeeland,R\n
12,{},Zuid-Holland,R\n""".format(*values)
    
    def expect_geojson_output(self):
        return True

    def csv_to_area_string_and_colors(self, csvfile):

        return self.order_by_example(csv.reader(csvfile), "Province", 0, 1, 2, 3, ["Drenthe","Flevoland","Friesland","Gelderland","Groningen","Limburg","Noord-Brabant","Noord-Holland","Overijssel","Utrecht","Zeeland","Zuid-Holland"], [0.0 for i in range(0,12)], {"Drenthe":"1","Flevoland":"2","Friesland":"3","Gelderland":"4","Groningen":"5","Limburg":"6","Noord-Brabant":"7","Noord-Holland":"8","Overijssel":"9","Utrecht":"10","Zeeland":"11","Zuid-Holland":"12"})
