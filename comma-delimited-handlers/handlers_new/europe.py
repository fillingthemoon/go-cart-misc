import settings
import handlers.base_handler
import csv

class CartogramHandler(handlers.base_handler.BaseCartogramHandler):

    def get_name(self):
        return "Europe (Eurostat members)"

    def get_gen_file(self):
        return "{}/europe_processedmap.json".format(settings.CARTOGRAM_DATA_DIR)
    
    def validate_values(self, values):

        if len(values) != 35:
            return False
        
        for v in values:
            if type(v) != float:
                return False

        return True
    
    def gen_area_data(self, values):
        return """cartogram_id,Region Data,Region Name,Inset\n
1,{},Austria,L\n
2,{},Belgium,L\n
3,{},Bosnia and Herzegovina,L\n
4,{},Bulgaria,L\n
5,{},Croatia,L\n
6,{},Czech Republic,L\n
7,{},Denmark,L\n
8,{},Estonia,L\n
9,{},Finland,L\n
10,{},France,L\n
11,{},Germany,L\n
12,{},Greece,L\n
13,{},Hungary,L\n
14,{},Iceland,L\n
15,{},Ireland,L\n
16,{},Italy,L\n
17,{},Latvia,L\n
18,{},Liechtenstein,R\n
19,{},Lithuania,R\n
20,{},Luxembourg,R\n
21,{},Malta,R\n
22,{},Netherlands,R\n
23,{},North Macedonia,R\n
24,{},Norway,R\n
25,{},Poland,R\n
26,{},Portugal,R\n
27,{},Republic of Cyprus,R\n
28,{},Republic of Serbia,R\n
29,{},Romania,R\n
30,{},Slovakia,R\n
31,{},Slovenia,R\n
32,{},Spain,R\n
33,{},Sweden,R\n
34,{},Switzerland,R\n
35,{},United Kingdom,R\n""".format(*values)
    
    def expect_geojson_output(self):
        return True

    def csv_to_area_string_and_colors(self, csvfile):

        return self.order_by_example(csv.reader(csvfile), "Country", 0, 1, 2, 3, ["Austria","Belgium","Bosnia and Herzegovina","Bulgaria","Croatia","Czech Republic","Denmark","Estonia","Finland","France","Germany","Greece","Hungary","Iceland","Ireland","Italy","Latvia","Liechtenstein","Lithuania","Luxembourg","Malta","Netherlands","North Macedonia","Norway","Poland","Portugal","Republic of Cyprus","Republic of Serbia","Romania","Slovakia","Slovenia","Spain","Sweden","Switzerland","United Kingdom"], [0.0 for i in range(0,35)], {"Austria":"1","Belgium":"2","Bosnia and Herzegovina":"3","Bulgaria":"4","Croatia":"5","Czech Republic":"6","Denmark":"7","Estonia":"8","Finland":"9","France":"10","Germany":"11","Greece":"12","Hungary":"13","Iceland":"14","Ireland":"15","Italy":"16","Latvia":"17","Liechtenstein":"18","Lithuania":"19","Luxembourg":"20","Malta":"21","Netherlands":"22","North Macedonia":"23","Norway":"24","Poland":"25","Portugal":"26","Republic of Cyprus":"27","Republic of Serbia":"28","Romania":"29","Slovakia":"30","Slovenia":"31","Spain":"32","Sweden":"33","Switzerland":"34","United Kingdom":"35"})
