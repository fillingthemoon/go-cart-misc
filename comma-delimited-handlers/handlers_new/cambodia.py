import settings
import handlers.base_handler
import csv

class CartogramHandler(handlers.base_handler.BaseCartogramHandler):

    def get_name(self):
        return "Cambodia"

    def get_gen_file(self):
        return "{}/cam_processedmap.json".format(settings.CARTOGRAM_DATA_DIR)
    
    def validate_values(self, values):

        if len(values) != 25:
            return False
        
        for v in values:
            if type(v) != float:
                return False

        return True
    
    def gen_area_data(self, values):
        return """cartogram_id,Region Data,Region Name,Inset\n
1,{},Banteay Meanchey,L\n
2,{},Battambang,L\n
3,{},Kampong Cham,L\n
4,{},Kampong Chhnang,L\n
5,{},Kampong Speu,L\n
6,{},Kampong Thom,L\n
7,{},Kampot,L\n
8,{},Kandal,L\n
9,{},Koh Kong,L\n
10,{},Kep,L\n
11,{},Kratie,L\n
12,{},Pailin,L\n
13,{},Preah Sihanouk,R\n
14,{},Mondul Kiri,R\n
15,{},Otdar Meanchey,R\n
16,{},Phnom Penh,R\n
17,{},Pursat,R\n
18,{},Preah Vihear,R\n
19,{},Prey Veng,R\n
20,{},Ratanak Kiri,R\n
21,{},Siem Reap,R\n
22,{},Stung Treng,R\n
23,{},Svay Rieng,R\n
24,{},Takeo,R\n
25,{},Tbong Khmum,R\n""".format(*values)
    
    def expect_geojson_output(self):
        return True

    def csv_to_area_string_and_colors(self, csvfile):

        return self.order_by_example(csv.reader(csvfile), "Province", 0, 1, 2, 3, ["Banteay Meanchey","Battambang","Kampong Cham","Kampong Chhnang","Kampong Speu","Kampong Thom","Kampot","Kandal","Koh Kong","Kep","Kratie","Pailin","Preah Sihanouk","Mondul Kiri","Otdar Meanchey","Phnom Penh","Pursat","Preah Vihear","Prey Veng","Ratanak Kiri","Siem Reap","Stung Treng","Svay Rieng","Takeo","Tbong Khmum"], [0.0 for i in range(0,25)], {"Banteay Meanchey":"1","Battambang":"2","Kampong Cham":"3","Kampong Chhnang":"4","Kampong Speu":"5","Kampong Thom":"6","Kampot":"7","Kandal":"8","Koh Kong":"9","Kep":"10","Kratie":"11","Pailin":"12","Preah Sihanouk":"13","Mondul Kiri":"14","Otdar Meanchey":"15","Phnom Penh":"16","Pursat":"17","Preah Vihear":"18","Prey Veng":"19","Ratanak Kiri":"20","Siem Reap":"21","Stung Treng":"22","Svay Rieng":"23","Takeo":"24","Tbong Khmum":"25"})
