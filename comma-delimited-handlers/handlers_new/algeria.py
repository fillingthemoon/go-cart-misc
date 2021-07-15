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
2,{},Ain DeflaL\n
3,{},Ain TemouchentL\n
4,{},AlgerL\n
5,{},AnnabaL\n
6,{},BatnaL\n
7,{},BecharL\n
8,{},BejaiaL\n
9,{},BiskraL\n
10,{},BlidaL\n
11,{},Bordj Bou ArreridjL\n
12,{},BouiraL\n
13,{},BoumerdesL\n
14,{},ChlefL\n
15,{},ConstantineL\n
16,{},DjelfaL\n
17,{},El BayadhL\n
18,{},El OuedL\n
19,{},El TarfL\n
20,{},GhardaiaL\n
21,{},GuelmaL\n
22,{},IlliziL\n
23,{},JijelL\n
24,{},KhenchelaR\n
25,{},LaghouatR\n
26,{},M'SilaR\n
27,{},MascaraR\n
28,{},MedeaR\n
29,{},MilaR\n
30,{},MostaganemR\n
31,{},NaamaR\n
32,{},OranR\n
33,{},OuarglaR\n
34,{},Oum el BouaghiR\n
35,{},RelizaneR\n
36,{},SaidaR\n
37,{},SetifR\n
38,{},Sidi Bel AbbesR\n
39,{},SkikdaR\n
40,{},Souk AhrasR\n
41,{},TamanghassetR\n
42,{},TebessaR\n
43,{},TiaretR\n
44,{},TindoufR\n
45,{},TipazaR\n
46,{},TissemsiltR\n
47,{},Tizi OuzouR\n
48,{},Tlemcen,R\n""".format(*values)
    
    def expect_geojson_output(self):
        return True

    def csv_to_area_string_and_colors(self, csvfile):

        return self.order_by_example(csv.reader(csvfile), "Province", 0, 1, 2, 3, ["Adrar","Ain Defla","Ain Temouchent","Alger","Annaba","Batna","Bechar","Bejaia","Biskra","Blida","Bordj Bou Arreridj","Bouira","Boumerdes","Chlef","Constantine","Djelfa","El Bayadh","El Oued","El Tarf","Ghardaia","Guelma","Illizi","Jijel","Khenchela","Laghouat","M'Sila","Mascara","Medea","Mila","Mostaganem","Naama","Oran","Ouargla","Oum el Bouaghi","Relizane","Saida","Setif","Sidi Bel Abbes","Skikda","Souk Ahras","Tamanghasset","Tebessa","Tiaret","Tindouf","Tipaza","Tissemsilt","Tizi Ouzou","Tlemcen"], [0.0 for i in range(0,48)], {"Adrar":"1","Ain Defla":"2","Ain Temouchent":"3","Alger":"4","Annaba":"5","Batna":"6","Bechar":"7","Bejaia":"8","Biskra":"9","Blida":"10","Bordj Bou Arreridj":"11","Bouira":"12","Boumerdes":"13","Chlef":"14","Constantine":"15","Djelfa":"16","El Bayadh":"17","El Oued":"18","El Tarf":"19","Ghardaia":"20","Guelma":"21","Illizi":"22","Jijel":"23","Khenchela":"24","Laghouat":"25","M'Sila":"26","Mascara":"27","Medea":"28","Mila":"29","Mostaganem":"30","Naama":"31","Oran":"32","Ouargla":"33","Oum el Bouaghi":"34","Relizane":"35","Saida":"36","Setif":"37","Sidi Bel Abbes":"38","Skikda":"39","Souk Ahras":"40","Tamanghasset":"41","Tebessa":"42","Tiaret":"43","Tindouf":"44","Tipaza":"45","Tissemsilt":"46","Tizi Ouzou":"47","Tlemcen":"48"})
