import settings
import handlers.base_handler
import csv

class CartogramHandler(handlers.base_handler.BaseCartogramHandler):

    def get_name(self):
        return "Sri Lanka"

    def get_gen_file(self):
        return "{}/gadm36_LKA_1.gen".format(settings.CARTOGRAM_DATA_DIR)
    
    def validate_values(self, values):

        if len(values) != 25:
            return False
        
        for v in values:
            if type(v) != float:
                return False

        return True
    
    def gen_area_data(self, values):
        return """cartogram_id,Region Data,Region Name,Inset\n
1,{},Ampara,L\n
2,{},Anuradhapura,L\n
3,{},Badulla,L\n
4,{},Batticaloa,L\n
5,{},Colombo,L\n
6,{},Galle,L\n
7,{},Gampaha,L\n
8,{},Hambantota,L\n
9,{},Jaffna,L\n
10,{},Kalutara,L\n
11,{},Kandy,L\n
12,{},Kegalle,L\n
13,{},Kilinochchi,R\n
14,{},Kurunegala,R\n
15,{},Mannar,R\n
16,{},Matale,R\n
17,{},Matara,R\n
18,{},Moneragala,R\n
19,{},Mullaitivu,R\n
20,{},Nuwara Eliya,R\n
21,{},Polonnaruwa,R\n
22,{},Puttalam,R\n
23,{},Ratnapura,R\n
24,{},Trincomalee,R\n
25,{},Vavuniya,R\n""".format(*values)
    
    def remove_holes(self):
        return True

    def csv_to_area_string_and_colors(self, csvfile):

        return self.order_by_example(csv.reader(csvfile), "District", 0, 1, 2, 3, ["Ampara","Anuradhapura","Badulla","Batticaloa","Colombo","Galle","Gampaha","Hambantota","Jaffna","Kalutara","Kandy","Kegalle","Kilinochchi","Kurunegala","Mannar","Matale","Matara","Moneragala","Mullaitivu","Nuwara Eliya","Polonnaruwa","Puttalam","Ratnapura","Trincomalee","Vavuniya"], [0.0 for i in range(0,25)], {"Ampara":"1","Anuradhapura":"2","Badulla":"3","Batticaloa":"4","Colombo":"5","Galle":"6","Gampaha":"7","Hambantota":"8","Jaffna":"9","Kalutara":"10","Kandy":"11","Kegalle":"12","Kilinochchi":"13","Kurunegala":"14","Mannar":"15","Matale":"16","Matara":"17","Moneragala":"18","Mullaitivu":"19","Nuwara Eliya":"20","Polonnaruwa":"21","Puttalam":"22","Ratnapura":"23","Trincomalee":"24","Vavuniya":"25"})
