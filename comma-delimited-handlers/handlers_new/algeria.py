import settings
import handlers.base_handler
import csv

class CartogramHandler(handlers.base_handler.BaseCartogramHandler):

    def get_name(self):
        return "Algeria"

    def get_gen_file(self):
        return "{}/dza_processedmap.json".format(settings.CARTOGRAM_DATA_DIR)
    
    def validate_values(self, values):

        if len(values) != 48:
            return False
        
        for v in values:
            if type(v) != float:
                return False

        return True
    
    def gen_area_data(self, values):
        return """cartogram_id,Region Data,Region Name,Inset
1,{},Adrar,L
2,{},Ain Defla,L
3,{},Ain Temouchent,L
4,{},Alger,L
5,{},Annaba,L
6,{},Batna,L
7,{},Bechar,L
8,{},Bejaia,L
9,{},Biskra,L
10,{},Blida,L
11,{},Bordj Bou Arreridj,L
12,{},Bouira,L
13,{},Boumerdes,L
14,{},Chlef,L
15,{},Constantine,L
16,{},Djelfa,L
17,{},El Bayadh,L
18,{},El Oued,L
19,{},El Tarf,L
20,{},Ghardaia,L
21,{},Guelma,L
22,{},Illizi,L
23,{},Jijel,L
24,{},Khenchela,R
25,{},Laghouat,R
26,{},M'Sila,R
27,{},Mascara,R
28,{},Medea,R
29,{},Mila,R
30,{},Mostaganem,R
31,{},Naama,R
32,{},Oran,R
33,{},Ouargla,R
34,{},Oum el Bouaghi,R
35,{},Relizane,R
36,{},Saida,R
37,{},Setif,R
38,{},Sidi Bel Abbes,R
39,{},Skikda,R
40,{},Souk Ahras,R
41,{},Tamanghasset,R
42,{},Tebessa,R
43,{},Tiaret,R
44,{},Tindouf,R
45,{},Tipaza,R
46,{},Tissemsilt,R
47,{},Tizi Ouzou,R
48,{},Tlemcen,R""".format(*values)
    
    def expect_geojson_output(self):
        return True

    def csv_to_area_string_and_colors(self, csvfile):

        return self.order_by_example(csv.reader(csvfile), "Province", 0, 1, 2, 3, ["Adrar","Ain Defla","Ain Temouchent","Alger","Annaba","Batna","Bechar","Bejaia","Biskra","Blida","Bordj Bou Arreridj","Bouira","Boumerdes","Chlef","Constantine","Djelfa","El Bayadh","El Oued","El Tarf","Ghardaia","Guelma","Illizi","Jijel","Khenchela","Laghouat","M'Sila","Mascara","Medea","Mila","Mostaganem","Naama","Oran","Ouargla","Oum el Bouaghi","Relizane","Saida","Setif","Sidi Bel Abbes","Skikda","Souk Ahras","Tamanghasset","Tebessa","Tiaret","Tindouf","Tipaza","Tissemsilt","Tizi Ouzou","Tlemcen"], [0.0 for i in range(0,48)], {"Adrar":"1","Ain Defla":"2","Ain Temouchent":"3","Alger":"4","Annaba":"5","Batna":"6","Bechar":"7","Bejaia":"8","Biskra":"9","Blida":"10","Bordj Bou Arreridj":"11","Bouira":"12","Boumerdes":"13","Chlef":"14","Constantine":"15","Djelfa":"16","El Bayadh":"17","El Oued":"18","El Tarf":"19","Ghardaia":"20","Guelma":"21","Illizi":"22","Jijel":"23","Khenchela":"24","Laghouat":"25","M'Sila":"26","Mascara":"27","Medea":"28","Mila":"29","Mostaganem":"30","Naama":"31","Oran":"32","Ouargla":"33","Oum el Bouaghi":"34","Relizane":"35","Saida":"36","Setif":"37","Sidi Bel Abbes":"38","Skikda":"39","Souk Ahras":"40","Tamanghasset":"41","Tebessa":"42","Tiaret":"43","Tindouf":"44","Tipaza":"45","Tissemsilt":"46","Tizi Ouzou":"47","Tlemcen":"48"})
