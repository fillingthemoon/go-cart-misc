import settings
import handlers.base_handler
import csv

class CartogramHandler(handlers.base_handler.BaseCartogramHandler):

    def get_name(self):
        return "The Bahamas"

    def get_gen_file(self):
        return "{}/bahamas_processedmap.json".format(settings.CARTOGRAM_DATA_DIR)
    
    def validate_values(self, values):

        if len(values) != 19:
            return False
        
        for v in values:
            if type(v) != float:
                return False

        return True
    
    def gen_area_data(self, values):
        return """cartogram_id,Region Data,Region Name,Inset\n
1,{},Abaco,L\n
2,{},Acklins,L\n
3,{},Andros,L\n
4,{},Berry Islands,L\n
5,{},Bimini,L\n
6,{},Cat Island,L\n
7,{},Crooked Island,L\n
8,{},Eleuthera,L\n
9,{},Exuma,L\n
10,{},Grand Bahama,R\n
11,{},Harbour Island,R\n
12,{},Inagua,R\n
13,{},Long Island,R\n
14,{},Mayaguana,R\n
15,{},New Providence,R\n
16,{},Ragged Islands,R\n
17,{},Rum Cay,R\n
18,{},San Salvador,R\n
19,{},Spanish Wells,R\n""".format(*values)
    
    def expect_geojson_output(self):
        return True

    def csv_to_area_string_and_colors(self, csvfile):

        return self.order_by_example(csv.reader(csvfile), "Island", 0, 1, 2, 3, ["Abaco","Acklins","Andros","Berry Islands","Bimini","Cat Island","Crooked Island","Eleuthera","Exuma","Grand Bahama","Harbour Island","Inagua","Long Island","Mayaguana","New Providence","Ragged Islands","Rum Cay","San Salvador","Spanish Wells"], [0.0 for i in range(0,19)], {"Abaco":"1","Acklins":"2","Andros":"3","Berry Islands":"4","Bimini":"5","Cat Island":"6","Crooked Island":"7","Eleuthera":"8","Exuma":"9","Grand Bahama":"10","Harbour Island":"11","Inagua":"12","Long Island":"13","Mayaguana":"14","New Providence":"15","Ragged Islands":"16","Rum Cay":"17","San Salvador":"18","Spanish Wells":"19"})
