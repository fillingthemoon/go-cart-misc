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
        return """cartogram_id,Region Data,Region Name,Inset
1,{},Buenos Aires,L
2,{},Catamarca,L
3,{},Chaco,L
4,{},Chubut,L
5,{},Ciudad de Buenos Aires,L
6,{},Cordoba,L
7,{},Corrientes,L
8,{},Entre Rios,L
9,{},Formosa,L
10,{},Jujuy,L
11,{},La Pampa,L
12,{},La Rioja,R
13,{},Mendoza,R
14,{},Misiones,R
15,{},Neuquen,R
16,{},Rio Negro,R
17,{},Salta,R
18,{},San Juan,R
19,{},San Luis,R
20,{},Santa Cruz,R
21,{},Santa Fe,R
22,{},Santiago del Estero,R
23,{},Tierra del Fuego,R
24,{},Tucuman,R""".format(*values)
    
    def expect_geojson_output(self):
        return True

    def csv_to_area_string_and_colors(self, csvfile):

        return self.order_by_example(csv.reader(csvfile), "Region", 0, 1, 2, 3, ["Buenos Aires","Catamarca","Chaco","Chubut","Ciudad de Buenos Aires","Cordoba","Corrientes","Entre Rios","Formosa","Jujuy","La Pampa","La Rioja","Mendoza","Misiones","Neuquen","Rio Negro","Salta","San Juan","San Luis","Santa Cruz","Santa Fe","Santiago del Estero","Tierra del Fuego","Tucuman"], [0.0 for i in range(0,24)], {"Buenos Aires":"1","Catamarca":"2","Chaco":"3","Chubut":"4","Ciudad de Buenos Aires":"5","Cordoba":"6","Corrientes":"7","Entre Rios":"8","Formosa":"9","Jujuy":"10","La Pampa":"11","La Rioja":"12","Mendoza":"13","Misiones":"14","Neuquen":"15","Rio Negro":"16","Salta":"17","San Juan":"18","San Luis":"19","Santa Cruz":"20","Santa Fe":"21","Santiago del Estero":"22","Tierra del Fuego":"23","Tucuman":"24"})
