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
        return """cartogram_id,Region Data,Region Name,Inset\n
1,{},Adana,L\n
2,{},Adiyaman,L\n
3,{},Afyon,L\n
4,{},Agri,L\n
5,{},Aksaray,L\n
6,{},Amasya,L\n
7,{},Ankara,L\n
8,{},Antalya,L\n
9,{},Ardahan,L\n
10,{},Artvin,L\n
11,{},Aydin,L\n
12,{},Balikesir,L\n
13,{},Bartin,L\n
14,{},Batman,L\n
15,{},Bayburt,L\n
16,{},Bilecik,L\n
17,{},Bingol,L\n
18,{},Bitlis,L\n
19,{},Bolu,L\n
20,{},Burdur,L\n
21,{},Bursa,L\n
22,{},Canakkale,L\n
23,{},Cankiri,L\n
24,{},Corum,L\n
25,{},Denizli,L\n
26,{},Diyarbakir,L\n
27,{},Duzce,L\n
28,{},Edirne,L\n
29,{},Elazig,L\n
30,{},Erzincan,L\n
31,{},Erzurum,L\n
32,{},Eskisehir,L\n
33,{},Gaziantep,L\n
34,{},Giresun,L\n
35,{},Gumushane,L\n
36,{},Hakkari,L\n
37,{},Hatay,L\n
38,{},Igdir,L\n
39,{},Isparta,L\n
40,{},Istanbul,L\n
41,{},Izmir,R\n
42,{},Kahramanmaras,R\n
43,{},Karabuk,R\n
44,{},Karaman,R\n
45,{},Kars,R\n
46,{},Kastamonu,R\n
47,{},Kayseri,R\n
48,{},Kilis,R\n
49,{},Kinkkale,R\n
50,{},Kirklareli,R\n
51,{},Kirsehir,R\n
52,{},Kocaeli,R\n
53,{},Konya,R\n
54,{},Kutahya,R\n
55,{},Malatya,R\n
56,{},Manisa,R\n
57,{},Mardin,R\n
58,{},Mersin,R\n
59,{},Mugla,R\n
60,{},Mus,R\n
61,{},Nevsehir,R\n
62,{},Nigde,R\n
63,{},Ordu,R\n
64,{},Osmaniye,R\n
65,{},Rize,R\n
66,{},Sakarya,R\n
67,{},Samsun,R\n
68,{},Sanliurfa,R\n
69,{},Siirt,R\n
70,{},Sinop,R\n
71,{},Sirnak,R\n
72,{},Sivas,R\n
73,{},Tekirdag,R\n
74,{},Tokat,R\n
75,{},Trabzon,R\n
76,{},Tunceli,R\n
77,{},Usak,R\n
78,{},Van,R\n
79,{},Yalova,R\n
80,{},Yozgat,R\n
81,{},Zonguldak,R\n""".format(*values)
    
    def expect_geojson_output(self):
        return True

    def csv_to_area_string_and_colors(self, csvfile):

        return self.order_by_example(csv.reader(csvfile), "Province", 0, 1, 2, 3, ["Adana","Adiyaman","Afyon","Agri","Aksaray","Amasya","Ankara","Antalya","Ardahan","Artvin","Aydin","Balikesir","Bartin","Batman","Bayburt","Bilecik","Bingol","Bitlis","Bolu","Burdur","Bursa","Canakkale","Cankiri","Corum","Denizli","Diyarbakir","Duzce","Edirne","Elazig","Erzincan","Erzurum","Eskisehir","Gaziantep","Giresun","Gumushane","Hakkari","Hatay","Igdir","Isparta","Istanbul","Izmir","Kahramanmaras","Karabuk","Karaman","Kars","Kastamonu","Kayseri","Kilis","Kinkkale","Kirklareli","Kirsehir","Kocaeli","Konya","Kutahya","Malatya","Manisa","Mardin","Mersin","Mugla","Mus","Nevsehir","Nigde","Ordu","Osmaniye","Rize","Sakarya","Samsun","Sanliurfa","Siirt","Sinop","Sirnak","Sivas","Tekirdag","Tokat","Trabzon","Tunceli","Usak","Van","Yalova","Yozgat","Zonguldak"], [0.0 for i in range(0,81)], {"Adana":"1","Adiyaman":"2","Afyon":"3","Agri":"4","Aksaray":"5","Amasya":"6","Ankara":"7","Antalya":"8","Ardahan":"9","Artvin":"10","Aydin":"11","Balikesir":"12","Bartin":"13","Batman":"14","Bayburt":"15","Bilecik":"16","Bingol":"17","Bitlis":"18","Bolu":"19","Burdur":"20","Bursa":"21","Canakkale":"22","Cankiri":"23","Corum":"24","Denizli":"25","Diyarbakir":"26","Duzce":"27","Edirne":"28","Elazig":"29","Erzincan":"30","Erzurum":"31","Eskisehir":"32","Gaziantep":"33","Giresun":"34","Gumushane":"35","Hakkari":"36","Hatay":"37","Igdir":"38","Isparta":"39","Istanbul":"40","Izmir":"41","Kahramanmaras":"42","Karabuk":"43","Karaman":"44","Kars":"45","Kastamonu":"46","Kayseri":"47","Kilis":"48","Kinkkale":"49","Kirklareli":"50","Kirsehir":"51","Kocaeli":"52","Konya":"53","Kutahya":"54","Malatya":"55","Manisa":"56","Mardin":"57","Mersin":"58","Mugla":"59","Mus":"60","Nevsehir":"61","Nigde":"62","Ordu":"63","Osmaniye":"64","Rize":"65","Sakarya":"66","Samsun":"67","Sanliurfa":"68","Siirt":"69","Sinop":"70","Sirnak":"71","Sivas":"72","Tekirdag":"73","Tokat":"74","Trabzon":"75","Tunceli":"76","Usak":"77","Van":"78","Yalova":"79","Yozgat":"80","Zonguldak":"81"})
