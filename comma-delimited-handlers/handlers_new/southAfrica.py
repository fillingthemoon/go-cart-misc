import settings
import handlers.base_handler
import csv

class CartogramHandler(handlers.base_handler.BaseCartogramHandler):

    def get_name(self):
        return "South Africa"

    def get_gen_file(self):
        return "{}/southAfrica_processedmap.json".format(settings.CARTOGRAM_DATA_DIR)
    
    def validate_values(self, values):

        if len(values) != 9:
            return False
        
        for v in values:
            if type(v) != float:
                return False

        return True
    
    def gen_area_data(self, values):
        return """cartogram_id,Region Data,Region Name,Inset
1,{},Eastern Cape,L
2,{},Free State,L
3,{},Gauteng,L
4,{},KwaZulu-Natal,L
5,{},Limpopo,R
6,{},Mpumalanga,R
7,{},North West,R
8,{},Northern Cape,R
9,{},Western Cape,R""".format(*values)
    
    def expect_geojson_output(self):
        return True

    def csv_to_area_string_and_colors(self, csvfile):

        return self.order_by_example(csv.reader(csvfile), "Province", 0, 1, 2, 3, ["Eastern Cape","Free State","Gauteng","KwaZulu-Natal","Limpopo","Mpumalanga","North West","Northern Cape","Western Cape"], [0.0 for i in range(0,9)], {"Eastern Cape":"1","Free State":"2","Gauteng":"3","KwaZulu-Natal":"4","Limpopo":"5","Mpumalanga":"6","North West":"7","Northern Cape":"8","Western Cape":"9"})
