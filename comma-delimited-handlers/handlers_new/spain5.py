import settings
import handlers.base_handler
import csv

class CartogramHandler(handlers.base_handler.BaseCartogramHandler):

    def get_name(self):
        return "Spain"

    def get_gen_file(self):
        return "{}/spain5_processedmap.json".format(settings.CARTOGRAM_DATA_DIR)
    
    def validate_values(self, values):

        if len(values) != 18:
            return False
        
        for v in values:
            if type(v) != float:
                return False

        return True
    
    def gen_area_data(self, values):
        return """cartogram_id,Region Data,Region Name,Inset\n
1,{},Andalucia,L\n
2,{},Aragon,L\n
3,{},Cantabria,L\n
4,{},Castilla y Leon,L\n
5,{},Castilla-La Mancha,L\n
6,{},Cataluna,L\n
7,{},Ceuta,L\n
8,{},Comunidad de Madrid,L\n
9,{},Comunidad Foral de Navarra,R\n
10,{},Comunidad Valenciana,R\n
11,{},Extremadura,R\n
12,{},Galicia,R\n
13,{},Islas Baleares,R\n
14,{},La Rioja,R\n
15,{},Melilla,R\n
16,{},Pais Vasco,R\n
17,{},Principado de Asturias,R\n
18,{},Region de Murcia,R\n""".format(*values)
    
    def expect_geojson_output(self):
        return True

    def csv_to_area_string_and_colors(self, csvfile):

        return self.order_by_example(csv.reader(csvfile), "Autonomous Community/City", 0, 1, 2, 3, ["Andalucia","Aragon","Cantabria","Castilla y Leon","Castilla-La Mancha","Cataluna","Ceuta","Comunidad de Madrid","Comunidad Foral de Navarra","Comunidad Valenciana","Extremadura","Galicia","Islas Baleares","La Rioja","Melilla","Pais Vasco","Principado de Asturias","Region de Murcia"], [0.0 for i in range(0,18)], {"Andalucia":"1","Aragon":"2","Cantabria":"3","Castilla y Leon":"4","Castilla-La Mancha":"5","Cataluna":"6","Ceuta":"7","Comunidad de Madrid":"8","Comunidad Foral de Navarra":"9","Comunidad Valenciana":"10","Extremadura":"11","Galicia":"12","Islas Baleares":"13","La Rioja":"14","Melilla":"15","Pais Vasco":"16","Principado de Asturias":"17","Region de Murcia":"18"})
