import settings
import handlers.base_handler
import csv

class CartogramHandler(handlers.base_handler.BaseCartogramHandler):

    def get_name(self):
        return "Ireland"

    def get_gen_file(self):
        return "{}/irl_processedmap.json".format(settings.CARTOGRAM_DATA_DIR)
    
    def validate_values(self, values):

        if len(values) != 26:
            return False
        
        for v in values:
            if type(v) != float:
                return False

        return True
    
    def gen_area_data(self, values):
        return """cartogram_id,Region Data,Region Name,Inset\n
1,{},Carlow,L\n
2,{},Cavan,L\n
3,{},Clare,L\n
4,{},Cork,L\n
5,{},Donegal,L\n
6,{},Dublin,L\n
7,{},Galway,L\n
8,{},Kerry,L\n
9,{},Kildare,L\n
10,{},Kilkenny,L\n
11,{},Laoighis,L\n
12,{},Leitrim,L\n
13,{},Limerick,R\n
14,{},Longford,R\n
15,{},Louth,R\n
16,{},Mayo,R\n
17,{},Meath,R\n
18,{},Monaghan,R\n
19,{},Offaly,R\n
20,{},Roscommon,R\n
21,{},Sligo,R\n
22,{},Tipperary,R\n
23,{},Waterford,R\n
24,{},Westmeath,R\n
25,{},Wexford,R\n
26,{},Wicklow,R\n""".format(*values)
    
    def expect_geojson_output(self):
        return True

    def csv_to_area_string_and_colors(self, csvfile):

        return self.order_by_example(csv.reader(csvfile), "Region", 0, 1, 2, 3, ["Carlow","Cavan","Clare","Cork","Donegal","Dublin","Galway","Kerry","Kildare","Kilkenny","Laoighis","Leitrim","Limerick","Longford","Louth","Mayo","Meath","Monaghan","Offaly","Roscommon","Sligo","Tipperary","Waterford","Westmeath","Wexford","Wicklow"], [0.0 for i in range(0,26)], {"Carlow":"1","Cavan":"2","Clare":"3","Cork":"4","Donegal":"5","Dublin":"6","Galway":"7","Kerry":"8","Kildare":"9","Kilkenny":"10","Laoighis":"11","Leitrim":"12","Limerick":"13","Longford":"14","Louth":"15","Mayo":"16","Meath":"17","Monaghan":"18","Offaly":"19","Roscommon":"20","Sligo":"21","Tipperary":"22","Waterford":"23","Westmeath":"24","Wexford":"25","Wicklow":"26"})
