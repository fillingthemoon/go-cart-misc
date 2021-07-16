import settings
import handlers.base_handler
import csv

class CartogramHandler(handlers.base_handler.BaseCartogramHandler):

    def get_name(self):
        return "Brazil"

    def get_gen_file(self):
        return "{}/brazil_conic.gen".format(settings.CARTOGRAM_DATA_DIR)
    
    def validate_values(self, values):

        if len(values) != 27:
            return False
        
        for v in values:
            if type(v) != float:
                return False

        return True
    
    def gen_area_data(self, values):
        return """cartogram_id,Region Data,Region Name,Inset
1,{},Acre,L
2,{},Alagoas,L
3,{},Amapa,L
4,{},Amazonas,L
5,{},Bahia,L
6,{},Ceara,L
7,{},Distrito Federal,L
8,{},Espirito Santo,L
9,{},Goias,L
10,{},Maranhao,L
11,{},Mato Grosso,L
12,{},Mato Grosso do Sul,L
13,{},Minas Gerais,L
14,{},Para,R
15,{},Paraiba,R
16,{},Parana,R
17,{},Pernambuco,R
18,{},Piaui,R
19,{},Rio de Janeiro,R
20,{},Rio Grande do Norte,R
21,{},Rio Grande do Sul,R
22,{},Rondonia,R
23,{},Roraima,R
24,{},Santa Catarina,R
25,{},Sao Paulo,R
26,{},Sergipe,R
27,{},Tocantins,R
""".format(*values)

    def csv_to_area_string_and_colors(self, csvfile):

        return self.order_by_example(csv.reader(csvfile), "State", 0, 1, 2, 3, ['Acre','Alagoas','Amapa','Amazonas','Bahia','Ceara','Distrito Federal','Espirito Santo','Goias','Maranhao','Mato Grosso','Mato Grosso do Sul','Minas Gerais','Para','Paraiba','Parana','Pernambuco','Piaui','Rio de Janeiro','Rio Grande do Norte','Rio Grande do Sul','Rondonia','Roraima','Santa Catarina','Sao Paulo','Sergipe','Tocantins'
        ], [0.0 for i in range(0,27)], {'Acre':'1','Alagoas':'2','Amapa':'3','Amazonas':'4','Bahia':'5','Ceara':'6','Distrito Federal':'7','Espirito Santo':'8','Goias':'9','Maranhao':'10','Mato Grosso':'11','Mato Grosso do Sul':'12','Minas Gerais':'13','Para':'14','Paraiba':'15','Parana':'16','Pernambuco':'17','Piaui':'18','Rio de Janeiro':'19','Rio Grande do Norte':'20','Rio Grande do Sul':'21','Rondonia':'22','Roraima':'23','Santa Catarina':'24','Sao Paulo':'25','Sergipe':'26','Tocantins':'27'})

