import settings
import handlers.base_handler
import csv

class CartogramHandler(handlers.base_handler.BaseCartogramHandler):

    def get_name(self):
        return "Libya"

    def get_gen_file(self):
        return "{}/lby_processedmap.json".format(settings.CARTOGRAM_DATA_DIR)
    
    def validate_values(self, values):

        if len(values) != 22:
            return False
        
        for v in values:
            if type(v) != float:
                return False

        return True
    
    def gen_area_data(self, values):
        return """cartogram_id,Region Data,Region Name,Inset\n
1,{},Al Butnan,L\n
2,{},Al Jabal al Akhdar,L\n
3,{},Al Jabal al Gharbi,L\n
4,{},Al Jifarah,L\n
5,{},Al Jufrah,L\n
6,{},Al Kufrah,L\n
7,{},Al Marj,L\n
8,{},Al Marqab,L\n
9,{},Al Wahat,L\n
10,{},An Nuqat al Khams,L\n
11,{},Az Zawiyah,R\n
12,{},Benghazi,R\n
13,{},Darnah,R\n
14,{},Ghat,R\n
15,{},Misratah,R\n
16,{},Murzuq,R\n
17,{},Nalut,R\n
18,{},Sabha,R\n
19,{},Surt,R\n
20,{},Tripoli,R\n
21,{},Wadi al Hayat,R\n
22,{},Wadi ash Shati',R\n""".format(*values)
    
    def expect_geojson_output(self):
        return True

    def csv_to_area_string_and_colors(self, csvfile):

        return self.order_by_example(csv.reader(csvfile), "District", 0, 1, 2, 3, ["Al Butnan","Al Jabal al Akhdar","Al Jabal al Gharbi","Al Jifarah","Al Jufrah","Al Kufrah","Al Marj","Al Marqab","Al Wahat","An Nuqat al Khams","Az Zawiyah","Benghazi","Darnah","Ghat","Misratah","Murzuq","Nalut","Sabha","Surt","Tripoli","Wadi al Hayat","Wadi ash Shati'"], [0.0 for i in range(0,22)], {"Al Butnan":"1","Al Jabal al Akhdar":"2","Al Jabal al Gharbi":"3","Al Jifarah":"4","Al Jufrah":"5","Al Kufrah":"6","Al Marj":"7","Al Marqab":"8","Al Wahat":"9","An Nuqat al Khams":"10","Az Zawiyah":"11","Benghazi":"12","Darnah":"13","Ghat":"14","Misratah":"15","Murzuq":"16","Nalut":"17","Sabha":"18","Surt":"19","Tripoli":"20","Wadi al Hayat":"21","Wadi ash Shati'":"22"})
