import settings
import handlers.base_handler
import csv

class CartogramHandler(handlers.base_handler.BaseCartogramHandler):

    def get_name(self):
        return "Sweden"

    def get_gen_file(self):
        return "{}/swe_processedmap.json".format(settings.CARTOGRAM_DATA_DIR)
    
    def validate_values(self, values):

        if len(values) != 21:
            return False
        
        for v in values:
            if type(v) != float:
                return False

        return True
    
    def gen_area_data(self, values):
        return """cartogram_id,Region Data,Region Name,Inset
2,{},Dalarna,L
3,{},Gavleborg,L
4,{},Gotland,L
5,{},Halland,L
6,{},Jamtland,L
7,{},Jonkoping,L
8,{},Kalmar,L
9,{},Kronoberg,L
10,{},Norrbotten,L
11,{},Orebro,L
12,{},Ostergotland,R
1,{},Blekinge,R
14,{},Sodermanland,R
13,{},Skane,R
15,{},Stockholm,R
16,{},Uppsala,R
17,{},Varmland,R
18,{},Vasterbotten,R
19,{},Vasternorrland,R
20,{},Vastmanland,R
21,{},Vastra Gotaland,R""".format(*values)
    
    def expect_geojson_output(self):
        return True

    def csv_to_area_string_and_colors(self, csvfile):

        return self.order_by_example(csv.reader(csvfile), "Region", 0, 1, 2, 3, ["Dalarna","Gavleborg","Gotland","Halland","Jamtland","Jonkoping","Kalmar","Kronoberg","Norrbotten","Orebro","Ostergotland","Blekinge","Sodermanland","Skane","Stockholm","Uppsala","Varmland","Vasterbotten","Vasternorrland","Vastmanland","Vastra Gotaland"], [0.0 for i in range(0,21)], {"Dalarna":"2","Gavleborg":"3","Gotland":"4","Halland":"5","Jamtland":"6","Jonkoping":"7","Kalmar":"8","Kronoberg":"9","Norrbotten":"10","Orebro":"11","Ostergotland":"12","Blekinge":"1","Sodermanland":"14","Skane":"13","Stockholm":"15","Uppsala":"16","Varmland":"17","Vasterbotten":"18","Vasternorrland":"19","Vastmanland":"20","Vastra Gotaland":"21"})
