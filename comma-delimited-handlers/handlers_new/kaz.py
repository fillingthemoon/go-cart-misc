import settings
import handlers.base_handler
import csv

class CartogramHandler(handlers.base_handler.BaseCartogramHandler):

    def get_name(self):
        return "Kazakhstan"

    def get_gen_file(self):
        return "{}/kaz_processedmap.json".format(settings.CARTOGRAM_DATA_DIR)
    
    def validate_values(self, values):

        if len(values) != 14:
            return False
        
        for v in values:
            if type(v) != float:
                return False

        return True
    
    def gen_area_data(self, values):
        return """cartogram_id,Region Data,Region Name,Inset\n
1,{},Almaty,L\n
2,{},Akmola,L\n
3,{},Aktobe,L\n
4,{},Atyrau,L\n
5,{},East Kazakhstan,L\n
6,{},Mangystau,L\n
7,{},North Kazakhstan,R\n
8,{},Pavlodar,R\n
9,{},Karagandy,R\n
10,{},Kostanay,R\n
11,{},Kyzylorda,R\n
12,{},Turkistan Region,R\n
13,{},West Kazakhstan,R\n
14,{},Zhambyl,R\n""".format(*values)
    
    def expect_geojson_output(self):
        return True

    def csv_to_area_string_and_colors(self, csvfile):

        return self.order_by_example(csv.reader(csvfile), "Region", 0, 1, 2, 3, ["Almaty","Akmola","Aktobe","Atyrau","East Kazakhstan","Mangystau","North Kazakhstan","Pavlodar","Karagandy","Kostanay","Kyzylorda","Turkistan Region","West Kazakhstan","Zhambyl"], [0.0 for i in range(0,14)], {"Almaty":"1","Akmola":"2","Aktobe":"3","Atyrau":"4","East Kazakhstan":"5","Mangystau":"6","North Kazakhstan":"7","Pavlodar":"8","Karagandy":"9","Kostanay":"10","Kyzylorda":"11","Turkistan Region":"12","West Kazakhstan":"13","Zhambyl":"14"})
