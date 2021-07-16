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
        return """cartogram_id,Region Data,Region Name,Inset
1,{},Carlow,L
2,{},Cavan,L
3,{},Clare,L
4,{},Cork,L
5,{},Donegal,L
6,{},Dublin,L
7,{},Galway,L
8,{},Kerry,L
9,{},Kildare,L
10,{},Kilkenny,L
11,{},Laoighis,L
12,{},Leitrim,L
13,{},Limerick,R
14,{},Longford,R
15,{},Louth,R
16,{},Mayo,R
17,{},Meath,R
18,{},Monaghan,R
19,{},Offaly,R
20,{},Roscommon,R
21,{},Sligo,R
22,{},Tipperary,R
23,{},Waterford,R
24,{},Westmeath,R
25,{},Wexford,R
26,{},Wicklow,R""".format(*values)
    
    def expect_geojson_output(self):
        return True

    def csv_to_area_string_and_colors(self, csvfile):

        return self.order_by_example(csv.reader(csvfile), "Region", 0, 1, 2, 3, ["Carlow","Cavan","Clare","Cork","Donegal","Dublin","Galway","Kerry","Kildare","Kilkenny","Laoighis","Leitrim","Limerick","Longford","Louth","Mayo","Meath","Monaghan","Offaly","Roscommon","Sligo","Tipperary","Waterford","Westmeath","Wexford","Wicklow"], [0.0 for i in range(0,26)], {"Carlow":"1","Cavan":"2","Clare":"3","Cork":"4","Donegal":"5","Dublin":"6","Galway":"7","Kerry":"8","Kildare":"9","Kilkenny":"10","Laoighis":"11","Leitrim":"12","Limerick":"13","Longford":"14","Louth":"15","Mayo":"16","Meath":"17","Monaghan":"18","Offaly":"19","Roscommon":"20","Sligo":"21","Tipperary":"22","Waterford":"23","Westmeath":"24","Wexford":"25","Wicklow":"26"})
