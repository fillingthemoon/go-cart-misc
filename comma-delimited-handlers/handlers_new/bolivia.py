import settings
import handlers.base_handler
import csv

class CartogramHandler(handlers.base_handler.BaseCartogramHandler):

    def get_name(self):
        return "Bolivia"

    def get_gen_file(self):
        return "{}/bol_processedmap.json".format(settings.CARTOGRAM_DATA_DIR)
    
    def validate_values(self, values):

        if len(values) != 9:
            return False
        
        for v in values:
            if type(v) != float:
                return False

        return True
    
    def gen_area_data(self, values):
        return """cartogram_id,Region Data,Region Name,Inset\n
1,{},Chuquisaca,L\n
2,{},Cochabamba,L\n
3,{},Beni,L\n
4,{},La Paz,L\n
5,{},Oruro,R\n
6,{},Pando,R\n
7,{},Potosi,R\n
8,{},Santa Cruz,R\n
9,{},Tarija,R\n""".format(*values)
    
    def expect_geojson_output(self):
        return True

    def csv_to_area_string_and_colors(self, csvfile):

        return self.order_by_example(csv.reader(csvfile), "Department", 0, 1, 2, 3, ["Chuquisaca","Cochabamba","Beni","La Paz","Oruro","Pando","Potosi","Santa Cruz","Tarija"], [0.0 for i in range(0,9)], {"Chuquisaca":"1","Cochabamba":"2","Beni":"3","La Paz":"4","Oruro":"5","Pando":"6","Potosi":"7","Santa Cruz":"8","Tarija":"9"})
