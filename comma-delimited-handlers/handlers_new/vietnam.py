import settings
import handlers.base_handler
import csv

class CartogramHandler(handlers.base_handler.BaseCartogramHandler):

    def get_name(self):
        return "Vietnam"

    def get_gen_file(self):
        return "{}/vietnam_processedmap.json".format(settings.CARTOGRAM_DATA_DIR)
    
    def validate_values(self, values):

        if len(values) != 63:
            return False
        
        for v in values:
            if type(v) != float:
                return False

        return True
    
    def gen_area_data(self, values):
        return """cartogram_id,Region Data,Region Name,Inset
1,{},An Giang,L
2,{},Ba Ria - Vung Tau,L
3,{},Bac Giang,L
4,{},Bac Kan,L
5,{},Bac Lieu,L
6,{},Bac Ninh,L
7,{},Ben Tre,L
8,{},Binh Dinh,L
9,{},Binh Duong,L
10,{},Binh Phuoc,L
11,{},Binh Thuan,L
12,{},Ca Mau,L
13,{},Can Tho,L
14,{},Cao Bang,L
15,{},Da Nang,L
16,{},Dak Lak,L
17,{},Dak Nong,L
18,{},Dien Bien,L
19,{},Dong Nai,L
20,{},Dong Thap,L
21,{},Gia Lai,L
22,{},Ha Giang,L
23,{},Ha Nam,L
24,{},Ha Noi,L
25,{},Ha Tinh,L
26,{},Hai Duong,L
27,{},Hai Phong,L
28,{},Hau Giang,L
29,{},Ho Chi Minh,L
30,{},Hoa Binh,L
31,{},Hung Yen,L
32,{},Khanh Hoa,R
33,{},Kien Giang,R
34,{},Kon Tum,R
35,{},Lai Chau,R
36,{},Lam Dong,R
37,{},Lang Son,R
38,{},Lao Cai,R
39,{},Long An,R
40,{},Nam Dinh,R
41,{},Nghe An,R
42,{},Ninh Binh,R
43,{},Ninh Thuan,R
44,{},Phu Tho,R
45,{},Phu Yen,R
46,{},Quang Binh,R
47,{},Quang Nam,R
48,{},Quang Ngai,R
49,{},Quang Ninh,R
50,{},Quang Tri,R
51,{},Soc Trang,R
52,{},Son La,R
53,{},Tay Ninh,R
54,{},Thai Binh,R
55,{},Thai Nguyen,R
56,{},Thanh Hoa,R
57,{},Thua Thien Hue,R
58,{},Tien Giang,R
59,{},Tra Vinh,R
60,{},Tuyen Quang,R
61,{},Vinh Long,R
62,{},Vinh Phuc,R
63,{},Yen Bai,R""".format(*values)
    
    def expect_geojson_output(self):
        return True

    def csv_to_area_string_and_colors(self, csvfile):

        return self.order_by_example(csv.reader(csvfile), "Province/Municipality", 0, 1, 2, 3, ["An Giang","Ba Ria - Vung Tau","Bac Giang","Bac Kan","Bac Lieu","Bac Ninh","Ben Tre","Binh Dinh","Binh Duong","Binh Phuoc","Binh Thuan","Ca Mau","Can Tho","Cao Bang","Da Nang","Dak Lak","Dak Nong","Dien Bien","Dong Nai","Dong Thap","Gia Lai","Ha Giang","Ha Nam","Ha Noi","Ha Tinh","Hai Duong","Hai Phong","Hau Giang","Ho Chi Minh","Hoa Binh","Hung Yen","Khanh Hoa","Kien Giang","Kon Tum","Lai Chau","Lam Dong","Lang Son","Lao Cai","Long An","Nam Dinh","Nghe An","Ninh Binh","Ninh Thuan","Phu Tho","Phu Yen","Quang Binh","Quang Nam","Quang Ngai","Quang Ninh","Quang Tri","Soc Trang","Son La","Tay Ninh","Thai Binh","Thai Nguyen","Thanh Hoa","Thua Thien Hue","Tien Giang","Tra Vinh","Tuyen Quang","Vinh Long","Vinh Phuc","Yen Bai"], [0.0 for i in range(0,63)], {"An Giang":"1","Ba Ria - Vung Tau":"2","Bac Giang":"3","Bac Kan":"4","Bac Lieu":"5","Bac Ninh":"6","Ben Tre":"7","Binh Dinh":"8","Binh Duong":"9","Binh Phuoc":"10","Binh Thuan":"11","Ca Mau":"12","Can Tho":"13","Cao Bang":"14","Da Nang":"15","Dak Lak":"16","Dak Nong":"17","Dien Bien":"18","Dong Nai":"19","Dong Thap":"20","Gia Lai":"21","Ha Giang":"22","Ha Nam":"23","Ha Noi":"24","Ha Tinh":"25","Hai Duong":"26","Hai Phong":"27","Hau Giang":"28","Ho Chi Minh":"29","Hoa Binh":"30","Hung Yen":"31","Khanh Hoa":"32","Kien Giang":"33","Kon Tum":"34","Lai Chau":"35","Lam Dong":"36","Lang Son":"37","Lao Cai":"38","Long An":"39","Nam Dinh":"40","Nghe An":"41","Ninh Binh":"42","Ninh Thuan":"43","Phu Tho":"44","Phu Yen":"45","Quang Binh":"46","Quang Nam":"47","Quang Ngai":"48","Quang Ninh":"49","Quang Tri":"50","Soc Trang":"51","Son La":"52","Tay Ninh":"53","Thai Binh":"54","Thai Nguyen":"55","Thanh Hoa":"56","Thua Thien Hue":"57","Tien Giang":"58","Tra Vinh":"59","Tuyen Quang":"60","Vinh Long":"61","Vinh Phuc":"62","Yen Bai":"63"})
