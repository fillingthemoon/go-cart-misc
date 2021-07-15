import settings
import handlers.base_handler
import csv

class CartogramHandler(handlers.base_handler.BaseCartogramHandler):

    def get_name(self):
        return "Poland"

    def get_gen_file(self):
        return "{}/pol_processedmap.json".format(settings.CARTOGRAM_DATA_DIR)
    
    def validate_values(self, values):

        if len(values) != 16:
            return False
        
        for v in values:
            if type(v) != float:
                return False

        return True
    
    def gen_area_data(self, values):
        return """cartogram_id,Region Data,Region Name,Inset\n
15,{},Greater Poland	,L\n
13,{},Holy Cross,L\n
2,{},Kuyavian-Pomeranian,L\n
6,{},Lesser Poland,L\n
3,{},Lodz,L\n
1,{},Lower Silesian,L\n
4,{},Lublin,L\n
5,{},Lubusz,R\n
7,{},Masovian,R\n
8,{},Opole,R\n
10,{},Podlaskie,R\n
11,{},Pomeranian,R\n
12,{},Silesian,R\n
9,{},Subcarpathian,R\n
14,{},Warmian-Masurian,R\n
16,{},West Pomeranian,R\n""".format(*values)
    
    def expect_geojson_output(self):
        return True

    def csv_to_area_string_and_colors(self, csvfile):

        return self.order_by_example(csv.reader(csvfile), "Region", 0, 1, 2, 3, ["Greater Poland","Holy Cross","Kuyavian-Pomeranian","Lesser Poland","Lodz","Lower Silesian","Lublin","Lubusz","Masovian","Opole","Podlaskie","Pomeranian","Silesian","Subcarpathian","Warmian-Masurian","West Pomeranian"], [0.0 for i in range(0,16)], {"Greater Poland":"15","Holy Cross":"13","Kuyavian-Pomeranian":"2","Lesser Poland":"6","Lodz":"3","Lower Silesian":"1","Lublin":"4","Lubusz":"5","Masovian":"7","Opole":"8","Podlaskie":"10","Pomeranian":"11","Silesian":"12","Subcarpathian":"9","Warmian-Masurian":"14","West Pomeranian":"16"})
