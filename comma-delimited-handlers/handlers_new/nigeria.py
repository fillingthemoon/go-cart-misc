import settings
import handlers.base_handler
import csv

class CartogramHandler(handlers.base_handler.BaseCartogramHandler):

    def get_name(self):
        return "Nigeria"

    def get_gen_file(self):
        return "{}/nga_processedmap.json".format(settings.CARTOGRAM_DATA_DIR)
    
    def validate_values(self, values):

        if len(values) != 37:
            return False
        
        for v in values:
            if type(v) != float:
                return False

        return True
    
    def gen_area_data(self, values):
        return """cartogram_id,Region Data,Region Name,Inset
1,{},Abia,L
2,{},Adamawa,L
3,{},Akwa Ibom,L
4,{},Anambra,L
5,{},Bauchi,L
6,{},Bayelsa,L
7,{},Benue,L
8,{},Borno,L
9,{},Cross River,L
10,{},Delta,L
11,{},Ebonyi,L
12,{},Edo,L
13,{},Ekiti,L
14,{},Enugu,L
15,{},Federal Capital Territory,L
16,{},Gombe,L
17,{},Imo,L
18,{},Jigawa,L
19,{},Kaduna,R
20,{},Kano,R
21,{},Katsina,R
22,{},Kebbi,R
23,{},Kogi,R
24,{},Kwara,R
25,{},Lagos,R
26,{},Nassarawa,R
27,{},Niger,R
28,{},Ogun,R
29,{},Ondo,R
30,{},Osun,R
31,{},Oyo,R
32,{},Plateau,R
33,{},Rivers,R
34,{},Sokoto,R
35,{},Taraba,R
36,{},Yobe,R
37,{},Zamfara,R""".format(*values)
    
    def expect_geojson_output(self):
        return True

    def csv_to_area_string_and_colors(self, csvfile):

        return self.order_by_example(csv.reader(csvfile), "Region", 0, 1, 2, 3, ["Abia","Adamawa","Akwa Ibom","Anambra","Bauchi","Bayelsa","Benue","Borno","Cross River","Delta","Ebonyi","Edo","Ekiti","Enugu","Federal Capital Territory","Gombe","Imo","Jigawa","Kaduna","Kano","Katsina","Kebbi","Kogi","Kwara","Lagos","Nassarawa","Niger","Ogun","Ondo","Osun","Oyo","Plateau","Rivers","Sokoto","Taraba","Yobe","Zamfara"], [0.0 for i in range(0,37)], {"Abia":"1","Adamawa":"2","Akwa Ibom":"3","Anambra":"4","Bauchi":"5","Bayelsa":"6","Benue":"7","Borno":"8","Cross River":"9","Delta":"10","Ebonyi":"11","Edo":"12","Ekiti":"13","Enugu":"14","Federal Capital Territory":"15","Gombe":"16","Imo":"17","Jigawa":"18","Kaduna":"19","Kano":"20","Katsina":"21","Kebbi":"22","Kogi":"23","Kwara":"24","Lagos":"25","Nassarawa":"26","Niger":"27","Ogun":"28","Ondo":"29","Osun":"30","Oyo":"31","Plateau":"32","Rivers":"33","Sokoto":"34","Taraba":"35","Yobe":"36","Zamfara":"37"})
