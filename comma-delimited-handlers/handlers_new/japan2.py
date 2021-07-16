import settings
import handlers.base_handler
import csv

class CartogramHandler(handlers.base_handler.BaseCartogramHandler):

    def get_name(self):
        return "Japan"

    def get_gen_file(self):
        return "{}/jpn2_processedmap.json".format(settings.CARTOGRAM_DATA_DIR)
    
    def validate_values(self, values):

        if len(values) != 47:
            return False
        
        for v in values:
            if type(v) != float:
                return False

        return True
    
    def gen_area_data(self, values):
        return """cartogram_id,Region Data,Region Name,Inset
1,{},Aichi,L
2,{},Akita,L
3,{},Aomori,L
4,{},Chiba,L
5,{},Ehime,L
6,{},Fukui,L
7,{},Fukuoka,L
8,{},Fukushima,L
9,{},Gifu,L
10,{},Gunma,L
11,{},Hiroshima,L
12,{},Hokkaido,L
13,{},Hyogo,L
14,{},Ibaraki,L
15,{},Ishikawa,L
16,{},Iwate,L
17,{},Kagawa,L
18,{},Kagoshima,L
19,{},Kanagawa,L
20,{},Kochi,L
21,{},Kumamoto,L
22,{},Kyoto,L
23,{},Mie,L
24,{},Miyagi,R
25,{},Miyazaki,R
26,{},Nagano,R
27,{},Nagasaki,R
28,{},Nara,R
29,{},Niigata,R
30,{},Oita,R
31,{},Okayama,R
32,{},Okinawa,R
33,{},Osaka,R
34,{},Saga,R
35,{},Saitama,R
36,{},Shiga,R
37,{},Shimane,R
38,{},Shizuoka,R
39,{},Tochigi,R
40,{},Tokushima,R
41,{},Tokyo,R
42,{},Tottori,R
43,{},Toyama,R
44,{},Wakayama,R
45,{},Yamagata,R
46,{},Yamaguchi,R
47,{},Yamanashi,R""".format(*values)
    
    def expect_geojson_output(self):
        return True

    def csv_to_area_string_and_colors(self, csvfile):

        return self.order_by_example(csv.reader(csvfile), "Prefectures", 0, 1, 2, 3, ["Aichi","Akita","Aomori","Chiba","Ehime","Fukui","Fukuoka","Fukushima","Gifu","Gunma","Hiroshima","Hokkaido","Hyogo","Ibaraki","Ishikawa","Iwate","Kagawa","Kagoshima","Kanagawa","Kochi","Kumamoto","Kyoto","Mie","Miyagi","Miyazaki","Nagano","Nagasaki","Nara","Niigata","Oita","Okayama","Okinawa","Osaka","Saga","Saitama","Shiga","Shimane","Shizuoka","Tochigi","Tokushima","Tokyo","Tottori","Toyama","Wakayama","Yamagata","Yamaguchi","Yamanashi"], [0.0 for i in range(0,47)], {"Aichi":"1","Akita":"2","Aomori":"3","Chiba":"4","Ehime":"5","Fukui":"6","Fukuoka":"7","Fukushima":"8","Gifu":"9","Gunma":"10","Hiroshima":"11","Hokkaido":"12","Hyogo":"13","Ibaraki":"14","Ishikawa":"15","Iwate":"16","Kagawa":"17","Kagoshima":"18","Kanagawa":"19","Kochi":"20","Kumamoto":"21","Kyoto":"22","Mie":"23","Miyagi":"24","Miyazaki":"25","Nagano":"26","Nagasaki":"27","Nara":"28","Niigata":"29","Oita":"30","Okayama":"31","Okinawa":"32","Osaka":"33","Saga":"34","Saitama":"35","Shiga":"36","Shimane":"37","Shizuoka":"38","Tochigi":"39","Tokushima":"40","Tokyo":"41","Tottori":"42","Toyama":"43","Wakayama":"44","Yamagata":"45","Yamaguchi":"46","Yamanashi":"47"})
