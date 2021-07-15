import settings
import handlers.base_handler
import csv

class CartogramHandler(handlers.base_handler.BaseCartogramHandler):

    def get_name(self):
        return "Mongolia"

    def get_gen_file(self):
        return "{}/mng_processedmap.json".format(settings.CARTOGRAM_DATA_DIR)
    
    def validate_values(self, values):

        if len(values) != 22:
            return False
        
        for v in values:
            if type(v) != float:
                return False

        return True
    
    def gen_area_data(self, values):
        return """cartogram_id,Region Data,Region Name,Inset\n
1,{},Arhangay,L\n
2,{},Bayan-Olgii,L\n
3,{},Bayankhongor,L\n
4,{},Bulgan,L\n
5,{},Darkhan-Uul,L\n
6,{},Dornod,L\n
7,{},Dornogovi,L\n
8,{},Dundgovi,L\n
9,{},Zavkhan,L\n
10,{},Govi-Altai,L\n
11,{},Govisumber,R\n
12,{},Khentii,R\n
13,{},Khovd,R\n
14,{},Khovsgol,R\n
15,{},Omnogovi,R\n
16,{},Orkhon,R\n
17,{},Ovorkhangai,R\n
18,{},Selenge,R\n
19,{},Sukhbaatar,R\n
20,{},Tov,R\n
21,{},Ulaanbaatar,R\n
22,{},Uvs,R\n""".format(*values)
    
    def expect_geojson_output(self):
        return True

    def csv_to_area_string_and_colors(self, csvfile):

        return self.order_by_example(csv.reader(csvfile), "Province", 0, 1, 2, 3, ["Arhangay","Bayan-Olgii","Bayankhongor","Bulgan","Darkhan-Uul","Dornod","Dornogovi","Dundgovi","Zavkhan","Govi-Altai","Govisumber","Khentii","Khovd","Khovsgol","Omnogovi","Orkhon","Ovorkhangai","Selenge","Sukhbaatar","Tov","Ulaanbaatar","Uvs"], [0.0 for i in range(0,22)], {"Arhangay":"1","Bayan-Olgii":"2","Bayankhongor":"3","Bulgan":"4","Darkhan-Uul":"5","Dornod":"6","Dornogovi":"7","Dundgovi":"8","Zavkhan":"9","Govi-Altai":"10","Govisumber":"11","Khentii":"12","Khovd":"13","Khovsgol":"14","Omnogovi":"15","Orkhon":"16","Ovorkhangai":"17","Selenge":"18","Sukhbaatar":"19","Tov":"20","Ulaanbaatar":"21","Uvs":"22"})
