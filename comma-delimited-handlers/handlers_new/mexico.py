import settings
import handlers.base_handler
import csv

class CartogramHandler(handlers.base_handler.BaseCartogramHandler):

    def get_name(self):
        return "Mexico"

    def get_gen_file(self):
        return "{}/mex_processedmap.json".format(settings.CARTOGRAM_DATA_DIR)
    
    def validate_values(self, values):

        if len(values) != 32:
            return False
        
        for v in values:
            if type(v) != float:
                return False

        return True
    
    def gen_area_data(self, values):
        return """cartogram_id,Region Data,Region Name,Inset
1,{},Aguascalientes,L
2,{},Baja California,L
3,{},Baja California Sur,L
4,{},Campeche,L
5,{},Chiapas,L
6,{},Chihuahua,L
7,{},Coahuila,L
8,{},Colima,L
9,{},Mexico City,L
10,{},Durango,L
11,{},Guanajuato,L
12,{},Guerrero,L
13,{},Hidalgo,L
14,{},Jalisco,L
15,{},Mexico State,L
16,{},Michoacan,R
17,{},Morelos,R
18,{},Nayarit,R
19,{},Nuevo Leon,R
20,{},Oaxaca,R
21,{},Puebla,R
22,{},Queretaro,R
23,{},Quintana Roo,R
24,{},San Luis Potosi,R
25,{},Sinaloa,R
26,{},Sonora,R
27,{},Tabasco,R
28,{},Tamaulipas,R
29,{},Tlaxcala,R
30,{},Veracruz,R
31,{},Yucatan,R
32,{},Zacatecas,R""".format(*values)
    
    def expect_geojson_output(self):
        return True

    def csv_to_area_string_and_colors(self, csvfile):

        return self.order_by_example(csv.reader(csvfile), "State", 0, 1, 2, 3, ["Aguascalientes","Baja California","Baja California Sur","Campeche","Chiapas","Chihuahua","Coahuila","Colima","Mexico City","Durango","Guanajuato","Guerrero","Hidalgo","Jalisco","Mexico State","Michoacan","Morelos","Nayarit","Nuevo Leon","Oaxaca","Puebla","Queretaro","Quintana Roo","San Luis Potosi","Sinaloa","Sonora","Tabasco","Tamaulipas","Tlaxcala","Veracruz","Yucatan","Zacatecas"], [0.0 for i in range(0,32)], {"Aguascalientes":"1","Baja California":"2","Baja California Sur":"3","Campeche":"4","Chiapas":"5","Chihuahua":"6","Coahuila":"7","Colima":"8","Mexico City":"9","Durango":"10","Guanajuato":"11","Guerrero":"12","Hidalgo":"13","Jalisco":"14","Mexico State":"15","Michoacan":"16","Morelos":"17","Nayarit":"18","Nuevo Leon":"19","Oaxaca":"20","Puebla":"21","Queretaro":"22","Quintana Roo":"23","San Luis Potosi":"24","Sinaloa":"25","Sonora":"26","Tabasco":"27","Tamaulipas":"28","Tlaxcala":"29","Veracruz":"30","Yucatan":"31","Zacatecas":"32"})
