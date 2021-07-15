import settings
import handlers.base_handler
import csv

class CartogramHandler(handlers.base_handler.BaseCartogramHandler):

    def get_name(self):
        return "Philippines"

    def get_gen_file(self):
        return "{}/phl_processedmap.json".format(settings.CARTOGRAM_DATA_DIR)
    
    def validate_values(self, values):

        if len(values) != 82:
            return False
        
        for v in values:
            if type(v) != float:
                return False

        return True
    
    def gen_area_data(self, values):
        return """cartogram_id,Region Data,Region Name,Inset\n
1,{},Abra,L\n
2,{},Agusan del Norte,L\n
3,{},Agusan del Sur,L\n
4,{},Aklan,L\n
5,{},Albay,L\n
6,{},Antique,L\n
7,{},Apayao,L\n
8,{},Aurora,L\n
9,{},Basilan,L\n
10,{},Bataan,L\n
11,{},Batanes,L\n
12,{},Batangas,L\n
13,{},Benguet,L\n
14,{},Biliran,L\n
15,{},Bohol,L\n
16,{},Bukidnon,L\n
17,{},Bulacan,L\n
18,{},Cagayan,L\n
19,{},Camarines Norte,L\n
20,{},Camarines Sur,L\n
21,{},Camiguin,L\n
22,{},Capiz,L\n
23,{},Catanduanes,L\n
24,{},Cavite,L\n
25,{},Cebu,L\n
26,{},Compostela Valley,L\n
27,{},Davao del Norte,L\n
28,{},Davao del Sur,L\n
29,{},Davao Occidental,L\n
30,{},Davao Oriental,L\n
31,{},Dinagat Islands,L\n
32,{},Eastern Samar,L\n
33,{},Guimaras,L\n
34,{},Ifugao,L\n
35,{},Ilocos Norte,L\n
36,{},Ilocos Sur,L\n
37,{},Iloilo,L\n
38,{},Isabela,L\n
39,{},Kalinga,L\n
40,{},La Union,L\n
41,{},Laguna,R\n
42,{},Lanao del Norte,R\n
43,{},Lanao del Sur,R\n
44,{},Leyte,R\n
45,{},Maguindanao,R\n
46,{},Marinduque,R\n
47,{},Masbate,R\n
48,{},Metropolitan Manila,R\n
49,{},Misamis Occidental,R\n
50,{},Misamis Oriental,R\n
51,{},Mountain Province,R\n
52,{},Negros Occidental,R\n
53,{},Negros Oriental,R\n
54,{},North Cotabato,R\n
55,{},Northern Samar,R\n
56,{},Nueva Ecija,R\n
57,{},Nueva Vizcaya,R\n
58,{},Occidental Mindoro,R\n
59,{},Oriental Mindoro,R\n
60,{},Palawan,R\n
61,{},Pampanga,R\n
62,{},Pangasinan,R\n
63,{},Quezon,R\n
64,{},Quirino,R\n
65,{},Rizal,R\n
66,{},Romblon,R\n
67,{},Samar,R\n
68,{},Sarangani,R\n
69,{},Siquijor,R\n
70,{},Sorsogon,R\n
71,{},South Cotabato,R\n
72,{},Southern Leyte,R\n
73,{},Sultan Kudarat,R\n
74,{},Sulu,R\n
75,{},Surigao del Norte,R\n
76,{},Surigao del Sur,R\n
77,{},Tarlac,R\n
78,{},Tawi-Tawi,R\n
79,{},Zambales,R\n
80,{},Zamboanga del Norte,R\n
81,{},Zamboanga del Sur,R\n
82,{},Zamboanga Sibugay,R\n""".format(*values)
    
    def expect_geojson_output(self):
        return True

    def csv_to_area_string_and_colors(self, csvfile):

        return self.order_by_example(csv.reader(csvfile), "Province/Region", 0, 1, 2, 3, ["Abra","Agusan del Norte","Agusan del Sur","Aklan","Albay","Antique","Apayao","Aurora","Basilan","Bataan","Batanes","Batangas","Benguet","Biliran","Bohol","Bukidnon","Bulacan","Cagayan","Camarines Norte","Camarines Sur","Camiguin","Capiz","Catanduanes","Cavite","Cebu","Compostela Valley","Davao del Norte","Davao del Sur","Davao Occidental","Davao Oriental","Dinagat Islands","Eastern Samar","Guimaras","Ifugao","Ilocos Norte","Ilocos Sur","Iloilo","Isabela","Kalinga","La Union","Laguna","Lanao del Norte","Lanao del Sur","Leyte","Maguindanao","Marinduque","Masbate","Metropolitan Manila","Misamis Occidental","Misamis Oriental","Mountain Province","Negros Occidental","Negros Oriental","North Cotabato","Northern Samar","Nueva Ecija","Nueva Vizcaya","Occidental Mindoro","Oriental Mindoro","Palawan","Pampanga","Pangasinan","Quezon","Quirino","Rizal","Romblon","Samar","Sarangani","Siquijor","Sorsogon","South Cotabato","Southern Leyte","Sultan Kudarat","Sulu","Surigao del Norte","Surigao del Sur","Tarlac","Tawi-Tawi","Zambales","Zamboanga del Norte","Zamboanga del Sur","Zamboanga Sibugay"], [0.0 for i in range(0,82)], {"Abra":"1","Agusan del Norte":"2","Agusan del Sur":"3","Aklan":"4","Albay":"5","Antique":"6","Apayao":"7","Aurora":"8","Basilan":"9","Bataan":"10","Batanes":"11","Batangas":"12","Benguet":"13","Biliran":"14","Bohol":"15","Bukidnon":"16","Bulacan":"17","Cagayan":"18","Camarines Norte":"19","Camarines Sur":"20","Camiguin":"21","Capiz":"22","Catanduanes":"23","Cavite":"24","Cebu":"25","Compostela Valley":"26","Davao del Norte":"27","Davao del Sur":"28","Davao Occidental":"29","Davao Oriental":"30","Dinagat Islands":"31","Eastern Samar":"32","Guimaras":"33","Ifugao":"34","Ilocos Norte":"35","Ilocos Sur":"36","Iloilo":"37","Isabela":"38","Kalinga":"39","La Union":"40","Laguna":"41","Lanao del Norte":"42","Lanao del Sur":"43","Leyte":"44","Maguindanao":"45","Marinduque":"46","Masbate":"47","Metropolitan Manila":"48","Misamis Occidental":"49","Misamis Oriental":"50","Mountain Province":"51","Negros Occidental":"52","Negros Oriental":"53","North Cotabato":"54","Northern Samar":"55","Nueva Ecija":"56","Nueva Vizcaya":"57","Occidental Mindoro":"58","Oriental Mindoro":"59","Palawan":"60","Pampanga":"61","Pangasinan":"62","Quezon":"63","Quirino":"64","Rizal":"65","Romblon":"66","Samar":"67","Sarangani":"68","Siquijor":"69","Sorsogon":"70","South Cotabato":"71","Southern Leyte":"72","Sultan Kudarat":"73","Sulu":"74","Surigao del Norte":"75","Surigao del Sur":"76","Tarlac":"77","Tawi-Tawi":"78","Zambales":"79","Zamboanga del Norte":"80","Zamboanga del Sur":"81","Zamboanga Sibugay":"82"})
