import settings
import handlers.base_handler
import csv
class CartogramHandler(handlers.base_handler.BaseCartogramHandler):
    def get_name(self):
        return "Paraguay"
    def get_gen_file(self):
        return "{}/pry_processedmap.json".format(settings.CARTOGRAM_DATA_DIR)
    
    def validate_values(self, values):
        if len(values) != 18:
            return False
        
        for v in values:
            if type(v) != float:
                return False
        return True
    
    def gen_area_data(self, values):
        return """cartogram_id,Region Data,Region Name,Inset\n
1,{},Alto Paraguay,L\n
2,{},Alto Parana,L\n
3,{},Amambay,L\n
4,{},Asuncion,L\n
5,{},Boqueron,L\n
6,{},Caaguazu,L\n
7,{},Caazapa,L\n
8,{},Canindeyu,L\n
9,{},Central,R\n
10,{},Concepcion,R\n
11,{},Cordillera,R\n
12,{},Guaira,R\n
13,{},Itapua,R\n
14,{},Misiones,R\n
15,{},Neembucu,R\n
16,{},Paraguari,R\n
17,{},Presidente Hayes,R\n
18,{},San Pedro,R\n""".format(*values)
    
    def expect_geojson_output(self):
        return True
    def csv_to_area_string_and_colors(self, csvfile):
        return self.order_by_example(csv.reader(csvfile), "Department", 0, 1, 2, 3, ["Alto Paraguay","Alto Parana","Amambay","Asuncion","Boqueron","Caaguazu","Caazapa","Canindeyu","Central","Concepcion","Cordillera","Guaira","Itapua","Misiones","Neembucu","Paraguari","Presidente Hayes","San Pedro"], [0.0 for i in range(0,18)], {"Alto Paraguay":"1","Alto Parana":"2","Amambay":"3","Asuncion":"4","Boqueron":"5","Caaguazu":"6","Caazapa":"7","Canindeyu":"8","Central":"9","Concepcion":"10","Cordillera":"11","Guaira":"12","Itapua":"13","Misiones":"14","Neembucu":"15","Paraguari":"16","Presidente Hayes":"17","San Pedro":"18"})
