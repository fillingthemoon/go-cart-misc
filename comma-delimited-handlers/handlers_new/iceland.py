import settings
import handlers.base_handler
import csv

class CartogramHandler(handlers.base_handler.BaseCartogramHandler):

    def get_name(self):
        return "Iceland"

    def get_gen_file(self):
        return "{}/isl_processedmap.json".format(settings.CARTOGRAM_DATA_DIR)
    
    def validate_values(self, values):

        if len(values) != 8:
            return False
        
        for v in values:
            if type(v) != float:
                return False

        return True
    
    def gen_area_data(self, values):
        return """cartogram_id,Region Data,Region Name,Inset\n
1,{},Eastern Region,L\n
2,{},Northeastern Region,L\n
3,{},Capital Region,L\n
4,{},Northwestern Region,R\n
5,{},Southern Region,R\n
6,{},Southern Peninsula,R\n
7,{},Westfjords,R\n
8,{},Western Region,R\n""".format(*values)
    
    def expect_geojson_output(self):
        return True

    def csv_to_area_string_and_colors(self, csvfile):

        return self.order_by_example(csv.reader(csvfile), "Region", 0, 1, 2, 3, ["Eastern Region","Northeastern Region","Capital Region","Northwestern Region","Southern Region","Southern Peninsula","Westfjords","Western Region"], [0.0 for i in range(0,8)], {"Eastern Region":"1","Northeastern Region":"2","Capital Region":"3","Northwestern Region":"4","Southern Region":"5","Southern Peninsula":"6","Westfjords":"7","Western Region":"8"})
