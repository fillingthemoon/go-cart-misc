import settings
import handlers.base_handler
import csv

class CartogramHandler(handlers.base_handler.BaseCartogramHandler):

    def get_name(self):
        return "Switzerland"

    def get_gen_file(self):
        return "{}/che_processedmap.json".format(settings.CARTOGRAM_DATA_DIR)
    
    def validate_values(self, values):

        if len(values) != 26:
            return False
        
        for v in values:
            if type(v) != float:
                return False

        return True
    
    def gen_area_data(self, values):
        return """cartogram_id,Region Data,Region Name,Inset
1,{},Aargau,L
2,{},Appenzell Ausserrhoden,L
3,{},Appenzell Innerrhoden,L
4,{},Basel-Landschaft,L
5,{},Basel-Stadt,L
6,{},Bern,L
7,{},Fribourg,L
8,{},Geneva,L
9,{},Glarus,L
10,{},Graubunden,L
11,{},Jura,L
12,{},Lucerne,L
13,{},Neuchatel,R
14,{},Nidwalden,R
15,{},Obwalden,R
16,{},Sankt Gallen,R
17,{},Schaffhausen,R
18,{},Schwyz,R
19,{},Solothurn,R
20,{},Thurgau,R
21,{},Ticino,R
22,{},Uri,R
23,{},Valais,R
24,{},Vaud,R
25,{},Zug,R
26,{},Zurich,R""".format(*values)
    
    def expect_geojson_output(self):
        return True

    def csv_to_area_string_and_colors(self, csvfile):

        return self.order_by_example(csv.reader(csvfile), "Region", 0, 1, 2, 3, ["Aargau","Appenzell Ausserrhoden","Appenzell Innerrhoden","Basel-Landschaft","Basel-Stadt","Bern","Fribourg","Geneva","Glarus","Graubunden","Jura","Lucerne","Neuchatel","Nidwalden","Obwalden","Sankt Gallen","Schaffhausen","Schwyz","Solothurn","Thurgau","Ticino","Uri","Valais","Vaud","Zug","Zurich"], [0.0 for i in range(0,26)], {"Aargau":"1","Appenzell Ausserrhoden":"2","Appenzell Innerrhoden":"3","Basel-Landschaft":"4","Basel-Stadt":"5","Bern":"6","Fribourg":"7","Geneva":"8","Glarus":"9","Graubunden":"10","Jura":"11","Lucerne":"12","Neuchatel":"13","Nidwalden":"14","Obwalden":"15","Sankt Gallen":"16","Schaffhausen":"17","Schwyz":"18","Solothurn":"19","Thurgau":"20","Ticino":"21","Uri":"22","Valais":"23","Vaud":"24","Zug":"25","Zurich":"26"})
