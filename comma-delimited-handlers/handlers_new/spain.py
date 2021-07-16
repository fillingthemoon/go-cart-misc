import settings
import handlers.base_handler
import csv

class CartogramHandler(handlers.base_handler.BaseCartogramHandler):

    def get_name(self):
        return "Spain"

    def get_gen_file(self):
        return "{}/esp_processedmap.json".format(settings.CARTOGRAM_DATA_DIR)
    
    def validate_values(self, values):

        if len(values) != 18:
            return False
        
        for v in values:
            if type(v) != float:
                return False

        return True
    
    def gen_area_data(self, values):
        return """cartogram_id,Region Data,Region Name,Inset
1,{},Andalusia,L
2,{},Aragon,L
13,{},Balearic Islands,L
16,{},Basque Autonomous Community,L
14,{},Canary Islands,L
3,{},Cantabria,L
4,{},Castile and Leon,L
5,{},Castile-La Mancha,L
6,{},Catalonia,R
7,{},Ceuta y Melilla,R
9,{},Chartered Community of Navarre,R
8,{},Community of Madrid,R
11,{},Extremadura,R
12,{},Galicia,R
15,{},La Rioja,R
17,{},Principality of Asturias,R
18,{},Region of Murcia,R
10,{},Valencian Community,R""".format(*values)
    
    def expect_geojson_output(self):
        return True

    def csv_to_area_string_and_colors(self, csvfile):

        return self.order_by_example(csv.reader(csvfile), "Regions", 0, 1, 2, 3, ["Andalusia","Aragon","Balearic Islands","Basque Autonomous Community","Canary Islands","Cantabria","Castile and Leon","Castile-La Mancha","Catalonia","Ceuta y Melilla","Chartered Community of Navarre","Community of Madrid","Extremadura","Galicia","La Rioja","Principality of Asturias","Region of Murcia","Valencian Community"], [0.0 for i in range(0,18)], {"Andalusia":"1","Aragon":"2","Balearic Islands":"13","Basque Autonomous Community":"16","Canary Islands":"14","Cantabria":"3","Castile and Leon":"4","Castile-La Mancha":"5","Catalonia":"6","Ceuta y Melilla":"7","Chartered Community of Navarre":"9","Community of Madrid":"8","Extremadura":"11","Galicia":"12","La Rioja":"15","Principality of Asturias":"17","Region of Murcia":"18","Valencian Community":"10"})
