import settings
import handlers.base_handler
import csv

class CartogramHandler(handlers.base_handler.BaseCartogramHandler):

    def get_name(self):
        return "Indonesia"

    def get_gen_file(self):
        return "{}/idn_processedmap.json".format(settings.CARTOGRAM_DATA_DIR)
    
    def validate_values(self, values):

        if len(values) != 33:
            return False
        
        for v in values:
            if type(v) != float:
                return False

        return True
    
    def gen_area_data(self, values):
        return """cartogram_id,Region Data,Region Name,Inset
1,{},Aceh,L
2,{},Bali,L
3,{},Bangka Belitung,L
4,{},Banten,L
5,{},Bengkulu,L
6,{},Gorontalo,L
7,{},Jakarta Raya,L
8,{},Jambi,L
9,{},Jawa Barat,L
10,{},Jawa Tengah,L
11,{},Jawa Timur,L
12,{},Kalimantan Barat,L
13,{},Kalimantan Selatan,L
14,{},Kalimantan Tengah,L
15,{},Kalimantan Timur,L
16,{},Kepulauan Riau,L
17,{},Lampung,R
18,{},Maluku,R
19,{},Maluku Utara,R
20,{},Nusa Tenggara Barat,R
21,{},Nusa Tenggara Timur,R
22,{},Papua,R
23,{},Papua Barat,R
24,{},Riau,R
25,{},Sulawesi Barat,R
26,{},Sulawesi Selatan,R
27,{},Sulawesi Tengah,R
28,{},Sulawesi Tenggara,R
29,{},Sulawesi Utara,R
30,{},Sumatera Barat,R
31,{},Sumatera Selatan,R
32,{},Sumatera Utara,R
33,{},Yogyakarta,R""".format(*values)
    
    def expect_geojson_output(self):
        return True

    def csv_to_area_string_and_colors(self, csvfile):
        return self.order_by_example(csv.reader(csvfile), "Province", 0, 1, 2, 3, ["Aceh","Bali","Bangka Belitung","Banten","Bengkulu","Gorontalo","Jakarta Raya","Jambi","Jawa Barat","Jawa Tengah","Jawa Timur","Kalimantan Barat","Kalimantan Selatan","Kalimantan Tengah","Kalimantan Timur","Kepulauan Riau","Lampung","Maluku","Maluku Utara","Nusa Tenggara Barat","Nusa Tenggara Timur","Papua","Papua Barat","Riau","Sulawesi Barat","Sulawesi Selatan","Sulawesi Tengah","Sulawesi Tenggara","Sulawesi Utara","Sumatera Barat","Sumatera Selatan","Sumatera Utara","Yogyakarta"], [0.0 for i in range(0,33)], {"Aceh":"1","Bali":"2","Bangka Belitung":"3","Banten":"4","Bengkulu":"5","Gorontalo":"6","Jakarta Raya":"7","Jambi":"8","Jawa Barat":"9","Jawa Tengah":"10","Jawa Timur":"11","Kalimantan Barat":"12","Kalimantan Selatan":"13","Kalimantan Tengah":"14","Kalimantan Timur":"15","Kepulauan Riau":"16","Lampung":"17","Maluku":"18","Maluku Utara":"19","Nusa Tenggara Barat":"20","Nusa Tenggara Timur":"21","Papua":"22","Papua Barat":"23","Riau":"24","Sulawesi Barat":"25","Sulawesi Selatan":"26","Sulawesi Tengah":"27","Sulawesi Tenggara":"28","Sulawesi Utara":"29","Sumatera Barat":"30","Sumatera Selatan":"31","Sumatera Utara":"32","Yogyakarta":"33"})

