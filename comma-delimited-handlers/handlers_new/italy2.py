import settings
import handlers.base_handler
import csv

class CartogramHandler(handlers.base_handler.BaseCartogramHandler):

    def get_name(self):
        return "Italy"

    def get_gen_file(self):
        return "{}/ita2_processedmap.json".format(settings.CARTOGRAM_DATA_DIR)
    
    def validate_values(self, values):

        if len(values) != 20:
            return False
        
        for v in values:
            if type(v) != float:
                return False

        return True
    
    def gen_area_data(self, values):
        return """cartogram_id,Region Data,Region Name,Inset\n
1,{},Abruzzo,L\n
2,{},Apulia,L\n
3,{},Basilicata,L\n
4,{},Calabria,L\n
5,{},Campania,L\n
6,{},Emilia-Romagna,L\n
7,{},Friuli-Venezia Giulia,L\n
8,{},Lazio,L\n
9,{},Liguria,L\n
10,{},Lombardia,R\n
11,{},Marche,R\n
12,{},Molise,R\n
13,{},Piemonte,R\n
14,{},Sardegna,R\n
15,{},Sicily,R\n
16,{},Toscana,R\n
17,{},Trentino-Alto Adige,R\n
18,{},Umbria,R\n
19,{},Valle d'Aosta,R\n
20,{},Veneto,R\n""".format(*values)
    
    def expect_geojson_output(self):
        return True

    def csv_to_area_string_and_colors(self, csvfile):

        return self.order_by_example(csv.reader(csvfile), "Region", 0, 1, 2, 3, ["Abruzzo","Apulia","Basilicata","Calabria","Campania","Emilia-Romagna","Friuli-Venezia Giulia","Lazio","Liguria","Lombardia","Marche","Molise","Piemonte","Sardegna","Sicily","Toscana","Trentino-Alto Adige","Umbria","Valle d'Aosta","Veneto"], [0.0 for i in range(0,20)], {"Abruzzo":"1","Apulia":"2","Basilicata":"3","Calabria":"4","Campania":"5","Emilia-Romagna":"6","Friuli-Venezia Giulia":"7","Lazio":"8","Liguria":"9","Lombardia":"10","Marche":"11","Molise":"12","Piemonte":"13","Sardegna":"14","Sicily":"15","Toscana":"16","Trentino-Alto Adige":"17","Umbria":"18","Valle d'Aosta":"19","Veneto":"20"})
