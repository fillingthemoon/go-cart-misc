import settings
import handlers.base_handler
import csv

class CartogramHandler(handlers.base_handler.BaseCartogramHandler):

    def get_name(self):
        return "Russia"

    def get_gen_file(self):
        return "{}/rus_processedmap.json".format(settings.CARTOGRAM_DATA_DIR)
    
    def validate_values(self, values):

        if len(values) != 83:
            return False
        
        for v in values:
            if type(v) != float:
                return False

        return True
    
    def gen_area_data(self, values):
        return """cartogram_id,Region Data,Region Name,Inset\n
1,{},Adygey,L\n
2,{},Altay,L\n
3,{},Amur,L\n
4,{},Arkhangel'sk,L\n
5,{},Astrakhan',L\n
6,{},Bashkortostan,L\n
7,{},Belgorod,L\n
8,{},Bryansk,L\n
9,{},Buryat,L\n
10,{},Chechnya,L\n
11,{},Chelyabinsk,L\n
12,{},Chukot,L\n
13,{},Chuvash,L\n
14,{},City of St. Petersburg,L\n
15,{},Dagestan,L\n
16,{},Gorno-Altay,L\n
17,{},Ingush,L\n
18,{},Irkutsk,L\n
19,{},Ivanovo,L\n
20,{},Kabardin-Balkar,L\n
21,{},Kaliningrad,L\n
22,{},Kalmyk,L\n
23,{},Kaluga,L\n
24,{},Kamchatka,L\n
25,{},Karachay-Cherkess,L\n
26,{},Karelia,L\n
27,{},Kemerovo,L\n
28,{},Khabarovsk,L\n
29,{},Khakass,L\n
30,{},Khanty-Mansiy,L\n
31,{},Kirov,L\n
32,{},Komi,L\n
33,{},Kostroma,L\n
34,{},Krasnodar,L\n
35,{},Krasnoyarsk,L\n
36,{},Kurgan,L\n
37,{},Kursk,L\n
38,{},Leningrad,L\n
39,{},Lipetsk,L\n
40,{},Maga Buryatdan,L\n
41,{},Mariy-El,L\n
42,{},Mordovia,R\n
43,{},Moscow City,R\n
44,{},Moskva,R\n
45,{},Murmansk,R\n
46,{},Nenets,R\n
47,{},Nizhegorod,R\n
48,{},North Ossetia,R\n
49,{},Novgorod,R\n
50,{},Novosibirsk,R\n
51,{},Omsk,R\n
52,{},Orel,R\n
53,{},Orenburg,R\n
54,{},Penza,R\n
55,{},Perm',R\n
56,{},Primor'ye,R\n
57,{},Pskov,R\n
58,{},Rostov,R\n
59,{},Ryazan',R\n
60,{},Sakha,R\n
61,{},Sakhalin,R\n
62,{},Samara,R\n
63,{},Saratov,R\n
64,{},Smolensk,R\n
65,{},Stavropol',R\n
66,{},Sverdlovsk,R\n
67,{},Tambov,R\n
68,{},Tatarstan,R\n
69,{},Tomsk,R\n
70,{},Tula,R\n
71,{},Tuva,R\n
72,{},Tver',R\n
73,{},Tyumen',R\n
74,{},Udmurt,R\n
75,{},Ul'yanovsk,R\n
76,{},Vladimir,R\n
77,{},Volgograd,R\n
78,{},Vologda,R\n
79,{},Voronezh,R\n
80,{},Yamal-Nenets,R\n
81,{},Yaroslavl',R\n
82,{},Yevrey,R\n
83,{},Zabaykal'ye,R\n""".format(*values)
    
    def expect_geojson_output(self):
        return True

    def csv_to_area_string_and_colors(self, csvfile):

        return self.order_by_example(csv.reader(csvfile), "Region", 0, 1, 2, 3, ["Adygey","Altay","Amur","Arkhangel'sk","Astrakhan'","Bashkortostan","Belgorod","Bryansk","Buryat","Chechnya","Chelyabinsk","Chukot","Chuvash","City of St. Petersburg","Dagestan","Gorno-Altay","Ingush","Irkutsk","Ivanovo","Kabardin-Balkar","Kaliningrad","Kalmyk","Kaluga","Kamchatka","Karachay-Cherkess","Karelia","Kemerovo","Khabarovsk","Khakass","Khanty-Mansiy","Kirov","Komi","Kostroma","Krasnodar","Krasnoyarsk","Kurgan","Kursk","Leningrad","Lipetsk","Maga Buryatdan","Mariy-El","Mordovia","Moscow City","Moskva","Murmansk","Nenets","Nizhegorod","North Ossetia","Novgorod","Novosibirsk","Omsk","Orel","Orenburg","Penza","Perm'","Primor'ye","Pskov","Rostov","Ryazan'","Sakha","Sakhalin","Samara","Saratov","Smolensk","Stavropol'","Sverdlovsk","Tambov","Tatarstan","Tomsk","Tula","Tuva","Tver'","Tyumen'","Udmurt","Ul'yanovsk","Vladimir","Volgograd","Vologda","Voronezh","Yamal-Nenets","Yaroslavl'","Yevrey","Zabaykal'ye"], [0.0 for i in range(0,83)], {"Adygey":"1","Altay":"2","Amur":"3","Arkhangel'sk":"4","Astrakhan'":"5","Bashkortostan":"6","Belgorod":"7","Bryansk":"8","Buryat":"9","Chechnya":"10","Chelyabinsk":"11","Chukot":"12","Chuvash":"13","City of St. Petersburg":"14","Dagestan":"15","Gorno-Altay":"16","Ingush":"17","Irkutsk":"18","Ivanovo":"19","Kabardin-Balkar":"20","Kaliningrad":"21","Kalmyk":"22","Kaluga":"23","Kamchatka":"24","Karachay-Cherkess":"25","Karelia":"26","Kemerovo":"27","Khabarovsk":"28","Khakass":"29","Khanty-Mansiy":"30","Kirov":"31","Komi":"32","Kostroma":"33","Krasnodar":"34","Krasnoyarsk":"35","Kurgan":"36","Kursk":"37","Leningrad":"38","Lipetsk":"39","Maga Buryatdan":"40","Mariy-El":"41","Mordovia":"42","Moscow City":"43","Moskva":"44","Murmansk":"45","Nenets":"46","Nizhegorod":"47","North Ossetia":"48","Novgorod":"49","Novosibirsk":"50","Omsk":"51","Orel":"52","Orenburg":"53","Penza":"54","Perm'":"55","Primor'ye":"56","Pskov":"57","Rostov":"58","Ryazan'":"59","Sakha":"60","Sakhalin":"61","Samara":"62","Saratov":"63","Smolensk":"64","Stavropol'":"65","Sverdlovsk":"66","Tambov":"67","Tatarstan":"68","Tomsk":"69","Tula":"70","Tuva":"71","Tver'":"72","Tyumen'":"73","Udmurt":"74","Ul'yanovsk":"75","Vladimir":"76","Volgograd":"77","Vologda":"78","Voronezh":"79","Yamal-Nenets":"80","Yaroslavl'":"81","Yevrey":"82","Zabaykal'ye":"83"})
