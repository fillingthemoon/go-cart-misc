import settings
import handlers.base_handler
import csv

class CartogramHandler(handlers.base_handler.BaseCartogramHandler):

    def get_name(self):
        return "Colombia"

    def get_gen_file(self):
        return "{}/colombia_processedmap.json".format(settings.CARTOGRAM_DATA_DIR)
    
    def validate_values(self, values):

        if len(values) != 32:
            return False
        
        for v in values:
            if type(v) != float:
                return False

        return True
    
    def gen_area_data(self, values):
        return """cartogram_id,Region Data,Region Name,Inset
1,{},Amazonas,L
2,{},Antioquia,L
3,{},Arauca,L
4,{},Atlantico,L
5,{},Bolivar,L
6,{},Boyaca,L
7,{},Caldas,L
8,{},Caqueta,L
9,{},Casanare,L
10,{},Cauca,L
11,{},Cesar,L
12,{},Choco,L
13,{},Cordoba,L
14,{},Cundinamarca,L
15,{},Guainia,L
16,{},Guaviare,R
17,{},Huila,R
18,{},La Guajira,R
19,{},Magdalena,R
20,{},Meta,R
21,{},Narino,R
22,{},Norte de Santander,R
23,{},Putumayo,R
24,{},Quindio,R
25,{},Risaralda,R
26,{},San Andres y Providencia  ,R
27,{},Santander,R
28,{},Sucre,R
29,{},Tolima,R
30,{},Valle del Cauca,R
31,{},Vaupes,R
32,{},Vichada,R""".format(*values)
    
    def expect_geojson_output(self):
        return True

    def csv_to_area_string_and_colors(self, csvfile):

        return self.order_by_example(csv.reader(csvfile), "Department", 0, 1, 2, 3, ["Amazonas","Antioquia","Arauca","Atlantico","Bolivar","Boyaca","Caldas","Caqueta","Casanare","Cauca","Cesar","Choco","Cordoba","Cundinamarca","Guainia","Guaviare","Huila","La Guajira","Magdalena","Meta","Narino","Norte de Santander","Putumayo","Quindio","Risaralda","San Andres y Providencia  ","Santander","Sucre","Tolima","Valle del Cauca","Vaupes","Vichada"], [0.0 for i in range(0,32)], {"Amazonas":"1","Antioquia":"2","Arauca":"3","Atlantico":"4","Bolivar":"5","Boyaca":"6","Caldas":"7","Caqueta":"8","Casanare":"9","Cauca":"10","Cesar":"11","Choco":"12","Cordoba":"13","Cundinamarca":"14","Guainia":"15","Guaviare":"16","Huila":"17","La Guajira":"18","Magdalena":"19","Meta":"20","Narino":"21","Norte de Santander":"22","Putumayo":"23","Quindio":"24","Risaralda":"25","San Andres y Providencia  ":"26","Santander":"27","Sucre":"28","Tolima":"29","Valle del Cauca":"30","Vaupes":"31","Vichada":"32"})
