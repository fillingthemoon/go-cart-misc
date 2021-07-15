import settings
import handlers.base_handler
import csv

class CartogramHandler(handlers.base_handler.BaseCartogramHandler):

    def get_name(self):
        return "Germany"

    def get_gen_file(self):
        return "{}/germany_conic.gen".format(settings.CARTOGRAM_DATA_DIR)
    
    def validate_values(self, values):

        if len(values) != 16:
            return False
        
        for v in values:
            if type(v) != float:
                return False

        return True
    
    def gen_area_data(self, values):
        return """cartogram_id,Region Data,Region Name,Inset\n
1,{},Hamburg HH,L\n
2,{},Niedersachsen NI,L\n
3,{},Bremen HB,L\n
4,{},Nordrhein-Westfalen NW,L\n
5,{},Hessen HE,L\n
6,{},Rheinland-Pfalz RP,L\n
7,{},Baden-Wuerttemberg BW,L\n
8,{},Bayern BY,R\n
9,{},Saarland SL,R\n
10,{},Berlin BE,R\n
11,{},Brandenburg BB,R\n
12,{},Mecklenburg-Vorpommern MV,R\n
13,{},Sachsen SN,R\n
14,{},Sachsen-Anhalt ST,R\n
15,{},Thueringen TH,R\n
16,{},Schleswig-Holstein SH,R\n
""".format(*values)

    def csv_to_area_string_and_colors(self, csvfile):

        return self.order_by_example(csv.reader(csvfile), "State", 0, 1, 2, 3, ['Hamburg','Niedersachsen','Bremen','Nordrhein-Westfalen','Hessen','Rheinland-Pfalz','Baden-Wuerttemberg','Bayern','Saarland','Berlin','Brandenburg','Mecklenburg-Vorpommern','Sachsen','Sachsen-Anhalt','Thueringen','Schleswig-Holstein'
        ], [0.0 for i in range(0,16)], {'Hamburg':'1','Niedersachsen':'2','Bremen':'3','Nordrhein-Westfalen':'4','Hessen':'5','Rheinland-Pfalz':'6','Baden-Wuerttemberg':'7','Bayern':'8','Saarland':'9','Berlin':'10','Brandenburg':'11','Mecklenburg-Vorpommern':'12','Sachsen':'13','Sachsen-Anhalt':'14','Thueringen':'15','Schleswig-Holstein':'16'})

