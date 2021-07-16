import settings
import handlers.base_handler
import csv

class CartogramHandler(handlers.base_handler.BaseCartogramHandler):

    def get_name(self):
        return "Sudan"

    def get_gen_file(self):
        return "{}/sdn_processedmap.json".format(settings.CARTOGRAM_DATA_DIR)
    
    def validate_values(self, values):

        if len(values) != 18:
            return False
        
        for v in values:
            if type(v) != float:
                return False

        return True
    
    def gen_area_data(self, values):
        return """cartogram_id,Region Data,Region Name,Inset
1,{},Al Jazirah,L
2,{},Al Qadarif,L
3,{},Blue Nile,L
4,{},Central Darfur,L
5,{},East Darfur,L
6,{},Kassala,L
7,{},Khartoum,L
8,{},North Darfur,L
9,{},North Kurdufan,R
10,{},Northern,R
11,{},Red Sea,R
12,{},River Nile,R
13,{},Sennar,R
14,{},South Darfur,R
15,{},South Kurdufan,R
16,{},West Darfur,R
17,{},West Kurdufan,R
18,{},White Nile,R""".format(*values)
    
    def expect_geojson_output(self):
        return True

    def csv_to_area_string_and_colors(self, csvfile):

        return self.order_by_example(csv.reader(csvfile), "State", 0, 1, 2, 3, ["Al Jazirah","Al Qadarif","Blue Nile","Central Darfur","East Darfur","Kassala","Khartoum","North Darfur","North Kurdufan","Northern","Red Sea","River Nile","Sennar","South Darfur","South Kurdufan","West Darfur","West Kurdufan","White Nile"], [0.0 for i in range(0,18)], {"Al Jazirah":"1","Al Qadarif":"2","Blue Nile":"3","Central Darfur":"4","East Darfur":"5","Kassala":"6","Khartoum":"7","North Darfur":"8","North Kurdufan":"9","Northern":"10","Red Sea":"11","River Nile":"12","Sennar":"13","South Darfur":"14","South Kurdufan":"15","West Darfur":"16","West Kurdufan":"17","White Nile":"18"})
