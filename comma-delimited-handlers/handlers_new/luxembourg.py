import settings
import handlers.base_handler
import csv

class CartogramHandler(handlers.base_handler.BaseCartogramHandler):

    def get_name(self):
        return "Luxembourg"

    def get_gen_file(self):
        return "{}/lux_processedmap.json".format(settings.CARTOGRAM_DATA_DIR)
    
    def validate_values(self, values):

        if len(values) != 12:
            return False
        
        for v in values:
            if type(v) != float:
                return False

        return True
    
    def gen_area_data(self, values):
        return """cartogram_id,Region Data,Region Name,Inset
1,{},Capellen,L
2,{},Clervaux,L
3,{},Diekirch,L
4,{},Echternach,L
5,{},Esch-sur-Alzette,L
6,{},Grevenmacher,R
7,{},Luxembourg,R
8,{},Mersch,R
9,{},Redange,R
10,{},Remich,R
11,{},Vianden,R
12,{},Wiltz,R""".format(*values)
    
    def expect_geojson_output(self):
        return True

    def csv_to_area_string_and_colors(self, csvfile):

        return self.order_by_example(csv.reader(csvfile), "Canton", 0, 1, 2, 3, ["Capellen","Clervaux","Diekirch","Echternach","Esch-sur-Alzette","Grevenmacher","Luxembourg","Mersch","Redange","Remich","Vianden","Wiltz"], [0.0 for i in range(0,12)], {"Capellen":"1","Clervaux":"2","Diekirch":"3","Echternach":"4","Esch-sur-Alzette":"5","Grevenmacher":"6","Luxembourg":"7","Mersch":"8","Redange":"9","Remich":"10","Vianden":"11","Wiltz":"12"})
