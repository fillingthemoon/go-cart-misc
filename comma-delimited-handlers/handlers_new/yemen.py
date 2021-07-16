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
        return """cartogram_id,Region Data,Region Name,Inset
1,{},Aden,L
2,{},Abyan,L
3,{},Al Bayda',L
4,{},Ad Dali,L
5,{},Al Hudaydah,L
6,{},Al Jawf,L
7,{},Al Mahrah,L
8,{},Al Mahwit,L
9,{},Amanat Al Asimah,L
10,{},'Amran,L
11,{},Dhamar,R
12,{},Hadramawt,R
13,{},Hajjah,R
14,{},Ibb,R
15,{},Lahij,R
16,{},Ma'rib,R
17,{},Raymah,R
18,{},Sa'dah,R
19,{},Sana'a,R
20,{},Shabwah,R
21,{},Socotra,R
22,{},Ta'izz,R""".format(*values)
    
    def expect_geojson_output(self):
        return True

    def csv_to_area_string_and_colors(self, csvfile):

        return self.order_by_example(csv.reader(csvfile), "Governorate", 0, 1, 2, 3, ["Aden","Abyan","Al Bayda'","Ad Dali","Al Hudaydah","Al Jawf","Al Mahrah","Al Mahwit","Amanat Al Asimah","'Amran","Dhamar","Hadramawt","Hajjah","Ibb","Lahij","Ma'rib","Raymah","Sa'dah","Sana'a","Shabwah","Socotra","Ta'izz"], [0.0 for i in range(0,22)], {"Aden":"1","Abyan":"2","Al Bayda'":"3","Ad Dali":"4","Al Hudaydah":"5","Al Jawf":"6","Al Mahrah":"7","Al Mahwit":"8","Amanat Al Asimah":"9","'Amran":"10","Dhamar":"11","Hadramawt":"12","Hajjah":"13","Ibb":"14","Lahij":"15","Ma'rib":"16","Raymah":"17","Sa'dah":"18","Sana'a":"19","Shabwah":"20","Socotra":"21","Ta'izz":"22"})
