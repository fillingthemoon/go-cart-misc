import settings
import handlers.base_handler
import csv

class CartogramHandler(handlers.base_handler.BaseCartogramHandler):

    def get_name(self):
        return "ASEAN Countries"

    def get_gen_file(self):
        return "{}/asean_processedmap.json".format(settings.CARTOGRAM_DATA_DIR)
    
    def validate_values(self, values):

        if len(values) != 10:
            return False
        
        for v in values:
            if type(v) != float:
                return False

        return True
    
    def gen_area_data(self, values):
        return """cartogram_id,Region Data,Region Name,Inset\n
1,{},BRN,L\n
2,{},IDN,L\n
3,{},KHM,L\n
4,{},LAO,L\n
5,{},MMR,R\n
6,{},MYS,R\n
7,{},PHL,R\n
8,{},SGP,R\n
9,{},THA,R\n
10,{},VNM,R\n""".format(*values)
    
    def expect_geojson_output(self):
        return True

    def csv_to_area_string_and_colors(self, csvfile):

        return self.order_by_example(csv.reader(csvfile), "Country", 0, 1, 2, 3, ["BRN","IDN","KHM","LAO","MMR","MYS","PHL","SGP","THA","VNM"], [0.0 for i in range(0,10)], {"BRN":"1","IDN":"2","KHM":"3","LAO":"4","MMR":"5","MYS":"6","PHL":"7","SGP":"8","THA":"9","VNM":"10"})
