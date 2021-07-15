import settings
import handlers.base_handler
import csv

class CartogramHandler(handlers.base_handler.BaseCartogramHandler):

    def get_name(self):
        return "Portugal"

    def get_gen_file(self):
        return "{}/prt_processedmap.json".format(settings.CARTOGRAM_DATA_DIR)
    
    def validate_values(self, values):

        if len(values) != 18:
            return False
        
        for v in values:
            if type(v) != float:
                return False

        return True
    
    def gen_area_data(self, values):
        return """cartogram_id,Region Data,Region Name,Inset\n
1,{},Aveiro,L\n
2,{},Beja,L\n
3,{},Braga,L\n
4,{},Braganca,L\n
5,{},Castelo Branco,L\n
6,{},Coimbra,L\n
7,{},Evora,L\n
8,{},Faro,L\n
9,{},Guarda,R\n
10,{},Leiria,R\n
11,{},Lisboa,R\n
12,{},Portalegre,R\n
13,{},Porto,R\n
14,{},Santarem,R\n
15,{},Setubal,R\n
16,{},Viana do Castelo,R\n
17,{},Vila Real,R\n
18,{},Viseu,R\n""".format(*values)
    
    def expect_geojson_output(self):
        return True

    def csv_to_area_string_and_colors(self, csvfile):

        return self.order_by_example(csv.reader(csvfile), "District", 0, 1, 2, 3, ["Aveiro","Beja","Braga","Braganca","Castelo Branco","Coimbra","Evora","Faro","Guarda","Leiria","Lisboa","Portalegre","Porto","Santarem","Setubal","Viana do Castelo","Vila Real","Viseu"], [0.0 for i in range(0,18)], {"Aveiro":"1","Beja":"2","Braga":"3","Braganca":"4","Castelo Branco":"5","Coimbra":"6","Evora":"7","Faro":"8","Guarda":"9","Leiria":"10","Lisboa":"11","Portalegre":"12","Porto":"13","Santarem":"14","Setubal":"15","Viana do Castelo":"16","Vila Real":"17","Viseu":"18"})
