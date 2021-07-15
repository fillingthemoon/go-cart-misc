import settings
import handlers.base_handler
import csv

class CartogramHandler(handlers.base_handler.BaseCartogramHandler):

    def get_name(self):
        return "Ethiopia"

    def get_gen_file(self):
        return "{}/eth_processedmap.json".format(settings.CARTOGRAM_DATA_DIR)
    
    def validate_values(self, values):

        if len(values) != 11:
            return False
        
        for v in values:
            if type(v) != float:
                return False

        return True
    
    def gen_area_data(self, values):
        return """cartogram_id,Region Data,Region Name,Inset\n
1,{},Addis Abeba,L\n
2,{},Afar,L\n
3,{},Amhara,L\n
4,{},Benshangul-Gumaz,L\n
5,{},Dire Dawa,L\n
6,{},Gambela,R\n
7,{},Harari,R\n
8,{},Oromia,R\n
9,{},Somali,R\n
10,{},Southern Nations, Nationalities and Peoples,R\n
11,{},Tigray,R\n""".format(*values)
    
    def expect_geojson_output(self):
        return True

    def csv_to_area_string_and_colors(self, csvfile):

        return self.order_by_example(csv.reader(csvfile), "Region", 0, 1, 2, 3, ["Addis Abeba","Afar","Amhara","Benshangul-Gumaz","Dire Dawa","Gambela","Harari","Oromia","Somali","Southern Nations, Nationalities and Peoples","Tigray"], [0.0 for i in range(0,11)], {"Addis Abeba":"1","Afar":"2","Amhara":"3","Benshangul-Gumaz":"4","Dire Dawa":"5","Gambela":"6","Harari":"7","Oromia":"8","Somali":"9","Southern Nations, Nationalities and Peoples":"10","Tigray":"11"})
