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
        return """cartogram_id,Region Data,Region Name,Inset\n
1,{},Amazonas,L\n
2,{},Ancash,L\n
3,{},Apurimac,L\n
4,{},Arequipa,L\n
5,{},Ayacucho,L\n
6,{},Cajamarca,L\n
7,{},Callao,L\n
8,{},Cusco,L\n
9,{},Huancavelica,L\n
10,{},Huanuco,L\n
11,{},Ica,L\n
12,{},Junin,L\n
13,{},La Libertad,R\n
14,{},Lambayeque,R\n
15,{},Lima,R\n
16,{},Lima Province,R\n
17,{},Loreto,R\n
18,{},Madre de Dios,R\n
19,{},Moquegua,R\n
20,{},Pasco,R\n
21,{},Piura,R\n
22,{},Puno,R\n
23,{},San Martin,R\n
24,{},Tacna,R\n
25,{},Tumbes,R\n
26,{},Ucayali,R\n""".format(*values)
    
    def expect_geojson_output(self):
        return True

    def csv_to_area_string_and_colors(self, csvfile):

        return self.order_by_example(csv.reader(csvfile), "Region/Province", 0, 1, 2, 3, ["Amazonas","Ancash","Apurimac","Arequipa","Ayacucho","Cajamarca","Callao","Cusco","Huancavelica","Huanuco","Ica","Junin","La Libertad","Lambayeque","Lima","Lima Province","Loreto","Madre de Dios","Moquegua","Pasco","Piura","Puno","San Martin","Tacna","Tumbes","Ucayali"], [0.0 for i in range(0,26)], {"Amazonas":"1","Ancash":"2","Apurimac":"3","Arequipa":"4","Ayacucho":"5","Cajamarca":"6","Callao":"7","Cusco":"8","Huancavelica":"9","Huanuco":"10","Ica":"11","Junin":"12","La Libertad":"13","Lambayeque":"14","Lima":"15","Lima Province":"16","Loreto":"17","Madre de Dios":"18","Moquegua":"19","Pasco":"20","Piura":"21","Puno":"22","San Martin":"23","Tacna":"24","Tumbes":"25","Ucayali":"26"})
