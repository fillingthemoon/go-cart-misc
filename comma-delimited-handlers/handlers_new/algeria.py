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
        return """cartogram_id,Region Data,Region Name,Inset\n
1,{},Adrar,L\n
2,{},Ain Defla,L\n
3,{},Ain Temouchent,L\n
4,{},Alger,L\n
5,{},Annaba,L\n
6,{},Batna,L\n
7,{},Bechar,L\n
8,{},Bejaia,L\n
9,{},Biskra,L\n
10,{},Blida,L\n
11,{},Bordj Bou Arreridj,L\n
12,{},Bouira,L\n
13,{},Boumerdes,L\n
14,{},Chlef,L\n
15,{},Constantine,L\n
16,{},Djelfa,L\n
17,{},El Bayadh,L\n
18,{},El Oued,L\n
19,{},El Tarf,L\n
20,{},Ghardaia,L\n
21,{},Guelma,L\n
22,{},Illizi,L\n
23,{},Jijel,L\n
24,{},Khenchela,R\n
25,{},Laghouat,R\n
26,{},M'Sila,R\n
27,{},Mascara,R\n
28,{},Medea,R\n
29,{},Mila,R\n
30,{},Mostaganem,R\n
31,{},Naama,R\n
32,{},Oran,R\n
33,{},Ouargla,R\n
34,{},Oum el Bouaghi,R\n
35,{},Relizane,R\n
36,{},Saida,R\n
37,{},Setif,R\n
38,{},Sidi Bel Abbes,R\n
39,{},Skikda,R\n
40,{},Souk Ahras,R\n
41,{},Tamanghasset,R\n
42,{},Tebessa,R\n
43,{},Tiaret,R\n
44,{},Tindouf,R\n
45,{},Tipaza,R\n
46,{},Tissemsilt,R\n
47,{},Tizi Ouzou,R\n
48,{},Tlemcen,R\n""".format(*values)
    
    def expect_geojson_output(self):
        return True

    def csv_to_area_string_and_colors(self, csvfile):

        return self.order_by_example(csv.reader(csvfile), "Province", 0, 1, 2, 3, ["Adrar","Ain Defla","Ain Temouchent","Alger","Annaba","Batna","Bechar","Bejaia","Biskra","Blida","Bordj Bou Arreridj","Bouira","Boumerdes","Chlef","Constantine","Djelfa","El Bayadh","El Oued","El Tarf","Ghardaia","Guelma","Illizi","Jijel","Khenchela","Laghouat","M'Sila","Mascara","Medea","Mila","Mostaganem","Naama","Oran","Ouargla","Oum el Bouaghi","Relizane","Saida","Setif","Sidi Bel Abbes","Skikda","Souk Ahras","Tamanghasset","Tebessa","Tiaret","Tindouf","Tipaza","Tissemsilt","Tizi Ouzou","Tlemcen"], [0.0 for i in range(0,48)], {"Adrar":"1","Ain Defla":"2","Ain Temouchent":"3","Alger":"4","Annaba":"5","Batna":"6","Bechar":"7","Bejaia":"8","Biskra":"9","Blida":"10","Bordj Bou Arreridj":"11","Bouira":"12","Boumerdes":"13","Chlef":"14","Constantine":"15","Djelfa":"16","El Bayadh":"17","El Oued":"18","El Tarf":"19","Ghardaia":"20","Guelma":"21","Illizi":"22","Jijel":"23","Khenchela":"24","Laghouat":"25","M'Sila":"26","Mascara":"27","Medea":"28","Mila":"29","Mostaganem":"30","Naama":"31","Oran":"32","Ouargla":"33","Oum el Bouaghi":"34","Relizane":"35","Saida":"36","Setif":"37","Sidi Bel Abbes":"38","Skikda":"39","Souk Ahras":"40","Tamanghasset":"41","Tebessa":"42","Tiaret":"43","Tindouf":"44","Tipaza":"45","Tissemsilt":"46","Tizi Ouzou":"47","Tlemcen":"48"})
