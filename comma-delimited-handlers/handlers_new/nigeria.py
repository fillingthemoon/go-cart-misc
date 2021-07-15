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
        return """cartogram_id,Region Data,Region Name,Inset\n
1,{},Abia,L\n
2,{},Adamawa,L\n
3,{},Akwa Ibom,L\n
4,{},Anambra,L\n
5,{},Bauchi,L\n
6,{},Bayelsa,L\n
7,{},Benue,L\n
8,{},Borno,L\n
9,{},Cross River,L\n
10,{},Delta,L\n
11,{},Ebonyi,L\n
12,{},Edo,L\n
13,{},Ekiti,L\n
14,{},Enugu,L\n
15,{},Federal Capital Territory,L\n
16,{},Gombe,L\n
17,{},Imo,L\n
18,{},Jigawa,L\n
19,{},Kaduna,R\n
20,{},Kano,R\n
21,{},Katsina,R\n
22,{},Kebbi,R\n
23,{},Kogi,R\n
24,{},Kwara,R\n
25,{},Lagos,R\n
26,{},Nassarawa,R\n
27,{},Niger,R\n
28,{},Ogun,R\n
29,{},Ondo,R\n
30,{},Osun,R\n
31,{},Oyo,R\n
32,{},Plateau,R\n
33,{},Rivers,R\n
34,{},Sokoto,R\n
35,{},Taraba,R\n
36,{},Yobe,R\n
37,{},Zamfara,R\n""".format(*values)
    
    def expect_geojson_output(self):
        return True

    def csv_to_area_string_and_colors(self, csvfile):

        return self.order_by_example(csv.reader(csvfile), "Region", 0, 1, 2, 3, ["Abia","Adamawa","Akwa Ibom","Anambra","Bauchi","Bayelsa","Benue","Borno","Cross River","Delta","Ebonyi","Edo","Ekiti","Enugu","Federal Capital Territory","Gombe","Imo","Jigawa","Kaduna","Kano","Katsina","Kebbi","Kogi","Kwara","Lagos","Nassarawa","Niger","Ogun","Ondo","Osun","Oyo","Plateau","Rivers","Sokoto","Taraba","Yobe","Zamfara"], [0.0 for i in range(0,37)], {"Abia":"1","Adamawa":"2","Akwa Ibom":"3","Anambra":"4","Bauchi":"5","Bayelsa":"6","Benue":"7","Borno":"8","Cross River":"9","Delta":"10","Ebonyi":"11","Edo":"12","Ekiti":"13","Enugu":"14","Federal Capital Territory":"15","Gombe":"16","Imo":"17","Jigawa":"18","Kaduna":"19","Kano":"20","Katsina":"21","Kebbi":"22","Kogi":"23","Kwara":"24","Lagos":"25","Nassarawa":"26","Niger":"27","Ogun":"28","Ondo":"29","Osun":"30","Oyo":"31","Plateau":"32","Rivers":"33","Sokoto":"34","Taraba":"35","Yobe":"36","Zamfara":"37"})
