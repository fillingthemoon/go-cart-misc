import settings
import handlers.base_handler
import csv

class CartogramHandler(handlers.base_handler.BaseCartogramHandler):

    def get_name(self):
        return "India"

    def get_gen_file(self):
        return "{}/india_noLD_conic.gen".format(settings.CARTOGRAM_DATA_DIR)
    
    def validate_values(self, values):

        if len(values) != 35:
            return False
        
        for v in values:
            if type(v) != float:
                return False

        return True
    
    def gen_area_data(self, values):
        return """cartogram_id,Region Data,Region Name,Inset
1,{},Andaman and Nicobar Islands AN,L
2,{},Andhra Pradesh AP,L
3,{},Arunachal Pradesh AR,L
4,{},Assam AS,L
5,{},Bihar BR,L
6,{},Chandigarh CH,L
7,{},Chhattisgarh CT,L
8,{},Dadra and Nagar Haveli DN,L
9,{},Daman and Diu DD,L
10,{},Delhi DL,L
11,{},Goa GA,L
12,{},Gujarat GJ,L
13,{},Haryana HR,L
14,{},Himachal Pradesh HP,L
15,{},Jammu and Kashmir JK,L
16,{},Jharkhand JH,L
17,{},Karnataka KA,L
18,{},Kerala KL,R
20,{},Madhya Pradesh MP,R
21,{},Maharashtra MH,R
22,{},Manipur MN,R
23,{},Meghalaya ML,R
24,{},Mizoram MZ,R
25,{},Nagaland NL,R
26,{},Odisha OD,R
27,{},Puducherry PY,R
28,{},Punjab PB,R
29,{},Rajasthan RJ,R
30,{},Sikkim SK,R
31,{},Tamil Nadu TN,R
32,{},Telangana TG,R
33,{},Tripura TR,R
34,{},Uttar Pradesh UP,R
35,{},Uttarakhand UK,R
36,{},West Bengal WB,R""".format(*values)

    def csv_to_area_string_and_colors(self, csvfile):

        return self.order_by_example(csv.reader(csvfile), "State", 0, 1, 2, 3, ['Andaman and Nicobar Islands','Andhra Pradesh','Arunachal Pradesh','Assam','Bihar','Chandigarh','Chhattisgarh','Dadra and Nagar Haveli','Daman and Diu','Delhi','Goa','Gujarat','Haryana','Himachal Pradesh','Jammu and Kashmir','Jharkhand','Karnataka','Kerala','Madhya Pradesh','Maharashtra','Manipur','Meghalaya','Mizoram','Nagaland','Odisha','Puducherry','Punjab','Rajasthan','Sikkim','Tamil Nadu','Telangana','Tripura','Uttar Pradesh','Uttarakhand','West Bengal'], [0.0 for i in range(0,35)], {'Andaman and Nicobar Islands':'1','Andhra Pradesh':'2','Arunachal Pradesh':'3','Assam':'4','Bihar':'5','Chandigarh':'6','Chhattisgarh':'7','Dadra and Nagar Haveli':'8','Daman and Diu':'9','Delhi':'10','Goa':'11','Gujarat':'12','Haryana':'13','Himachal Pradesh':'14','Jammu and Kashmir':'15','Jharkhand':'16','Karnataka':'17','Kerala':'18','Madhya Pradesh':'20','Maharashtra':'21','Manipur':'22','Meghalaya':'23','Mizoram':'24','Nagaland':'25','Odisha':'26','Puducherry':'27','Punjab':'28','Rajasthan':'29','Sikkim':'30','Tamil Nadu':'31','Telangana':'32','Tripura':'33','Uttar Pradesh':'34','Uttarakhand':'35','West Bengal':'36'})

