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
        return """cartogram_id,Region Data,Region Name,Inset\n
1,{},Acre,L\n
2,{},Alagoas,L\n
3,{},Amapa,L\n
4,{},Amazonas,L\n
5,{},Bahia,L\n
6,{},Ceara,L\n
7,{},Distrito Federal,L\n
8,{},Espirito Santo,L\n
9,{},Goias,L\n
10,{},Maranhao,L\n
11,{},Mato Grosso,L\n
12,{},Mato Grosso do Sul,L\n
13,{},Minas Gerais,L\n
14,{},Para,R\n
15,{},Paraiba,R\n
16,{},Parana,R\n
17,{},Pernambuco,R\n
18,{},Piaui,R\n
19,{},Rio de Janeiro,R\n
20,{},Rio Grande do Norte,R\n
21,{},Rio Grande do Sul,R\n
22,{},Rondonia,R\n
23,{},Roraima,R\n
24,{},Santa Catarina,R\n
25,{},Sao Paulo,R\n
26,{},Sergipe,R\n
27,{},Tocantins,R\n
""".format(*values)

    def csv_to_area_string_and_colors(self, csvfile):

        return self.order_by_example(csv.reader(csvfile), "State", 0, 1, 2, 3, ['Acre','Alagoas','Amapa','Amazonas','Bahia','Ceara','Distrito Federal','Espirito Santo','Goias','Maranhao','Mato Grosso','Mato Grosso do Sul','Minas Gerais','Para','Paraiba','Parana','Pernambuco','Piaui','Rio de Janeiro','Rio Grande do Norte','Rio Grande do Sul','Rondonia','Roraima','Santa Catarina','Sao Paulo','Sergipe','Tocantins'
        ], [0.0 for i in range(0,27)], {'Acre':'1','Alagoas':'2','Amapa':'3','Amazonas':'4','Bahia':'5','Ceara':'6','Distrito Federal':'7','Espirito Santo':'8','Goias':'9','Maranhao':'10','Mato Grosso':'11','Mato Grosso do Sul':'12','Minas Gerais':'13','Para':'14','Paraiba':'15','Parana':'16','Pernambuco':'17','Piaui':'18','Rio de Janeiro':'19','Rio Grande do Norte':'20','Rio Grande do Sul':'21','Rondonia':'22','Roraima':'23','Santa Catarina':'24','Sao Paulo':'25','Sergipe':'26','Tocantins':'27'})

