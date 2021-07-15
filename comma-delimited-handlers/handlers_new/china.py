import settings
import handlers.base_handler
import csv

class CartogramHandler(handlers.base_handler.BaseCartogramHandler):

    def get_name(self):
        return "Mainland China and Taiwan"

    def selector_names(self):
        return ["China (Mainland China and Taiwan)", "Taiwan (Mainland China and Taiwan)"]

    def get_gen_file(self):
        return "{}/china_withSARandTWN_conic.gen".format(settings.CARTOGRAM_DATA_DIR)
    
    def validate_values(self, values):

        if len(values) != 34:
            return False
        
        for v in values:
            if type(v) != float:
                return False

        return True
    
    def gen_area_data(self, values):
        return """cartogram_id,Region Data,Region Name,Inset\n
1,{},Anhui AH,L\n
2,{},Beijing BJ,L\n
3,{},Chongqing CQ,L\n
4,{},Fujian FJ,L\n
5,{},Gansu GS,L\n
6,{},Guangxi GX,L\n
7,{},Guizhou GZ,L\n
8,{},Hainan HA,L\n
9,{},Hebei HEB,L\n
10,{},Heilongjiang HL,L\n
11,{},Henan HEN,L\n
12,{},Hubei HUB,L\n
13,{},Hunan HUN,L\n
14,{},Jiangsu JS,L\n
15,{},Jiangxi JX,L\n
16,{},Jilin JL,L\n
17,{},Liaoning LN,R\n
18,{},Inner Mongolia NM,R\n
19,{},Ningxia NX,R\n
20,{},Qinghai QH,R\n
21,{},Shaanxi SAA,R\n
22,{},Shandong SD,R\n
23,{},Shanghai SHG,R\n
24,{},Shanxi SAX,R\n
25,{},Sichuan SC,R\n
26,{},Tianjin TJ,R\n
27,{},Xinjiang XJ,R\n
28,{},Tibet TAR,R\n
29,{},Yunnan YN,R\n
30,{},Zhejiang ZJ,R\n
31,{},Guangdong GD,R\n
32,{},Hong Kong HK,R\n
33,{},Macau MO,R\n
34,{},Taiwan TW,R\n""".format(*values)

    def csv_to_area_string_and_colors(self, csvfile):

        return self.order_by_example(csv.reader(csvfile), "Province", 0, 1, 2, 3, ['Anhui','Beijing','Chongqing','Fujian','Gansu','Guangxi','Guizhou','Hainan','Hebei','Heilongjiang','Henan','Hubei','Hunan','Jiangsu','Jiangxi','Jilin','Liaoning','Inner Mongolia','Ningxia','Qinghai','Shaanxi','Shandong','Shanghai','Shanxi','Sichuan','Tianjin','Xinjiang','Tibet','Yunnan','Zhejiang','Guangdong','Hong Kong','Macau','Taiwan'], [0.0 for i in range(0,34)], {'Anhui':'1','Beijing':'2','Chongqing':'3','Fujian':'4','Gansu':'5','Guangxi':'6','Guizhou':'7','Hainan':'8','Hebei':'9','Heilongjiang':'10','Henan':'11','Hubei':'12','Hunan':'13','Jiangsu':'14','Jiangxi':'15','Jilin':'16','Liaoning':'17','Inner Mongolia':'18','Ningxia':'19','Qinghai':'20','Shaanxi':'21','Shandong':'22','Shanghai':'23','Shanxi':'24','Sichuan':'25','Tianjin':'26','Xinjiang':'27','Tibet':'28','Yunnan':'29','Zhejiang':'30','Guangdong':'31','Hong Kong':'32','Macau':'33','Taiwan':'34'})

