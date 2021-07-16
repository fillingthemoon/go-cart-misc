import settings
import handlers.base_handler
import csv

class CartogramHandler(handlers.base_handler.BaseCartogramHandler):

    def get_name(self):
        return "Estonia"

    def get_gen_file(self):
        return "{}/est_processedmap.json".format(settings.CARTOGRAM_DATA_DIR)
    
    def validate_values(self, values):

        if len(values) != 15:
            return False
        
        for v in values:
            if type(v) != float:
                return False

        return True
    
    def gen_area_data(self, values):
        return """cartogram_id,Region Data,Region Name,Inset
1,{},Harju,L
2,{},Hiiu,L
3,{},Ida-Viru,L
4,{},Jarva,L
5,{},Jogeva,L
6,{},Laane,L
7,{},Laane-Viru,L
8,{},Parnu,R
9,{},Polva,R
10,{},Rapla,R
11,{},Saare,R
12,{},Tartu,R
13,{},Valga,R
14,{},Vilijandi,R
15,{},Voru,R""".format(*values)
    
    def expect_geojson_output(self):
        return True

    def csv_to_area_string_and_colors(self, csvfile):

        return self.order_by_example(csv.reader(csvfile), "County", 0, 1, 2, 3, ["Harju","Hiiu","Ida-Viru","Jarva","Jogeva","Laane","Laane-Viru","Parnu","Polva","Rapla","Saare","Tartu","Valga","Vilijandi","Voru"], [0.0 for i in range(0,15)], {"Harju":"1","Hiiu":"2","Ida-Viru":"3","Jarva":"4","Jogeva":"5","Laane":"6","Laane-Viru":"7","Parnu":"8","Polva":"9","Rapla":"10","Saare":"11","Tartu":"12","Valga":"13","Vilijandi":"14","Voru":"15"})
