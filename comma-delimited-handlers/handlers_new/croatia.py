import settings
import handlers.base_handler
import csv

class CartogramHandler(handlers.base_handler.BaseCartogramHandler):

    def get_name(self):
        return "Croatia"

    def get_gen_file(self):
        return "{}/hrv_processedmap.json".format(settings.CARTOGRAM_DATA_DIR)
    
    def validate_values(self, values):

        if len(values) != 21:
            return False
        
        for v in values:
            if type(v) != float:
                return False

        return True
    
    def gen_area_data(self, values):
        return """cartogram_id,Region Data,Region Name,Inset\n
1,{},Bjelovar-Bilogora,L\n
2,{},Brod-Posavina,L\n
3,{},Dubrovnik-Neretva,L\n
4,{},City of Zagreb,L\n
5,{},Istria,L\n
6,{},Karlovac,L\n
7,{},Koprivnica-Krizevci,L\n
8,{},Krapina-Zagorje,L\n
9,{},Lika-Senj,L\n
10,{},Medimurje,L\n
11,{},Osijek-Baranja,R\n
12,{},Pozega-Slavonia,R\n
13,{},Primorje-Gorski Kotar,R\n
14,{},Sibenik-Knin,R\n
15,{},Sisak-Moslavina,R\n
16,{},Split-Dalmatia,R\n
17,{},Varazdin,R\n
18,{},Virovitica-Podravina,R\n
19,{},Vukovar-Srijem,R\n
20,{},Zadar,R\n
21,{},Zagreb County,R\n""".format(*values)
    
    def expect_geojson_output(self):
        return True

    def csv_to_area_string_and_colors(self, csvfile):

        return self.order_by_example(csv.reader(csvfile), "Region", 0, 1, 2, 3, ["Bjelovar-Bilogora","Brod-Posavina","Dubrovnik-Neretva","City of Zagreb","Istria","Karlovac","Koprivnica-Krizevci","Krapina-Zagorje","Lika-Senj","Medimurje","Osijek-Baranja","Pozega-Slavonia","Primorje-Gorski Kotar","Sibenik-Knin","Sisak-Moslavina","Split-Dalmatia","Varazdin","Virovitica-Podravina","Vukovar-Srijem","Zadar","Zagreb County"], [0.0 for i in range(0,21)], {"Bjelovar-Bilogora":"1","Brod-Posavina":"2","Dubrovnik-Neretva":"3","City of Zagreb":"4","Istria":"5","Karlovac":"6","Koprivnica-Krizevci":"7","Krapina-Zagorje":"8","Lika-Senj":"9","Medimurje":"10","Osijek-Baranja":"11","Pozega-Slavonia":"12","Primorje-Gorski Kotar":"13","Sibenik-Knin":"14","Sisak-Moslavina":"15","Split-Dalmatia":"16","Varazdin":"17","Virovitica-Podravina":"18","Vukovar-Srijem":"19","Zadar":"20","Zagreb County":"21"})
