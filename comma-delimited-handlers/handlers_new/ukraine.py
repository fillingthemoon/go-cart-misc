import settings
import handlers.base_handler
import csv

class CartogramHandler(handlers.base_handler.BaseCartogramHandler):

    def get_name(self):
        return "Ukraine"

    def get_gen_file(self):
        return "{}/ukraine_processedmap.json".format(settings.CARTOGRAM_DATA_DIR)
    
    def validate_values(self, values):

        if len(values) != 27:
            return False
        
        for v in values:
            if type(v) != float:
                return False

        return True
    
    def gen_area_data(self, values):
        return """cartogram_id,Region Data,Region Name,Inset
1,{},Cherkasy,L
2,{},Chernihiv,L
3,{},Chernivtsi,L
4,{},Crimea,L
5,{},Dnipropetrovsk,L
6,{},Donetsk,L
7,{},Ivano-Frankivsk,L
8,{},Kharkiv,L
9,{},Kherson,L
10,{},Khmelnytskyi,L
11,{},Kiev,L
12,{},Kiev City,L
13,{},Kirovohrad,L
14,{},Lviv,R
15,{},Luhansk,R
16,{},Mykolayiv,R
17,{},Odessa,R
18,{},Poltava,R
19,{},Rivne,R
20,{},Sevastopol,R
21,{},Sumy,R
22,{},Ternopil,R
23,{},Transcarpathia,R
24,{},Vinnytsya,R
25,{},Volyn,R
26,{},Zaporizhzhya,R
27,{},Zhytomyr,R""".format(*values)
    
    def expect_geojson_output(self):
        return True

    def csv_to_area_string_and_colors(self, csvfile):

        return self.order_by_example(csv.reader(csvfile), "Region", 0, 1, 2, 3, ["Cherkasy","Chernihiv","Chernivtsi","Crimea","Dnipropetrovsk","Donetsk","Ivano-Frankivsk","Kharkiv","Kherson","Khmelnytskyi","Kiev","Kiev City","Kirovohrad","Lviv","Luhansk","Mykolayiv","Odessa","Poltava","Rivne","Sevastopol","Sumy","Ternopil","Transcarpathia","Vinnytsya","Volyn","Zaporizhzhya","Zhytomyr"], [0.0 for i in range(0,27)], {"Cherkasy":"1","Chernihiv":"2","Chernivtsi":"3","Crimea":"4","Dnipropetrovsk":"5","Donetsk":"6","Ivano-Frankivsk":"7","Kharkiv":"8","Kherson":"9","Khmelnytskyi":"10","Kiev":"11","Kiev City":"12","Kirovohrad":"13","Lviv":"14","Luhansk":"15","Mykolayiv":"16","Odessa":"17","Poltava":"18","Rivne":"19","Sevastopol":"20","Sumy":"21","Ternopil":"22","Transcarpathia":"23","Vinnytsya":"24","Volyn":"25","Zaporizhzhya":"26","Zhytomyr":"27"})
