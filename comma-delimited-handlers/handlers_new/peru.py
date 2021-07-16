import settings
import handlers.base_handler
import csv

class CartogramHandler(handlers.base_handler.BaseCartogramHandler):

    def get_name(self):
        return "Peru"

    def get_gen_file(self):
        return "{}/per_processedmap.json".format(settings.CARTOGRAM_DATA_DIR)
    
    def validate_values(self, values):

        if len(values) != 26:
            return False
        
        for v in values:
            if type(v) != float:
                return False

        return True
    
    def gen_area_data(self, values):
        return """cartogram_id,Region Data,Region Name,Inset
1,{},Amazonas,L
2,{},Ancash,L
3,{},Apurimac,L
4,{},Arequipa,L
5,{},Ayacucho,L
6,{},Cajamarca,L
7,{},Callao,L
8,{},Cusco,L
9,{},Huancavelica,L
10,{},Huanuco,L
11,{},Ica,L
12,{},Junin,L
13,{},La Libertad,R
14,{},Lambayeque,R
15,{},Lima,R
16,{},Lima Province,R
17,{},Loreto,R
18,{},Madre de Dios,R
19,{},Moquegua,R
20,{},Pasco,R
21,{},Piura,R
22,{},Puno,R
23,{},San Martin,R
24,{},Tacna,R
25,{},Tumbes,R
26,{},Ucayali,R""".format(*values)
    
    def expect_geojson_output(self):
        return True

    def csv_to_area_string_and_colors(self, csvfile):

        return self.order_by_example(csv.reader(csvfile), "Region/Province", 0, 1, 2, 3, ["Amazonas","Ancash","Apurimac","Arequipa","Ayacucho","Cajamarca","Callao","Cusco","Huancavelica","Huanuco","Ica","Junin","La Libertad","Lambayeque","Lima","Lima Province","Loreto","Madre de Dios","Moquegua","Pasco","Piura","Puno","San Martin","Tacna","Tumbes","Ucayali"], [0.0 for i in range(0,26)], {"Amazonas":"1","Ancash":"2","Apurimac":"3","Arequipa":"4","Ayacucho":"5","Cajamarca":"6","Callao":"7","Cusco":"8","Huancavelica":"9","Huanuco":"10","Ica":"11","Junin":"12","La Libertad":"13","Lambayeque":"14","Lima":"15","Lima Province":"16","Loreto":"17","Madre de Dios":"18","Moquegua":"19","Pasco":"20","Piura":"21","Puno":"22","San Martin":"23","Tacna":"24","Tumbes":"25","Ucayali":"26"})
