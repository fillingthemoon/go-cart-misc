import settings
import handlers.base_handler
import csv

class CartogramHandler(handlers.base_handler.BaseCartogramHandler):

    def get_name(self):
        return "Yemen"

    def get_gen_file(self):
        return "{}/yem_processedmap.json".format(settings.CARTOGRAM_DATA_DIR)
    
    def validate_values(self, values):

        if len(values) != 22:
            return False
        
        for v in values:
            if type(v) != float:
                return False

        return True
    
    def gen_area_data(self, values):
        return """cartogram_id,Region Data,Region Name,Inset\n
1,{},Aden,L\n
2,{},Abyan,L\n
3,{},Al Bayda',L\n
4,{},Ad Dali,L\n
5,{},Al Hudaydah,L\n
6,{},Al Jawf,L\n
7,{},Al Mahrah,L\n
8,{},Al Mahwit,L\n
9,{},Amanat Al Asimah,L\n
10,{},'Amran,L\n
11,{},Dhamar,R\n
12,{},Hadramawt,R\n
13,{},Hajjah,R\n
14,{},Ibb,R\n
15,{},Lahij,R\n
16,{},Ma'rib,R\n
17,{},Raymah,R\n
18,{},Sa'dah,R\n
19,{},Sana'a,R\n
20,{},Shabwah,R\n
21,{},Socotra,R\n
22,{},Ta'izz,R\n""".format(*values)
    
    def expect_geojson_output(self):
        return True

    def csv_to_area_string_and_colors(self, csvfile):

        return self.order_by_example(csv.reader(csvfile), "Governorate", 0, 1, 2, 3, ["Aden","Abyan","Al Bayda'","Ad Dali","Al Hudaydah","Al Jawf","Al Mahrah","Al Mahwit","Amanat Al Asimah","'Amran","Dhamar","Hadramawt","Hajjah","Ibb","Lahij","Ma'rib","Raymah","Sa'dah","Sana'a","Shabwah","Socotra","Ta'izz"], [0.0 for i in range(0,22)], {"Aden":"1","Abyan":"2","Al Bayda'":"3","Ad Dali":"4","Al Hudaydah":"5","Al Jawf":"6","Al Mahrah":"7","Al Mahwit":"8","Amanat Al Asimah":"9","'Amran":"10","Dhamar":"11","Hadramawt":"12","Hajjah":"13","Ibb":"14","Lahij":"15","Ma'rib":"16","Raymah":"17","Sa'dah":"18","Sana'a":"19","Shabwah":"20","Socotra":"21","Ta'izz":"22"})
