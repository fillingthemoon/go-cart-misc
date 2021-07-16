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
        return """cartogram_id,Region Data,Region Name,Inset
1,{},Abra,L
2,{},Agusan del Norte,L
3,{},Agusan del Sur,L
4,{},Aklan,L
5,{},Albay,L
6,{},Antique,L
7,{},Apayao,L
8,{},Aurora,L
9,{},Basilan,L
10,{},Bataan,L
11,{},Batanes,L
12,{},Batangas,L
13,{},Benguet,L
14,{},Biliran,L
15,{},Bohol,L
16,{},Bukidnon,L
17,{},Bulacan,L
18,{},Cagayan,L
19,{},Camarines Norte,L
20,{},Camarines Sur,L
21,{},Camiguin,L
22,{},Capiz,L
23,{},Catanduanes,L
24,{},Cavite,L
25,{},Cebu,L
26,{},Compostela Valley,L
27,{},Davao del Norte,L
28,{},Davao del Sur,L
29,{},Davao Occidental,L
30,{},Davao Oriental,L
31,{},Dinagat Islands,L
32,{},Eastern Samar,L
33,{},Guimaras,L
34,{},Ifugao,L
35,{},Ilocos Norte,L
36,{},Ilocos Sur,L
37,{},Iloilo,L
38,{},Isabela,L
39,{},Kalinga,L
40,{},La Union,L
41,{},Laguna,R
42,{},Lanao del Norte,R
43,{},Lanao del Sur,R
44,{},Leyte,R
45,{},Maguindanao,R
46,{},Marinduque,R
47,{},Masbate,R
48,{},Metropolitan Manila,R
49,{},Misamis Occidental,R
50,{},Misamis Oriental,R
51,{},Mountain Province,R
52,{},Negros Occidental,R
53,{},Negros Oriental,R
54,{},North Cotabato,R
55,{},Northern Samar,R
56,{},Nueva Ecija,R
57,{},Nueva Vizcaya,R
58,{},Occidental Mindoro,R
59,{},Oriental Mindoro,R
60,{},Palawan,R
61,{},Pampanga,R
62,{},Pangasinan,R
63,{},Quezon,R
64,{},Quirino,R
65,{},Rizal,R
66,{},Romblon,R
67,{},Samar,R
68,{},Sarangani,R
69,{},Siquijor,R
70,{},Sorsogon,R
71,{},South Cotabato,R
72,{},Southern Leyte,R
73,{},Sultan Kudarat,R
74,{},Sulu,R
75,{},Surigao del Norte,R
76,{},Surigao del Sur,R
77,{},Tarlac,R
78,{},Tawi-Tawi,R
79,{},Zambales,R
80,{},Zamboanga del Norte,R
81,{},Zamboanga del Sur,R
82,{},Zamboanga Sibugay,R""".format(*values)
    
    def expect_geojson_output(self):
        return True

    def csv_to_area_string_and_colors(self, csvfile):

        return self.order_by_example(csv.reader(csvfile), "Province/Region", 0, 1, 2, 3, ["Abra","Agusan del Norte","Agusan del Sur","Aklan","Albay","Antique","Apayao","Aurora","Basilan","Bataan","Batanes","Batangas","Benguet","Biliran","Bohol","Bukidnon","Bulacan","Cagayan","Camarines Norte","Camarines Sur","Camiguin","Capiz","Catanduanes","Cavite","Cebu","Compostela Valley","Davao del Norte","Davao del Sur","Davao Occidental","Davao Oriental","Dinagat Islands","Eastern Samar","Guimaras","Ifugao","Ilocos Norte","Ilocos Sur","Iloilo","Isabela","Kalinga","La Union","Laguna","Lanao del Norte","Lanao del Sur","Leyte","Maguindanao","Marinduque","Masbate","Metropolitan Manila","Misamis Occidental","Misamis Oriental","Mountain Province","Negros Occidental","Negros Oriental","North Cotabato","Northern Samar","Nueva Ecija","Nueva Vizcaya","Occidental Mindoro","Oriental Mindoro","Palawan","Pampanga","Pangasinan","Quezon","Quirino","Rizal","Romblon","Samar","Sarangani","Siquijor","Sorsogon","South Cotabato","Southern Leyte","Sultan Kudarat","Sulu","Surigao del Norte","Surigao del Sur","Tarlac","Tawi-Tawi","Zambales","Zamboanga del Norte","Zamboanga del Sur","Zamboanga Sibugay"], [0.0 for i in range(0,82)], {"Abra":"1","Agusan del Norte":"2","Agusan del Sur":"3","Aklan":"4","Albay":"5","Antique":"6","Apayao":"7","Aurora":"8","Basilan":"9","Bataan":"10","Batanes":"11","Batangas":"12","Benguet":"13","Biliran":"14","Bohol":"15","Bukidnon":"16","Bulacan":"17","Cagayan":"18","Camarines Norte":"19","Camarines Sur":"20","Camiguin":"21","Capiz":"22","Catanduanes":"23","Cavite":"24","Cebu":"25","Compostela Valley":"26","Davao del Norte":"27","Davao del Sur":"28","Davao Occidental":"29","Davao Oriental":"30","Dinagat Islands":"31","Eastern Samar":"32","Guimaras":"33","Ifugao":"34","Ilocos Norte":"35","Ilocos Sur":"36","Iloilo":"37","Isabela":"38","Kalinga":"39","La Union":"40","Laguna":"41","Lanao del Norte":"42","Lanao del Sur":"43","Leyte":"44","Maguindanao":"45","Marinduque":"46","Masbate":"47","Metropolitan Manila":"48","Misamis Occidental":"49","Misamis Oriental":"50","Mountain Province":"51","Negros Occidental":"52","Negros Oriental":"53","North Cotabato":"54","Northern Samar":"55","Nueva Ecija":"56","Nueva Vizcaya":"57","Occidental Mindoro":"58","Oriental Mindoro":"59","Palawan":"60","Pampanga":"61","Pangasinan":"62","Quezon":"63","Quirino":"64","Rizal":"65","Romblon":"66","Samar":"67","Sarangani":"68","Siquijor":"69","Sorsogon":"70","South Cotabato":"71","Southern Leyte":"72","Sultan Kudarat":"73","Sulu":"74","Surigao del Norte":"75","Surigao del Sur":"76","Tarlac":"77","Tawi-Tawi":"78","Zambales":"79","Zamboanga del Norte":"80","Zamboanga del Sur":"81","Zamboanga Sibugay":"82"})
