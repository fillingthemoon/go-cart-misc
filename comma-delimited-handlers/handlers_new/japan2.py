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
        return """cartogram_id,Region Data,Region Name,Inset\n
1,{},Aichi,L\n
2,{},Akita,L\n
3,{},Aomori,L\n
4,{},Chiba,L\n
5,{},Ehime,L\n
6,{},Fukui,L\n
7,{},Fukuoka,L\n
8,{},Fukushima,L\n
9,{},Gifu,L\n
10,{},Gunma,L\n
11,{},Hiroshima,L\n
12,{},Hokkaido,L\n
13,{},Hyogo,L\n
14,{},Ibaraki,L\n
15,{},Ishikawa,L\n
16,{},Iwate,L\n
17,{},Kagawa,L\n
18,{},Kagoshima,L\n
19,{},Kanagawa,L\n
20,{},Kochi,L\n
21,{},Kumamoto,L\n
22,{},Kyoto,L\n
23,{},Mie,L\n
24,{},Miyagi,R\n
25,{},Miyazaki,R\n
26,{},Nagano,R\n
27,{},Nagasaki,R\n
28,{},Nara,R\n
29,{},Niigata,R\n
30,{},Oita,R\n
31,{},Okayama,R\n
32,{},Okinawa,R\n
33,{},Osaka,R\n
34,{},Saga,R\n
35,{},Saitama,R\n
36,{},Shiga,R\n
37,{},Shimane,R\n
38,{},Shizuoka,R\n
39,{},Tochigi,R\n
40,{},Tokushima,R\n
41,{},Tokyo,R\n
42,{},Tottori,R\n
43,{},Toyama,R\n
44,{},Wakayama,R\n
45,{},Yamagata,R\n
46,{},Yamaguchi,R\n
47,{},Yamanashi,R\n""".format(*values)
    
    def expect_geojson_output(self):
        return True

    def csv_to_area_string_and_colors(self, csvfile):

        return self.order_by_example(csv.reader(csvfile), "Prefectures", 0, 1, 2, 3, ["Aichi","Akita","Aomori","Chiba","Ehime","Fukui","Fukuoka","Fukushima","Gifu","Gunma","Hiroshima","Hokkaido","Hyogo","Ibaraki","Ishikawa","Iwate","Kagawa","Kagoshima","Kanagawa","Kochi","Kumamoto","Kyoto","Mie","Miyagi","Miyazaki","Nagano","Nagasaki","Nara","Niigata","Oita","Okayama","Okinawa","Osaka","Saga","Saitama","Shiga","Shimane","Shizuoka","Tochigi","Tokushima","Tokyo","Tottori","Toyama","Wakayama","Yamagata","Yamaguchi","Yamanashi"], [0.0 for i in range(0,47)], {"Aichi":"1","Akita":"2","Aomori":"3","Chiba":"4","Ehime":"5","Fukui":"6","Fukuoka":"7","Fukushima":"8","Gifu":"9","Gunma":"10","Hiroshima":"11","Hokkaido":"12","Hyogo":"13","Ibaraki":"14","Ishikawa":"15","Iwate":"16","Kagawa":"17","Kagoshima":"18","Kanagawa":"19","Kochi":"20","Kumamoto":"21","Kyoto":"22","Mie":"23","Miyagi":"24","Miyazaki":"25","Nagano":"26","Nagasaki":"27","Nara":"28","Niigata":"29","Oita":"30","Okayama":"31","Okinawa":"32","Osaka":"33","Saga":"34","Saitama":"35","Shiga":"36","Shimane":"37","Shizuoka":"38","Tochigi":"39","Tokushima":"40","Tokyo":"41","Tottori":"42","Toyama":"43","Wakayama":"44","Yamagata":"45","Yamaguchi":"46","Yamanashi":"47"})
