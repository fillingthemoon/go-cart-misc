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
        return """cartogram_id,Region Data,Region Name,Inset
1,{},Alba,L
2,{},Arad,L
3,{},Arges,L
4,{},Bacau,L
5,{},Bihor,L
6,{},Bistrita-Nasaud,L
7,{},Botosani,L
8,{},Braila,L
9,{},Brasov,L
10,{},Bucharest,L
11,{},Buzau,L
12,{},Calarasi,L
13,{},Caras-Severin,L
14,{},Cluj,L
15,{},Constanta,L
16,{},Covasna,L
17,{},Dambovita,L
18,{},Dolj,L
19,{},Galati,L
20,{},Giurgiu,L
21,{},Gorj,R
22,{},Harghita,R
23,{},Hunedoara,R
24,{},Ialomita,R
25,{},Iasi,R
26,{},Ilfov,R
27,{},Maramures,R
28,{},Mehedinti,R
29,{},Mures,R
30,{},Neamt,R
31,{},Olt,R
32,{},Prahova,R
33,{},Salaj,R
34,{},Satu Mare,R
35,{},Sibiu,R
36,{},Suceava,R
37,{},Teleorman,R
38,{},Timis,R
39,{},Tulcea,R
40,{},Valcea,R
41,{},Vaslui,R
42,{},Vrancea,R""".format(*values)
    
    def expect_geojson_output(self):
        return True

    def csv_to_area_string_and_colors(self, csvfile):

        return self.order_by_example(csv.reader(csvfile), "County", 0, 1, 2, 3, ["Alba","Arad","Arges","Bacau","Bihor","Bistrita-Nasaud","Botosani","Braila","Brasov","Bucharest","Buzau","Calarasi","Caras-Severin","Cluj","Constanta","Covasna","Dambovita","Dolj","Galati","Giurgiu","Gorj","Harghita","Hunedoara","Ialomita","Iasi","Ilfov","Maramures","Mehedinti","Mures","Neamt","Olt","Prahova","Salaj","Satu Mare","Sibiu","Suceava","Teleorman","Timis","Tulcea","Valcea","Vaslui","Vrancea"], [0.0 for i in range(0,42)], {"Alba":"1","Arad":"2","Arges":"3","Bacau":"4","Bihor":"5","Bistrita-Nasaud":"6","Botosani":"7","Braila":"8","Brasov":"9","Bucharest":"10","Buzau":"11","Calarasi":"12","Caras-Severin":"13","Cluj":"14","Constanta":"15","Covasna":"16","Dambovita":"17","Dolj":"18","Galati":"19","Giurgiu":"20","Gorj":"21","Harghita":"22","Hunedoara":"23","Ialomita":"24","Iasi":"25","Ilfov":"26","Maramures":"27","Mehedinti":"28","Mures":"29","Neamt":"30","Olt":"31","Prahova":"32","Salaj":"33","Satu Mare":"34","Sibiu":"35","Suceava":"36","Teleorman":"37","Timis":"38","Tulcea":"39","Valcea":"40","Vaslui":"41","Vrancea":"42"})
