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
        return """cartogram_id,Region Data,Region Name,Inset\n
1,{},Amnat Charoen,L\n
2,{},Ang Thong,L\n
3,{},Bangkok Metropolis,L\n
4,{},Bueng Kan,L\n
5,{},Buri Ram,L\n
6,{},Chachoengsao,L\n
7,{},Chai Nat,L\n
8,{},Chaiyaphum,L\n
9,{},Chanthaburi,L\n
10,{},Chiang Mai,L\n
11,{},Chiang Rai,L\n
12,{},Chon Buri,L\n
13,{},Chumphon,L\n
14,{},Kalasin,L\n
15,{},Kamphaeng Phet,L\n
16,{},Kanchanaburi,L\n
17,{},Khon Kaen,L\n
18,{},Krabi,L\n
19,{},Lampang,L\n
20,{},Lamphun,L\n
21,{},Loei,L\n
22,{},Lop Buri,L\n
23,{},Mae Hong Son,L\n
24,{},Maha Sarakham,L\n
25,{},Mukdahan,L\n
26,{},Nakhon Nayok,L\n
27,{},Nakhon Pathom,L\n
28,{},Nakhon Phanom,L\n
29,{},Nakhon Ratchasima,L\n
30,{},Nakhon Sawan,L\n
31,{},Nakhon Si Thammarat,L\n
32,{},Nan,L\n
33,{},Narathiwat,L\n
34,{},Nong Bua Lam Phu,L\n
35,{},Nong Khai,L\n
36,{},Nonthaburi,L\n
37,{},Pathum Thani,L\n
38,{},Pattani,L\n
39,{},Phangnga,R\n
40,{},Phatthalung,R\n
41,{},Phayao,R\n
42,{},Phetchabun,R\n
43,{},Phetchaburi,R\n
44,{},Phichit,R\n
45,{},Phitsanulok,R\n
46,{},Phra Nakhon Si Ayutthaya,R\n
47,{},Phrae,R\n
48,{},Phuket,R\n
49,{},Prachin Buri,R\n
50,{},Prachuap Khiri Khan,R\n
51,{},Ranong,R\n
52,{},Ratchaburi,R\n
53,{},Rayong,R\n
54,{},Roi Et,R\n
55,{},Sa Kaeo,R\n
56,{},Sakon Nakhon,R\n
57,{},Samut Prakan,R\n
58,{},Samut Sakhon,R\n
59,{},Samut Songkhram,R\n
60,{},Saraburi,R\n
61,{},Satun,R\n
62,{},Si Sa Ket,R\n
63,{},Sing Buri,R\n
64,{},Songkhla,R\n
65,{},Sukhothai,R\n
66,{},Suphan Buri,R\n
67,{},Surat Thani,R\n
68,{},Surin,R\n
69,{},Tak,R\n
70,{},Trang,R\n
71,{},Trat,R\n
72,{},Ubon Ratchathani,R\n
73,{},Udon Thani,R\n
74,{},Uthai Thani,R\n
75,{},Uttaradit,R\n
76,{},Yala,R\n
77,{},Yasothon,R\n""".format(*values)
    
    def expect_geojson_output(self):
        return True

    def csv_to_area_string_and_colors(self, csvfile):

        return self.order_by_example(csv.reader(csvfile), "Province", 0, 1, 2, 3, ["Amnat Charoen","Ang Thong","Bangkok Metropolis","Bueng Kan","Buri Ram","Chachoengsao","Chai Nat","Chaiyaphum","Chanthaburi","Chiang Mai","Chiang Rai","Chon Buri","Chumphon","Kalasin","Kamphaeng Phet","Kanchanaburi","Khon Kaen","Krabi","Lampang","Lamphun","Loei","Lop Buri","Mae Hong Son","Maha Sarakham","Mukdahan","Nakhon Nayok","Nakhon Pathom","Nakhon Phanom","Nakhon Ratchasima","Nakhon Sawan","Nakhon Si Thammarat","Nan","Narathiwat","Nong Bua Lam Phu","Nong Khai","Nonthaburi","Pathum Thani","Pattani","Phangnga","Phatthalung","Phayao","Phetchabun","Phetchaburi","Phichit","Phitsanulok","Phra Nakhon Si Ayutthaya","Phrae","Phuket","Prachin Buri","Prachuap Khiri Khan","Ranong","Ratchaburi","Rayong","Roi Et","Sa Kaeo","Sakon Nakhon","Samut Prakan","Samut Sakhon","Samut Songkhram","Saraburi","Satun","Si Sa Ket","Sing Buri","Songkhla","Sukhothai","Suphan Buri","Surat Thani","Surin","Tak","Trang","Trat","Ubon Ratchathani","Udon Thani","Uthai Thani","Uttaradit","Yala","Yasothon"], [0.0 for i in range(0,77)], {"Amnat Charoen":"1","Ang Thong":"2","Bangkok Metropolis":"3","Bueng Kan":"4","Buri Ram":"5","Chachoengsao":"6","Chai Nat":"7","Chaiyaphum":"8","Chanthaburi":"9","Chiang Mai":"10","Chiang Rai":"11","Chon Buri":"12","Chumphon":"13","Kalasin":"14","Kamphaeng Phet":"15","Kanchanaburi":"16","Khon Kaen":"17","Krabi":"18","Lampang":"19","Lamphun":"20","Loei":"21","Lop Buri":"22","Mae Hong Son":"23","Maha Sarakham":"24","Mukdahan":"25","Nakhon Nayok":"26","Nakhon Pathom":"27","Nakhon Phanom":"28","Nakhon Ratchasima":"29","Nakhon Sawan":"30","Nakhon Si Thammarat":"31","Nan":"32","Narathiwat":"33","Nong Bua Lam Phu":"34","Nong Khai":"35","Nonthaburi":"36","Pathum Thani":"37","Pattani":"38","Phangnga":"39","Phatthalung":"40","Phayao":"41","Phetchabun":"42","Phetchaburi":"43","Phichit":"44","Phitsanulok":"45","Phra Nakhon Si Ayutthaya":"46","Phrae":"47","Phuket":"48","Prachin Buri":"49","Prachuap Khiri Khan":"50","Ranong":"51","Ratchaburi":"52","Rayong":"53","Roi Et":"54","Sa Kaeo":"55","Sakon Nakhon":"56","Samut Prakan":"57","Samut Sakhon":"58","Samut Songkhram":"59","Saraburi":"60","Satun":"61","Si Sa Ket":"62","Sing Buri":"63","Songkhla":"64","Sukhothai":"65","Suphan Buri":"66","Surat Thani":"67","Surin":"68","Tak":"69","Trang":"70","Trat":"71","Ubon Ratchathani":"72","Udon Thani":"73","Uthai Thani":"74","Uttaradit":"75","Yala":"76","Yasothon":"77"})
