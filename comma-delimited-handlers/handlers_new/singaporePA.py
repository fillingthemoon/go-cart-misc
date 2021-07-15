import settings
import handlers.base_handler
import csv

class CartogramHandler(handlers.base_handler.BaseCartogramHandler):

    def get_name(self):
        return "Singapore (by Planning Area)"

    def get_gen_file(self):
        return "{}/singaporePA_processedmap.json".format(settings.CARTOGRAM_DATA_DIR)
    
    def validate_values(self, values):

        if len(values) != 55:
            return False
        
        for v in values:
            if type(v) != float:
                return False

        return True
    
    def gen_area_data(self, values):
        return """cartogram_id,Region Data,Region Name,Inset\n
1,{},Ang Mo Kio,L\n
2,{},Bedok,L\n
3,{},Bishan,L\n
4,{},Boon Lay,L\n
5,{},Bukit Batok,L\n
6,{},Bukit Merah,L\n
7,{},Bukit Panjang,L\n
8,{},Bukit Timah,L\n
9,{},Central Water Catchment,L\n
10,{},Changi,L\n
11,{},Changi Bay,L\n
12,{},Choa Chu Kang,L\n
13,{},Clementi,L\n
14,{},Downtown Core,L\n
15,{},Geylang,L\n
16,{},Hougang,L\n
17,{},Jurong East,L\n
18,{},Jurong West,L\n
19,{},Kallang,L\n
20,{},Lim Chu Kang,L\n
21,{},Mandai,L\n
22,{},Marina East,L\n
23,{},Marina South,L\n
24,{},Marine Parade,L\n
25,{},Museum,L\n
26,{},Newton,L\n
27,{},North-eastern Islands,L\n
28,{},Novena,R\n
29,{},Orchard,R\n
30,{},Outram,R\n
31,{},Pasir Ris,R\n
32,{},Paya Lebar,R\n
33,{},Pioneer,R\n
34,{},Punggol,R\n
35,{},Queenstown,R\n
36,{},River Valley,R\n
37,{},Rochor,R\n
38,{},Seletar,R\n
39,{},Sembawang,R\n
40,{},Sengkang,R\n
41,{},Serangoon,R\n
42,{},Simpang,R\n
43,{},Singapore River,R\n
44,{},Southern Islands,R\n
45,{},Straits View,R\n
46,{},Sungei Kadut,R\n
47,{},Tampines,R\n
48,{},Tanglin,R\n
49,{},Tengah,R\n
50,{},Toa Payoh,R\n
51,{},Tuas,R\n
52,{},Western Islands,R\n
53,{},Western Water Catchment,R\n
54,{},Woodlands,R\n
55,{},Yishun,R\n""".format(*values)
    
    def expect_geojson_output(self):
        return True

    def csv_to_area_string_and_colors(self, csvfile):

        return self.order_by_example(csv.reader(csvfile), "Planning Area", 0, 1, 2, 3, ["Ang Mo Kio","Bedok","Bishan","Boon Lay","Bukit Batok","Bukit Merah","Bukit Panjang","Bukit Timah","Central Water Catchment","Changi","Changi Bay","Choa Chu Kang","Clementi","Downtown Core","Geylang","Hougang","Jurong East","Jurong West","Kallang","Lim Chu Kang","Mandai","Marina East","Marina South","Marine Parade","Museum","Newton","North-eastern Islands","Novena","Orchard","Outram","Pasir Ris","Paya Lebar","Pioneer","Punggol","Queenstown","River Valley","Rochor","Seletar","Sembawang","Sengkang","Serangoon","Simpang","Singapore River","Southern Islands","Straits View","Sungei Kadut","Tampines","Tanglin","Tengah","Toa Payoh","Tuas","Western Islands","Western Water Catchment","Woodlands","Yishun"], [0.0 for i in range(0,55)], {"Ang Mo Kio":"1","Bedok":"2","Bishan":"3","Boon Lay":"4","Bukit Batok":"5","Bukit Merah":"6","Bukit Panjang":"7","Bukit Timah":"8","Central Water Catchment":"9","Changi":"10","Changi Bay":"11","Choa Chu Kang":"12","Clementi":"13","Downtown Core":"14","Geylang":"15","Hougang":"16","Jurong East":"17","Jurong West":"18","Kallang":"19","Lim Chu Kang":"20","Mandai":"21","Marina East":"22","Marina South":"23","Marine Parade":"24","Museum":"25","Newton":"26","North-eastern Islands":"27","Novena":"28","Orchard":"29","Outram":"30","Pasir Ris":"31","Paya Lebar":"32","Pioneer":"33","Punggol":"34","Queenstown":"35","River Valley":"36","Rochor":"37","Seletar":"38","Sembawang":"39","Sengkang":"40","Serangoon":"41","Simpang":"42","Singapore River":"43","Southern Islands":"44","Straits View":"45","Sungei Kadut":"46","Tampines":"47","Tanglin":"48","Tengah":"49","Toa Payoh":"50","Tuas":"51","Western Islands":"52","Western Water Catchment":"53","Woodlands":"54","Yishun":"55"})
