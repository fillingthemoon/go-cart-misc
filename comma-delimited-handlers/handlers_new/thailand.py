import settings
import handlers.base_handler
import csv

class CartogramHandler(handlers.base_handler.BaseCartogramHandler):

    def get_name(self):
        return "Thailand"

    def get_gen_file(self):
        return "{}/thailand_processedmap.json".format(settings.CARTOGRAM_DATA_DIR)
    
    def validate_values(self, values):

        if len(values) != 77:
            return False
        
        for v in values:
            if type(v) != float:
                return False

        return True
    
    def gen_area_data(self, values):
        return """cartogram_id,Region Data,Region Name,Inset
1,{},Amnat Charoen,L
2,{},Ang Thong,L
3,{},Bangkok Metropolis,L
4,{},Bueng Kan,L
5,{},Buri Ram,L
6,{},Chachoengsao,L
7,{},Chai Nat,L
8,{},Chaiyaphum,L
9,{},Chanthaburi,L
10,{},Chiang Mai,L
11,{},Chiang Rai,L
12,{},Chon Buri,L
13,{},Chumphon,L
14,{},Kalasin,L
15,{},Kamphaeng Phet,L
16,{},Kanchanaburi,L
17,{},Khon Kaen,L
18,{},Krabi,L
19,{},Lampang,L
20,{},Lamphun,L
21,{},Loei,L
22,{},Lop Buri,L
23,{},Mae Hong Son,L
24,{},Maha Sarakham,L
25,{},Mukdahan,L
26,{},Nakhon Nayok,L
27,{},Nakhon Pathom,L
28,{},Nakhon Phanom,L
29,{},Nakhon Ratchasima,L
30,{},Nakhon Sawan,L
31,{},Nakhon Si Thammarat,L
32,{},Nan,L
33,{},Narathiwat,L
34,{},Nong Bua Lam Phu,L
35,{},Nong Khai,L
36,{},Nonthaburi,L
37,{},Pathum Thani,L
38,{},Pattani,L
39,{},Phangnga,R
40,{},Phatthalung,R
41,{},Phayao,R
42,{},Phetchabun,R
43,{},Phetchaburi,R
44,{},Phichit,R
45,{},Phitsanulok,R
46,{},Phra Nakhon Si Ayutthaya,R
47,{},Phrae,R
48,{},Phuket,R
49,{},Prachin Buri,R
50,{},Prachuap Khiri Khan,R
51,{},Ranong,R
52,{},Ratchaburi,R
53,{},Rayong,R
54,{},Roi Et,R
55,{},Sa Kaeo,R
56,{},Sakon Nakhon,R
57,{},Samut Prakan,R
58,{},Samut Sakhon,R
59,{},Samut Songkhram,R
60,{},Saraburi,R
61,{},Satun,R
62,{},Si Sa Ket,R
63,{},Sing Buri,R
64,{},Songkhla,R
65,{},Sukhothai,R
66,{},Suphan Buri,R
67,{},Surat Thani,R
68,{},Surin,R
69,{},Tak,R
70,{},Trang,R
71,{},Trat,R
72,{},Ubon Ratchathani,R
73,{},Udon Thani,R
74,{},Uthai Thani,R
75,{},Uttaradit,R
76,{},Yala,R
77,{},Yasothon,R""".format(*values)
    
    def expect_geojson_output(self):
        return True

    def csv_to_area_string_and_colors(self, csvfile):

        return self.order_by_example(csv.reader(csvfile), "Province", 0, 1, 2, 3, ["Amnat Charoen","Ang Thong","Bangkok Metropolis","Bueng Kan","Buri Ram","Chachoengsao","Chai Nat","Chaiyaphum","Chanthaburi","Chiang Mai","Chiang Rai","Chon Buri","Chumphon","Kalasin","Kamphaeng Phet","Kanchanaburi","Khon Kaen","Krabi","Lampang","Lamphun","Loei","Lop Buri","Mae Hong Son","Maha Sarakham","Mukdahan","Nakhon Nayok","Nakhon Pathom","Nakhon Phanom","Nakhon Ratchasima","Nakhon Sawan","Nakhon Si Thammarat","Nan","Narathiwat","Nong Bua Lam Phu","Nong Khai","Nonthaburi","Pathum Thani","Pattani","Phangnga","Phatthalung","Phayao","Phetchabun","Phetchaburi","Phichit","Phitsanulok","Phra Nakhon Si Ayutthaya","Phrae","Phuket","Prachin Buri","Prachuap Khiri Khan","Ranong","Ratchaburi","Rayong","Roi Et","Sa Kaeo","Sakon Nakhon","Samut Prakan","Samut Sakhon","Samut Songkhram","Saraburi","Satun","Si Sa Ket","Sing Buri","Songkhla","Sukhothai","Suphan Buri","Surat Thani","Surin","Tak","Trang","Trat","Ubon Ratchathani","Udon Thani","Uthai Thani","Uttaradit","Yala","Yasothon"], [0.0 for i in range(0,77)], {"Amnat Charoen":"1","Ang Thong":"2","Bangkok Metropolis":"3","Bueng Kan":"4","Buri Ram":"5","Chachoengsao":"6","Chai Nat":"7","Chaiyaphum":"8","Chanthaburi":"9","Chiang Mai":"10","Chiang Rai":"11","Chon Buri":"12","Chumphon":"13","Kalasin":"14","Kamphaeng Phet":"15","Kanchanaburi":"16","Khon Kaen":"17","Krabi":"18","Lampang":"19","Lamphun":"20","Loei":"21","Lop Buri":"22","Mae Hong Son":"23","Maha Sarakham":"24","Mukdahan":"25","Nakhon Nayok":"26","Nakhon Pathom":"27","Nakhon Phanom":"28","Nakhon Ratchasima":"29","Nakhon Sawan":"30","Nakhon Si Thammarat":"31","Nan":"32","Narathiwat":"33","Nong Bua Lam Phu":"34","Nong Khai":"35","Nonthaburi":"36","Pathum Thani":"37","Pattani":"38","Phangnga":"39","Phatthalung":"40","Phayao":"41","Phetchabun":"42","Phetchaburi":"43","Phichit":"44","Phitsanulok":"45","Phra Nakhon Si Ayutthaya":"46","Phrae":"47","Phuket":"48","Prachin Buri":"49","Prachuap Khiri Khan":"50","Ranong":"51","Ratchaburi":"52","Rayong":"53","Roi Et":"54","Sa Kaeo":"55","Sakon Nakhon":"56","Samut Prakan":"57","Samut Sakhon":"58","Samut Songkhram":"59","Saraburi":"60","Satun":"61","Si Sa Ket":"62","Sing Buri":"63","Songkhla":"64","Sukhothai":"65","Suphan Buri":"66","Surat Thani":"67","Surin":"68","Tak":"69","Trang":"70","Trat":"71","Ubon Ratchathani":"72","Udon Thani":"73","Uthai Thani":"74","Uttaradit":"75","Yala":"76","Yasothon":"77"})
