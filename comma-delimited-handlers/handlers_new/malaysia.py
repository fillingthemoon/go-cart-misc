import settings
import handlers.base_handler
import csv

class CartogramHandler(handlers.base_handler.BaseCartogramHandler):

    def get_name(self):
        return "Malaysia"

    def get_gen_file(self):
        return "{}/mys_processedmap.json".format(settings.CARTOGRAM_DATA_DIR)
    
    def validate_values(self, values):

        if len(values) != 16:
            return False
        
        for v in values:
            if type(v) != float:
                return False

        return True
    
    def gen_area_data(self, values):
        return """cartogram_id,Region Data,Region Name,Inset\n
1,{},Johor,L\n
2,{},Kedah,L\n
3,{},Kelantan,L\n
4,{},Kuala Lumpur,L\n
5,{},Labuan,L\n
6,{},Melaka,L\n
7,{},Negeri Sembilan,L\n
8,{},Pahang,R\n
9,{},Perak,R\n
10,{},Perlis,R\n
11,{},Pulau Pinang,R\n
12,{},Putrajaya,R\n
13,{},Sabah,R\n
14,{},Sarawak,R\n
15,{},Selangor,R\n
16,{},Terengganu,R\n""".format(*values)
    
    def expect_geojson_output(self):
        return True

    def csv_to_area_string_and_colors(self, csvfile):

        return self.order_by_example(csv.reader(csvfile), "State/Federal Territory", 0, 1, 2, 3, ["Johor","Kedah","Kelantan","Kuala Lumpur","Labuan","Melaka","Negeri Sembilan","Pahang","Perak","Perlis","Pulau Pinang","Putrajaya","Sabah","Sarawak","Selangor","Terengganu"], [0.0 for i in range(0,16)], {"Johor":"1","Kedah":"2","Kelantan":"3","Kuala Lumpur":"4","Labuan":"5","Melaka":"6","Negeri Sembilan":"7","Pahang":"8","Perak":"9","Perlis":"10","Pulau Pinang":"11","Putrajaya":"12","Sabah":"13","Sarawak":"14","Selangor":"15","Terengganu":"16"})
