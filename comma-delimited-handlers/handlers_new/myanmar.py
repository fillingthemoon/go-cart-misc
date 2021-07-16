import settings
import handlers.base_handler
import csv

class CartogramHandler(handlers.base_handler.BaseCartogramHandler):

    def get_name(self):
        return "Myanmar"

    def get_gen_file(self):
        return "{}/mmr_processedmap.json".format(settings.CARTOGRAM_DATA_DIR)
    
    def validate_values(self, values):

        if len(values) != 15:
            return False
        
        for v in values:
            if type(v) != float:
                return False

        return True
    
    def gen_area_data(self, values):
        return """cartogram_id,Region Data,Region Name,Inset
1,{},Ayeyarwady,L
2,{},Bago,L
3,{},Chin,L
4,{},Kachin,L
5,{},Kayah,L
6,{},Kayin,L
7,{},Magway,L
8,{},Mandalay,R
9,{},Mon,R
10,{},Naypyitaw,R
11,{},Rakhine,R
12,{},Sagaing,R
13,{},Shan,R
14,{},Tanintharyi,R
15,{},Yangon,R""".format(*values)
    
    def expect_geojson_output(self):
        return True

    def csv_to_area_string_and_colors(self, csvfile):

        return self.order_by_example(csv.reader(csvfile), "State/Region", 0, 1, 2, 3, ["Ayeyarwady","Bago","Chin","Kachin","Kayah","Kayin","Magway","Mandalay","Mon","Naypyitaw","Rakhine","Sagaing","Shan","Tanintharyi","Yangon"], [0.0 for i in range(0,15)], {"Ayeyarwady":"1","Bago":"2","Chin":"3","Kachin":"4","Kayah":"5","Kayin":"6","Magway":"7","Mandalay":"8","Mon":"9","Naypyitaw":"10","Rakhine":"11","Sagaing":"12","Shan":"13","Tanintharyi":"14","Yangon":"15"})
