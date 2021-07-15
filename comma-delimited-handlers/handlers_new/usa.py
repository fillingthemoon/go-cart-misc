import settings
import handlers.base_handler
import csv

class CartogramHandler(handlers.base_handler.BaseCartogramHandler):

    def get_name(self):
        return "Conterminous United States"

    def selector_names(self):
        return ["United States (Conterminous)"]

    def get_gen_file(self):
        return "{}/usa_low48conic.gen".format(settings.CARTOGRAM_DATA_DIR)
    
    def validate_values(self, values):

        if len(values) != 49:
            return False
        
        for v in values:
            if type(v) != float:
                return False

        return True
    
    def gen_area_data(self, values):
        return """cartogram_id,Region Data,Region Name,Inset\n
43,{},Alabama,L\n
37,{},Arizona,L\n
47,{},Arkansas,L\n
25,{},California,L\n
32,{},Colorado,L\n
19,{},Connecticut,L\n
29,{},Delaware,L\n
28,{},District of Columbia,L\n
49,{},Florida,L\n
45,{},Georgia,L\n
9,{},Idaho,L\n
27,{},Illinois,L\n
22,{},Indiana,L\n
14,{},Iowa,L\n
34,{},Kansas,L\n
33,{},Kentucky,L\n
48,{},Louisiana,L\n
4,{},Maine,L\n
31,{},Maryland,L\n
15,{},Massachusetts,L\n
50,{},Michigan,L\n
11,{},Minnesota,L\n
44,{},Mississippi,L\n
36,{},Missouri,L\n
3,{},Montana,R\n
16,{},Nebraska,R\n
23,{},Nevada,R\n
13,{},New Hampshire,R\n
21,{},New Jersey,R\n
42,{},New Mexico,R\n
17,{},New York,R\n
39,{},North Carolina,R\n
5,{},North Dakota,R\n
26,{},Ohio,R\n
38,{},Oklahoma,R\n
12,{},Oregon,R\n
18,{},Pennsylvania,R\n
20,{},Rhode Island,R\n
46,{},South Carolina,R\n
6,{},South Dakota,R\n
40,{},Tennessee,R\n
41,{},Texas,R\n
24,{},Utah,R\n
10,{},Vermont,R\n
35,{},Virginia,R\n
2,{},Washington,R\n
30,{},West Virginia,R\n
8,{},Wisconsin,R\n
7,{},Wyoming,R\n""".format(*values)

    def csv_to_area_string_and_colors(self, csvfile):

        return self.order_by_example(csv.reader(csvfile), "State", 0, 1, 2, 3, [
            'Alabama', 'Arizona', 'Arkansas', 'California', 'Colorado', 'Connecticut', 'Delaware',
            'District of Columbia', 'Florida', 'Georgia', 'Idaho', 'Illinois', 'Indiana', 'Iowa',
            'Kansas', 'Kentucky', 'Louisiana', 'Maine', 'Maryland', 'Massachusetts', 'Michigan',
            'Minnesota', 'Mississippi', 'Missouri', 'Montana', 'Nebraska', 'Nevada', 'New Hampshire',
            'New Jersey', 'New Mexico', 'New York', 'North Carolina', 'North Dakota', 'Ohio', 'Oklahoma', 'Oregon', 'Pennsylvania', 'Rhode Island', 'South Carolina', 'South Dakota', 'Tennessee', 'Texas', 'Utah',          'Vermont', 'Virginia', 'Washington', 'West Virginia', 'Wisconsin', 'Wyoming'
        ], [0.0 for i in range(0,49)], {'Alabama': '43','Arizona': '37','Arkansas': '47','California': '25','Colorado': '32','Connecticut': '19','Delaware': '29','District of Columbia': '28','Florida': '49','Georgia': '45','Idaho': '9','Illinois': '27','Indiana': '22','Iowa': '14','Kansas': '34','Kentucky': '33','Louisiana': '48','Maine': '4','Maryland': '31','Massachusetts': '15','Michigan': '50','Minnesota': '11','Mississippi': '44','Missouri': '36','Montana': '3','Nebraska': '16','Nevada': '23','New Hampshire': '13','New Jersey': '21','New Mexico': '42','New York': '17','North Carolina': '39','North Dakota': '5','Ohio': '26','Oklahoma': '38','Oregon': '12','Pennsylvania': '18','Rhode Island': '20','South Carolina': '46','South Dakota': '6','Tennessee': '40','Texas': '41','Utah': '24','Vermont': '10','Virginia': '35','Washington': '2','West Virginia': '30','Wisconsin': '8','Wyoming': '7'})

