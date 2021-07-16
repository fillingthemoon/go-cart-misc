import settings
import handlers.base_handler
import csv

class CartogramHandler(handlers.base_handler.BaseCartogramHandler):

    def get_name(self):
        return "Turkey"

    def get_gen_file(self):
        return "{}/tur_processedmap.json".format(settings.CARTOGRAM_DATA_DIR)
    
    def validate_values(self, values):

        if len(values) != 81:
            return False
        
        for v in values:
            if type(v) != float:
                return False

        return True
    
    def gen_area_data(self, values):
        return """cartogram_id,Region Data,Region Name,Inset
1,{},Adana,L
2,{},Adiyaman,L
3,{},Afyon,L
4,{},Agri,L
5,{},Aksaray,L
6,{},Amasya,L
7,{},Ankara,L
8,{},Antalya,L
9,{},Ardahan,L
10,{},Artvin,L
11,{},Aydin,L
12,{},Balikesir,L
13,{},Bartin,L
14,{},Batman,L
15,{},Bayburt,L
16,{},Bilecik,L
17,{},Bingol,L
18,{},Bitlis,L
19,{},Bolu,L
20,{},Burdur,L
21,{},Bursa,L
22,{},Canakkale,L
23,{},Cankiri,L
24,{},Corum,L
25,{},Denizli,L
26,{},Diyarbakir,L
27,{},Duzce,L
28,{},Edirne,L
29,{},Elazig,L
30,{},Erzincan,L
31,{},Erzurum,L
32,{},Eskisehir,L
33,{},Gaziantep,L
34,{},Giresun,L
35,{},Gumushane,L
36,{},Hakkari,L
37,{},Hatay,L
38,{},Igdir,L
39,{},Isparta,L
40,{},Istanbul,L
41,{},Izmir,R
42,{},Kahramanmaras,R
43,{},Karabuk,R
44,{},Karaman,R
45,{},Kars,R
46,{},Kastamonu,R
47,{},Kayseri,R
48,{},Kilis,R
49,{},Kinkkale,R
50,{},Kirklareli,R
51,{},Kirsehir,R
52,{},Kocaeli,R
53,{},Konya,R
54,{},Kutahya,R
55,{},Malatya,R
56,{},Manisa,R
57,{},Mardin,R
58,{},Mersin,R
59,{},Mugla,R
60,{},Mus,R
61,{},Nevsehir,R
62,{},Nigde,R
63,{},Ordu,R
64,{},Osmaniye,R
65,{},Rize,R
66,{},Sakarya,R
67,{},Samsun,R
68,{},Sanliurfa,R
69,{},Siirt,R
70,{},Sinop,R
71,{},Sirnak,R
72,{},Sivas,R
73,{},Tekirdag,R
74,{},Tokat,R
75,{},Trabzon,R
76,{},Tunceli,R
77,{},Usak,R
78,{},Van,R
79,{},Yalova,R
80,{},Yozgat,R
81,{},Zonguldak,R""".format(*values)
    
    def expect_geojson_output(self):
        return True

    def csv_to_area_string_and_colors(self, csvfile):

        return self.order_by_example(csv.reader(csvfile), "Province", 0, 1, 2, 3, ["Adana","Adiyaman","Afyon","Agri","Aksaray","Amasya","Ankara","Antalya","Ardahan","Artvin","Aydin","Balikesir","Bartin","Batman","Bayburt","Bilecik","Bingol","Bitlis","Bolu","Burdur","Bursa","Canakkale","Cankiri","Corum","Denizli","Diyarbakir","Duzce","Edirne","Elazig","Erzincan","Erzurum","Eskisehir","Gaziantep","Giresun","Gumushane","Hakkari","Hatay","Igdir","Isparta","Istanbul","Izmir","Kahramanmaras","Karabuk","Karaman","Kars","Kastamonu","Kayseri","Kilis","Kinkkale","Kirklareli","Kirsehir","Kocaeli","Konya","Kutahya","Malatya","Manisa","Mardin","Mersin","Mugla","Mus","Nevsehir","Nigde","Ordu","Osmaniye","Rize","Sakarya","Samsun","Sanliurfa","Siirt","Sinop","Sirnak","Sivas","Tekirdag","Tokat","Trabzon","Tunceli","Usak","Van","Yalova","Yozgat","Zonguldak"], [0.0 for i in range(0,81)], {"Adana":"1","Adiyaman":"2","Afyon":"3","Agri":"4","Aksaray":"5","Amasya":"6","Ankara":"7","Antalya":"8","Ardahan":"9","Artvin":"10","Aydin":"11","Balikesir":"12","Bartin":"13","Batman":"14","Bayburt":"15","Bilecik":"16","Bingol":"17","Bitlis":"18","Bolu":"19","Burdur":"20","Bursa":"21","Canakkale":"22","Cankiri":"23","Corum":"24","Denizli":"25","Diyarbakir":"26","Duzce":"27","Edirne":"28","Elazig":"29","Erzincan":"30","Erzurum":"31","Eskisehir":"32","Gaziantep":"33","Giresun":"34","Gumushane":"35","Hakkari":"36","Hatay":"37","Igdir":"38","Isparta":"39","Istanbul":"40","Izmir":"41","Kahramanmaras":"42","Karabuk":"43","Karaman":"44","Kars":"45","Kastamonu":"46","Kayseri":"47","Kilis":"48","Kinkkale":"49","Kirklareli":"50","Kirsehir":"51","Kocaeli":"52","Konya":"53","Kutahya":"54","Malatya":"55","Manisa":"56","Mardin":"57","Mersin":"58","Mugla":"59","Mus":"60","Nevsehir":"61","Nigde":"62","Ordu":"63","Osmaniye":"64","Rize":"65","Sakarya":"66","Samsun":"67","Sanliurfa":"68","Siirt":"69","Sinop":"70","Sirnak":"71","Sivas":"72","Tekirdag":"73","Tokat":"74","Trabzon":"75","Tunceli":"76","Usak":"77","Van":"78","Yalova":"79","Yozgat":"80","Zonguldak":"81"})
