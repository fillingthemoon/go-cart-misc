import settings
import handlers.base_handler
import csv

class CartogramHandler(handlers.base_handler.BaseCartogramHandler):

    def get_name(self):
        return "Argentina"

    def get_gen_file(self):
        return "{}/arg_processedmap.json".format(settings.CARTOGRAM_DATA_DIR)
    
    def validate_values(self, values):

        if len(values) != 24:
            return False
        
        for v in values:
            if type(v) != float:
                return False

        return True
    
    def gen_area_data(self, values):
        return """cartogram_id,Region Data,Region Name,Inset\n
1,{},Buenos Aires,L\n
2,{},Catamarca,L\n
3,{},Chaco,L\n
4,{},Chubut,L\n
5,{},Ciudad de Buenos Aires,L\n
6,{},Cordoba,L\n
7,{},Corrientes,L\n
8,{},Entre Rios,L\n
9,{},Formosa,L\n
10,{},Jujuy,L\n
11,{},La Pampa,L\n
12,{},La Rioja,R\n
13,{},Mendoza,R\n
14,{},Misiones,R\n
15,{},Neuquen,R\n
16,{},Rio Negro,R\n
17,{},Salta,R\n
18,{},San Juan,R\n
19,{},San Luis,R\n
20,{},Santa Cruz,R\n
21,{},Santa Fe,R\n
22,{},Santiago del Estero,R\n
23,{},Tierra del Fuego,R\n
24,{},Tucuman,R\n""".format(*values)
    
    def expect_geojson_output(self):
        return True

    def csv_to_area_string_and_colors(self, csvfile):

        return self.order_by_example(csv.reader(csvfile), "Region", 0, 1, 2, 3, ["Buenos Aires","Catamarca","Chaco","Chubut","Ciudad de Buenos Aires","Cordoba","Corrientes","Entre Rios","Formosa","Jujuy","La Pampa","La Rioja","Mendoza","Misiones","Neuquen","Rio Negro","Salta","San Juan","San Luis","Santa Cruz","Santa Fe","Santiago del Estero","Tierra del Fuego","Tucuman"], [0.0 for i in range(0,24)], {"Buenos Aires":"1","Catamarca":"2","Chaco":"3","Chubut":"4","Ciudad de Buenos Aires":"5","Cordoba":"6","Corrientes":"7","Entre Rios":"8","Formosa":"9","Jujuy":"10","La Pampa":"11","La Rioja":"12","Mendoza":"13","Misiones":"14","Neuquen":"15","Rio Negro":"16","Salta":"17","San Juan":"18","San Luis":"19","Santa Cruz":"20","Santa Fe":"21","Santiago del Estero":"22","Tierra del Fuego":"23","Tucuman":"24"})
