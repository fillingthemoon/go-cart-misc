import settings
import handlers.base_handler
import csv

class CartogramHandler(handlers.base_handler.BaseCartogramHandler):

    def get_name(self):
        return "Hungary"

    def get_gen_file(self):
        return "{}/hun_processedmap.json".format(settings.CARTOGRAM_DATA_DIR)
    
    def validate_values(self, values):

        if len(values) != 20:
            return False
        
        for v in values:
            if type(v) != float:
                return False

        return True
    
    def gen_area_data(self, values):
        return """cartogram_id,Region Data,Region Name,Inset\n
1,{},Bacs-Kiskun,L\n
2,{},Baranya,L\n
3,{},Bekes,L\n
4,{},Borsod-Abauj-Zemplen,L\n
5,{},Budapest,L\n
6,{},Csongrad,L\n
7,{},Fejer,L\n
8,{},Gyor-Moson-Sopron,L\n
9,{},Hajdu-Bihar,L\n
10,{},Heves,R\n
11,{},Jasz-Nagykun-Szolnok,R\n
12,{},Komarom-Esztergom,R\n
13,{},Nograd,R\n
14,{},Pest,R\n
15,{},Somogy,R\n
16,{},Szabolcs-Szatmar-Bereg,R\n
17,{},Tolna,R\n
18,{},Vas,R\n
19,{},Veszprem,R\n
20,{},Zala,R\n""".format(*values)
    
    def expect_geojson_output(self):
        return True

    def csv_to_area_string_and_colors(self, csvfile):

        return self.order_by_example(csv.reader(csvfile), "Region", 0, 1, 2, 3, ["Bacs-Kiskun","Baranya","Bekes","Borsod-Abauj-Zemplen","Budapest","Csongrad","Fejer","Gyor-Moson-Sopron","Hajdu-Bihar","Heves","Jasz-Nagykun-Szolnok","Komarom-Esztergom","Nograd","Pest","Somogy","Szabolcs-Szatmar-Bereg","Tolna","Vas","Veszprem","Zala"], [0.0 for i in range(0,20)], {"Bacs-Kiskun":"1","Baranya":"2","Bekes":"3","Borsod-Abauj-Zemplen":"4","Budapest":"5","Csongrad":"6","Fejer":"7","Gyor-Moson-Sopron":"8","Hajdu-Bihar":"9","Heves":"10","Jasz-Nagykun-Szolnok":"11","Komarom-Esztergom":"12","Nograd":"13","Pest":"14","Somogy":"15","Szabolcs-Szatmar-Bereg":"16","Tolna":"17","Vas":"18","Veszprem":"19","Zala":"20"})
