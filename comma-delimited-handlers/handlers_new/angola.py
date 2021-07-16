import settings
import handlers.base_handler
import csv

class CartogramHandler(handlers.base_handler.BaseCartogramHandler):

    def get_name(self):
        return "Angola"

    def get_gen_file(self):
        return "{}/angola_processedmap.json".format(settings.CARTOGRAM_DATA_DIR)
    
    def validate_values(self, values):

        if len(values) != 18:
            return False
        
        for v in values:
            if type(v) != float:
                return False

        return True
    
    def gen_area_data(self, values):
        return """cartogram_id,Region Data,Region Name,Inset
1,{},Bengo,L
2,{},Benguela,L
3,{},Bie,L
4,{},Cabinda,L
5,{},Cuando Cubango,L
6,{},Cuanza Norte,L
7,{},Cuanza Sul,L
8,{},Cunene,L
9,{},Huambo,R
10,{},Huila,R
11,{},Luanda,R
12,{},Lunda Norte,R
13,{},Lunda Sul,R
14,{},Malanje,R
15,{},Moxico,R
16,{},Namibe,R
17,{},Uige,R
18,{},Zaire,R""".format(*values)
    
    def expect_geojson_output(self):
        return True

    def csv_to_area_string_and_colors(self, csvfile):

        return self.order_by_example(csv.reader(csvfile), "Province", 0, 1, 2, 3, ["Bengo","Benguela","Bie","Cabinda","Cuando Cubango","Cuanza Norte","Cuanza Sul","Cunene","Huambo","Huila","Luanda","Lunda Norte","Lunda Sul","Malanje","Moxico","Namibe","Uige","Zaire"], [0.0 for i in range(0,18)], {"Bengo":"1","Benguela":"2","Bie":"3","Cabinda":"4","Cuando Cubango":"5","Cuanza Norte":"6","Cuanza Sul":"7","Cunene":"8","Huambo":"9","Huila":"10","Luanda":"11","Lunda Norte":"12","Lunda Sul":"13","Malanje":"14","Moxico":"15","Namibe":"16","Uige":"17","Zaire":"18"})
