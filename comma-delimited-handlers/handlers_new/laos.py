import settings
import handlers.base_handler
import csv
class CartogramHandler(handlers.base_handler.BaseCartogramHandler):
    def get_name(self):
        return "Laos"
    def get_gen_file(self):
        return "{}/lao_processedmap.json".format(settings.CARTOGRAM_DATA_DIR)
    
    def validate_values(self, values):
        if len(values) != 18:
            return False
        
        for v in values:
            if type(v) != float:
                return False
        return True
    
    def gen_area_data(self, values):
        return """cartogram_id,Region Data,Region Name,Inset\n
1,{},Attapeu,L\n
2,{},Bokeo,L\n
3,{},Borikhamxai,L\n
4,{},Champasak,L\n
5,{},Houaphanh,L\n
6,{},Khammouane,L\n
7,{},Luang Namtha,L\n
8,{},Luang Prabang,L\n
9,{},Oudomxay,R\n
10,{},Phongsaly,R\n
11,{},Salavan,R\n
12,{},Savannakhet,R\n
13,{},Vientiane [Prefecture],R\n
14,{},Vientiane,R\n
15,{},Xaignabouli,R\n
16,{},Xaisomboun,R\n
17,{},Sekong,R\n
18,{},Xiangkhouang,R\n""".format(*values)
    
    def expect_geojson_output(self):
        return True
    def csv_to_area_string_and_colors(self, csvfile):
        return self.order_by_example(csv.reader(csvfile), "Province", 0, 1, 2, 3, ["Attapeu","Bokeo","Borikhamxai","Champasak","Houaphanh","Khammouane","Luang Namtha","Luang Prabang","Oudomxay","Phongsaly","Salavan","Savannakhet","Vientiane [Prefecture]","Vientiane","Xaignabouli","Xaisomboun","Sekong","Xiangkhouang"], [0.0 for i in range(0,18)], {"Attapeu":"1","Bokeo":"2","Borikhamxai":"3","Champasak":"4","Houaphanh":"5","Khammouane":"6","Luang Namtha":"7","Luang Prabang":"8","Oudomxay":"9","Phongsaly":"10","Salavan":"11","Savannakhet":"12","Vientiane [Prefecture]":"13","Vientiane":"14","Xaignabouli":"15","Xaisomboun":"16","Sekong":"17","Xiangkhouang":"18"})
