import settings
import handlers.base_handler
import csv

class CartogramHandler(handlers.base_handler.BaseCartogramHandler):

    def get_name(self):
        return "Lebanon"

    def get_gen_file(self):
        return "{}/lbn_processedmap.json".format(settings.CARTOGRAM_DATA_DIR)
    
    def validate_values(self, values):

        if len(values) != 8:
            return False
        
        for v in values:
            if type(v) != float:
                return False

        return True
    
    def gen_area_data(self, values):
        return """cartogram_id,Region Data,Region Name,Inset
1,{},Akkar,L
2,{},Baalbak-Hermel,L
3,{},Beirut,L
4,{},Beqaa,R
5,{},Mount Lebanon,R
6,{},Nabatieh,R
7,{},North,R
8,{},South,R""".format(*values)
    
    def expect_geojson_output(self):
        return True

    def csv_to_area_string_and_colors(self, csvfile):

        return self.order_by_example(csv.reader(csvfile), "Governorate", 0, 1, 2, 3, ["Akkar","Baalbak-Hermel","Beirut","Beqaa","Mount Lebanon","Nabatieh","North","South"], [0.0 for i in range(0,8)], {"Akkar":"1","Baalbak-Hermel":"2","Beirut":"3","Beqaa":"4","Mount Lebanon":"5","Nabatieh":"6","North":"7","South":"8"})
