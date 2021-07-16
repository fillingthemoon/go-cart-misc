import settings
import handlers.base_handler
import csv

class CartogramHandler(handlers.base_handler.BaseCartogramHandler):

    def get_name(self):
        return "South Korea"

    def get_gen_file(self):
        return "{}/southKorea2_processedmap.json".format(settings.CARTOGRAM_DATA_DIR)
    
    def validate_values(self, values):

        if len(values) != 17:
            return False
        
        for v in values:
            if type(v) != float:
                return False

        return True
    
    def gen_area_data(self, values):
        return """cartogram_id,Region Data,Region Name,Inset
1,{},Busan,L
2,{},Chungcheongbuk-do,L
3,{},Chungcheongnam-do,L
4,{},Daegu,L
5,{},Daejeon,L
6,{},Gangwon-do,L
7,{},Gwangju,L
8,{},Gyeonggi-do,L
9,{},Gyeongsangbuk-do,R
10,{},Gyeongsangnam-do,R
11,{},Incheon,R
12,{},Jeju,R
13,{},Jeollabuk-do,R
14,{},Jeollanam-do,R
15,{},Sejong,R
16,{},Seoul,R
17,{},Ulsan,R""".format(*values)
    
    def expect_geojson_output(self):
        return True

    def csv_to_area_string_and_colors(self, csvfile):

        return self.order_by_example(csv.reader(csvfile), "Province/City", 0, 1, 2, 3, ["Busan","Chungcheongbuk-do","Chungcheongnam-do","Daegu","Daejeon","Gangwon-do","Gwangju","Gyeonggi-do","Gyeongsangbuk-do","Gyeongsangnam-do","Incheon","Jeju","Jeollabuk-do","Jeollanam-do","Sejong","Seoul","Ulsan"], [0.0 for i in range(0,17)], {"Busan":"1","Chungcheongbuk-do":"2","Chungcheongnam-do":"3","Daegu":"4","Daejeon":"5","Gangwon-do":"6","Gwangju":"7","Gyeonggi-do":"8","Gyeongsangbuk-do":"9","Gyeongsangnam-do":"10","Incheon":"11","Jeju":"12","Jeollabuk-do":"13","Jeollanam-do":"14","Sejong":"15","Seoul":"16","Ulsan":"17"})
