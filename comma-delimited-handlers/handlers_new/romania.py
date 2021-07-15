import settings
import handlers.base_handler
import csv

class CartogramHandler(handlers.base_handler.BaseCartogramHandler):

    def get_name(self):
        return "Romania"

    def get_gen_file(self):
        return "{}/romania_processedmap.json".format(settings.CARTOGRAM_DATA_DIR)
    
    def validate_values(self, values):

        if len(values) != 42:
            return False
        
        for v in values:
            if type(v) != float:
                return False

        return True
    
    def gen_area_data(self, values):
        return """cartogram_id,Region Data,Region Name,Inset\n
1,{},Alba,L\n
2,{},Arad,L\n
3,{},Arges,L\n
4,{},Bacau,L\n
5,{},Bihor,L\n
6,{},Bistrita-Nasaud,L\n
7,{},Botosani,L\n
8,{},Braila,L\n
9,{},Brasov,L\n
10,{},Bucharest,L\n
11,{},Buzau,L\n
12,{},Calarasi,L\n
13,{},Caras-Severin,L\n
14,{},Cluj,L\n
15,{},Constanta,L\n
16,{},Covasna,L\n
17,{},Dambovita,L\n
18,{},Dolj,L\n
19,{},Galati,L\n
20,{},Giurgiu,L\n
21,{},Gorj,R\n
22,{},Harghita,R\n
23,{},Hunedoara,R\n
24,{},Ialomita,R\n
25,{},Iasi,R\n
26,{},Ilfov,R\n
27,{},Maramures,R\n
28,{},Mehedinti,R\n
29,{},Mures,R\n
30,{},Neamt,R\n
31,{},Olt,R\n
32,{},Prahova,R\n
33,{},Salaj,R\n
34,{},Satu Mare,R\n
35,{},Sibiu,R\n
36,{},Suceava,R\n
37,{},Teleorman,R\n
38,{},Timis,R\n
39,{},Tulcea,R\n
40,{},Valcea,R\n
41,{},Vaslui,R\n
42,{},Vrancea,R\n""".format(*values)
    
    def expect_geojson_output(self):
        return True

    def csv_to_area_string_and_colors(self, csvfile):

        return self.order_by_example(csv.reader(csvfile), "County", 0, 1, 2, 3, ["Alba","Arad","Arges","Bacau","Bihor","Bistrita-Nasaud","Botosani","Braila","Brasov","Bucharest","Buzau","Calarasi","Caras-Severin","Cluj","Constanta","Covasna","Dambovita","Dolj","Galati","Giurgiu","Gorj","Harghita","Hunedoara","Ialomita","Iasi","Ilfov","Maramures","Mehedinti","Mures","Neamt","Olt","Prahova","Salaj","Satu Mare","Sibiu","Suceava","Teleorman","Timis","Tulcea","Valcea","Vaslui","Vrancea"], [0.0 for i in range(0,42)], {"Alba":"1","Arad":"2","Arges":"3","Bacau":"4","Bihor":"5","Bistrita-Nasaud":"6","Botosani":"7","Braila":"8","Brasov":"9","Bucharest":"10","Buzau":"11","Calarasi":"12","Caras-Severin":"13","Cluj":"14","Constanta":"15","Covasna":"16","Dambovita":"17","Dolj":"18","Galati":"19","Giurgiu":"20","Gorj":"21","Harghita":"22","Hunedoara":"23","Ialomita":"24","Iasi":"25","Ilfov":"26","Maramures":"27","Mehedinti":"28","Mures":"29","Neamt":"30","Olt":"31","Prahova":"32","Salaj":"33","Satu Mare":"34","Sibiu":"35","Suceava":"36","Teleorman":"37","Timis":"38","Tulcea":"39","Valcea":"40","Vaslui":"41","Vrancea":"42"})
