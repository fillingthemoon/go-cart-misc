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
        return """cartogram_id,Region Data,Region Name,Inset
1,{},Adygey,L
2,{},Altay,L
3,{},Amur,L
4,{},Arkhangel'sk,L
5,{},Astrakhan',L
6,{},Bashkortostan,L
7,{},Belgorod,L
8,{},Bryansk,L
9,{},Buryat,L
10,{},Chechnya,L
11,{},Chelyabinsk,L
12,{},Chukot,L
13,{},Chuvash,L
14,{},City of St. Petersburg,L
15,{},Dagestan,L
16,{},Gorno-Altay,L
17,{},Ingush,L
18,{},Irkutsk,L
19,{},Ivanovo,L
20,{},Kabardin-Balkar,L
21,{},Kaliningrad,L
22,{},Kalmyk,L
23,{},Kaluga,L
24,{},Kamchatka,L
25,{},Karachay-Cherkess,L
26,{},Karelia,L
27,{},Kemerovo,L
28,{},Khabarovsk,L
29,{},Khakass,L
30,{},Khanty-Mansiy,L
31,{},Kirov,L
32,{},Komi,L
33,{},Kostroma,L
34,{},Krasnodar,L
35,{},Krasnoyarsk,L
36,{},Kurgan,L
37,{},Kursk,L
38,{},Leningrad,L
39,{},Lipetsk,L
40,{},Maga Buryatdan,L
41,{},Mariy-El,L
42,{},Mordovia,R
43,{},Moscow City,R
44,{},Moskva,R
45,{},Murmansk,R
46,{},Nenets,R
47,{},Nizhegorod,R
48,{},North Ossetia,R
49,{},Novgorod,R
50,{},Novosibirsk,R
51,{},Omsk,R
52,{},Orel,R
53,{},Orenburg,R
54,{},Penza,R
55,{},Perm',R
56,{},Primor'ye,R
57,{},Pskov,R
58,{},Rostov,R
59,{},Ryazan',R
60,{},Sakha,R
61,{},Sakhalin,R
62,{},Samara,R
63,{},Saratov,R
64,{},Smolensk,R
65,{},Stavropol',R
66,{},Sverdlovsk,R
67,{},Tambov,R
68,{},Tatarstan,R
69,{},Tomsk,R
70,{},Tula,R
71,{},Tuva,R
72,{},Tver',R
73,{},Tyumen',R
74,{},Udmurt,R
75,{},Ul'yanovsk,R
76,{},Vladimir,R
77,{},Volgograd,R
78,{},Vologda,R
79,{},Voronezh,R
80,{},Yamal-Nenets,R
81,{},Yaroslavl',R
82,{},Yevrey,R
83,{},Zabaykal'ye,R""".format(*values)
    
    def expect_geojson_output(self):
        return True

    def csv_to_area_string_and_colors(self, csvfile):

        return self.order_by_example(csv.reader(csvfile), "Region", 0, 1, 2, 3, ["Adygey","Altay","Amur","Arkhangel'sk","Astrakhan'","Bashkortostan","Belgorod","Bryansk","Buryat","Chechnya","Chelyabinsk","Chukot","Chuvash","City of St. Petersburg","Dagestan","Gorno-Altay","Ingush","Irkutsk","Ivanovo","Kabardin-Balkar","Kaliningrad","Kalmyk","Kaluga","Kamchatka","Karachay-Cherkess","Karelia","Kemerovo","Khabarovsk","Khakass","Khanty-Mansiy","Kirov","Komi","Kostroma","Krasnodar","Krasnoyarsk","Kurgan","Kursk","Leningrad","Lipetsk","Maga Buryatdan","Mariy-El","Mordovia","Moscow City","Moskva","Murmansk","Nenets","Nizhegorod","North Ossetia","Novgorod","Novosibirsk","Omsk","Orel","Orenburg","Penza","Perm'","Primor'ye","Pskov","Rostov","Ryazan'","Sakha","Sakhalin","Samara","Saratov","Smolensk","Stavropol'","Sverdlovsk","Tambov","Tatarstan","Tomsk","Tula","Tuva","Tver'","Tyumen'","Udmurt","Ul'yanovsk","Vladimir","Volgograd","Vologda","Voronezh","Yamal-Nenets","Yaroslavl'","Yevrey","Zabaykal'ye"], [0.0 for i in range(0,83)], {"Adygey":"1","Altay":"2","Amur":"3","Arkhangel'sk":"4","Astrakhan'":"5","Bashkortostan":"6","Belgorod":"7","Bryansk":"8","Buryat":"9","Chechnya":"10","Chelyabinsk":"11","Chukot":"12","Chuvash":"13","City of St. Petersburg":"14","Dagestan":"15","Gorno-Altay":"16","Ingush":"17","Irkutsk":"18","Ivanovo":"19","Kabardin-Balkar":"20","Kaliningrad":"21","Kalmyk":"22","Kaluga":"23","Kamchatka":"24","Karachay-Cherkess":"25","Karelia":"26","Kemerovo":"27","Khabarovsk":"28","Khakass":"29","Khanty-Mansiy":"30","Kirov":"31","Komi":"32","Kostroma":"33","Krasnodar":"34","Krasnoyarsk":"35","Kurgan":"36","Kursk":"37","Leningrad":"38","Lipetsk":"39","Maga Buryatdan":"40","Mariy-El":"41","Mordovia":"42","Moscow City":"43","Moskva":"44","Murmansk":"45","Nenets":"46","Nizhegorod":"47","North Ossetia":"48","Novgorod":"49","Novosibirsk":"50","Omsk":"51","Orel":"52","Orenburg":"53","Penza":"54","Perm'":"55","Primor'ye":"56","Pskov":"57","Rostov":"58","Ryazan'":"59","Sakha":"60","Sakhalin":"61","Samara":"62","Saratov":"63","Smolensk":"64","Stavropol'":"65","Sverdlovsk":"66","Tambov":"67","Tatarstan":"68","Tomsk":"69","Tula":"70","Tuva":"71","Tver'":"72","Tyumen'":"73","Udmurt":"74","Ul'yanovsk":"75","Vladimir":"76","Volgograd":"77","Vologda":"78","Voronezh":"79","Yamal-Nenets":"80","Yaroslavl'":"81","Yevrey":"82","Zabaykal'ye":"83"})
