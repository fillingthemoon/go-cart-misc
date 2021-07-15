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
        return """cartogram_id,Region Data,Region Name,Inset\n
1,{},Harju,L\n
2,{},Hiiu,L\n
3,{},Ida-Viru,L\n
4,{},Jarva,L\n
5,{},Jogeva,L\n
6,{},Laane,L\n
7,{},Laane-Viru,L\n
8,{},Parnu,R\n
9,{},Polva,R\n
10,{},Rapla,R\n
11,{},Saare,R\n
12,{},Tartu,R\n
13,{},Valga,R\n
14,{},Vilijandi,R\n
15,{},Voru,R\n""".format(*values)
    
    def expect_geojson_output(self):
        return True

    def csv_to_area_string_and_colors(self, csvfile):

        return self.order_by_example(csv.reader(csvfile), "County", 0, 1, 2, 3, ["Harju","Hiiu","Ida-Viru","Jarva","Jogeva","Laane","Laane-Viru","Parnu","Polva","Rapla","Saare","Tartu","Valga","Vilijandi","Voru"], [0.0 for i in range(0,15)], {"Harju":"1","Hiiu":"2","Ida-Viru":"3","Jarva":"4","Jogeva":"5","Laane":"6","Laane-Viru":"7","Parnu":"8","Polva":"9","Rapla":"10","Saare":"11","Tartu":"12","Valga":"13","Vilijandi":"14","Voru":"15"})
