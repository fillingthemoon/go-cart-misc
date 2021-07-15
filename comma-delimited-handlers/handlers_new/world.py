import settings
import handlers.base_handler
import csv

class CartogramHandler(handlers.base_handler.BaseCartogramHandler):

    def get_name(self):
        return "World"

    def get_gen_file(self):
        return "{}/world_enlarged.json".format(settings.CARTOGRAM_DATA_DIR)
    
    def validate_values(self, values):

        if len(values) != 242:
            return False
        
        for v in values:
            if type(v) != float:
                return False

        return True
    
    def gen_area_data(self, values):
        return """cartogram_id,Region Data,Region Name,Inset\n
1,{},Afghanistan,L\n
2,{},Aland,L\n
3,{},Albania,L\n
4,{},Algeria,L\n
5,{},American Samoa,L\n
6,{},Andorra,L\n
7,{},Angola,L\n
8,{},Anguilla,L\n
9,{},Antarctica,L\n
10,{},Antigua and Barb.,L\n
11,{},Argentina,L\n
12,{},Armenia,L\n
13,{},Aruba,L\n
14,{},Australia,L\n
15,{},Austria,L\n
16,{},Azerbaijan,L\n
17,{},Bahamas,L\n
18,{},Bahrain,L\n
19,{},Bangladesh,L\n
20,{},Barbados,L\n
21,{},Belarus,L\n
22,{},Belgium,L\n
23,{},Belize,L\n
24,{},Benin,L\n
25,{},Bermuda,L\n
26,{},Bhutan,L\n
27,{},Bolivia,L\n
28,{},Bosnia and Herz.,L\n
29,{},Botswana,L\n
30,{},Br. Indian Ocean Ter.,L\n
31,{},Brazil,L\n
32,{},British Virgin Is.,L\n
33,{},Brunei,L\n
34,{},Bulgaria,L\n
35,{},Burkina Faso,L\n
36,{},Burundi,L\n
37,{},Cabo Verde,L\n
38,{},Cambodia,L\n
39,{},Cameroon,L\n
40,{},Canada,L\n
41,{},Cayman Is.,L\n
42,{},Central African Rep.,L\n
43,{},Chad,L\n
44,{},Chile,L\n
45,{},China,L\n
46,{},Colombia,L\n
47,{},Comoros,L\n
48,{},Congo,L\n
49,{},Cook Is.,L\n
50,{},Costa Rica,L\n
51,{},Cote d'Ivoire,L\n
52,{},Croatia,L\n
53,{},Cuba,L\n
54,{},Curacao,L\n
55,{},Cyprus,L\n
56,{},Czechia,L\n
57,{},Dem. Rep. Congo,L\n
58,{},Denmark,L\n
59,{},Djibouti,L\n
60,{},Dominica,L\n
61,{},Dominican Rep.,L\n
62,{},Ecuador,L\n
63,{},Egypt,L\n
64,{},El Salvador,L\n
65,{},Eq. Guinea,L\n
66,{},Eritrea,L\n
67,{},Estonia,L\n
68,{},eSwatini,L\n
69,{},Ethiopia,L\n
70,{},Faeroe Is.,L\n
71,{},Falkland Is.,L\n
72,{},Fiji,L\n
73,{},Finland,L\n
74,{},Fr. Polynesia,L\n
75,{},Fr. S. Antarctic Lands,L\n
76,{},France,L\n
77,{},Gabon,L\n
78,{},Gambia,L\n
79,{},Georgia,L\n
80,{},Germany,L\n
81,{},Ghana,L\n
82,{},Gibraltar,L\n
83,{},Greece,L\n
84,{},Greenland,L\n
85,{},Grenada,L\n
86,{},Guam,L\n
87,{},Guatemala,L\n
88,{},Guernsey,L\n
89,{},Guinea,L\n
90,{},Guinea-Bissau,L\n
91,{},Guyana,L\n
92,{},Haiti,L\n
93,{},Heard I. and McDonald Is.,L\n
94,{},Honduras,L\n
95,{},Hong Kong,L\n
96,{},Hungary,L\n
97,{},Iceland,L\n
98,{},India,L\n
99,{},Indonesia,L\n
100,{},Iran,L\n
101,{},Iraq,L\n
102,{},Ireland,L\n
103,{},Isle of Man,L\n
104,{},Israel,L\n
105,{},Italy,L\n
106,{},Jamaica,L\n
107,{},Japan,L\n
108,{},Jersey,L\n
109,{},Jordan,L\n
110,{},Kazakhstan,L\n
111,{},Kenya,L\n
112,{},Kiribati,L\n
113,{},Kosovo,L\n
114,{},Kuwait,L\n
115,{},Kyrgyzstan,L\n
116,{},Laos,L\n
117,{},Latvia,L\n
118,{},Lebanon,L\n
119,{},Lesotho,L\n
120,{},Liberia,L\n
121,{},Libya,R\n
122,{},Liechtenstein,R\n
123,{},Lithuania,R\n
124,{},Luxembourg,R\n
125,{},Macao,R\n
126,{},Macedonia,R\n
127,{},Madagascar,R\n
128,{},Malawi,R\n
129,{},Malaysia,R\n
130,{},Maldives,R\n
131,{},Mali,R\n
132,{},Malta,R\n
133,{},Marshall Is.,R\n
134,{},Mauritania,R\n
135,{},Mauritius,R\n
136,{},Mexico,R\n
137,{},Micronesia,R\n
138,{},Moldova,R\n
139,{},Monaco,R\n
140,{},Mongolia,R\n
141,{},Montenegro,R\n
142,{},Montserrat,R\n
143,{},Morocco,R\n
144,{},Mozambique,R\n
145,{},Myanmar,R\n
146,{},N. Cyprus,R\n
147,{},N. Mariana Is.,R\n
148,{},Namibia,R\n
149,{},Nauru,R\n
150,{},Nepal,R\n
151,{},Netherlands,R\n
152,{},New Caledonia,R\n
153,{},New Zealand,R\n
154,{},Nicaragua,R\n
155,{},Niger,R\n
156,{},Nigeria,R\n
157,{},Niue,R\n
158,{},Norfolk Island,R\n
159,{},North Korea,R\n
160,{},Norway,R\n
161,{},Oman,R\n
162,{},Pakistan,R\n
163,{},Palau,R\n
164,{},Palestine,R\n
165,{},Panama,R\n
166,{},Papua New Guinea,R\n
167,{},Paraguay,R\n
168,{},Peru,R\n
169,{},Philippines,R\n
170,{},Pitcairn Is.,R\n
171,{},Poland,R\n
172,{},Portugal,R\n
173,{},Puerto Rico,R\n
174,{},Qatar,R\n
175,{},Romania,R\n
176,{},Russia,R\n
177,{},Rwanda,R\n
178,{},S. Geo. and the Is.,R\n
179,{},S. Sudan,R\n
180,{},Saint Helena,R\n
181,{},Saint Lucia,R\n
182,{},Samoa,R\n
183,{},San Marino,R\n
184,{},Sao Tome and Principe,R\n
185,{},Saudi Arabia,R\n
186,{},Senegal,R\n
187,{},Serbia,R\n
188,{},Seychelles,R\n
189,{},Siachen Glacier,R\n
190,{},Sierra Leone,R\n
191,{},Singapore,R\n
192,{},Sint Maarten,R\n
193,{},Slovakia,R\n
194,{},Slovenia,R\n
195,{},Solomon Is.,R\n
196,{},Somalia,R\n
197,{},Somaliland,R\n
198,{},South Africa,R\n
199,{},South Korea,R\n
200,{},Spain,R\n
201,{},Sri Lanka,R\n
202,{},St-Barthelemy,R\n
203,{},St-Martin,R\n
204,{},St. Kitts and Nevis,R\n
205,{},St. Pierre and Miquelon,R\n
206,{},St. Vin. and Gren.,R\n
207,{},Sudan,R\n
208,{},Suriname,R\n
209,{},Sweden,R\n
210,{},Switzerland,R\n
211,{},Syria,R\n
212,{},Taiwan,R\n
213,{},Tajikistan,R\n
214,{},Tanzania,R\n
215,{},Thailand,R\n
216,{},Timor-Leste,R\n
217,{},Togo,R\n
218,{},Tonga,R\n
219,{},Trinidad and Tobago,R\n
220,{},Tunisia,R\n
221,{},Turkey,R\n
222,{},Turkmenistan,R\n
223,{},Turks and Caicos Is.,R\n
224,{},Tuvalu,R\n
225,{},U.S. Minor Outlying Is.,R\n
226,{},U.S. Virgin Is.,R\n
227,{},Uganda,R\n
228,{},Ukraine,R\n
229,{},United Arab Emirates,R\n
230,{},United Kingdom,R\n
231,{},United States of America,R\n
232,{},Uruguay,R\n
233,{},Uzbekistan,R\n
234,{},Vanuatu,R\n
235,{},Vatican,R\n
236,{},Venezuela,R\n
237,{},Vietnam,R\n
238,{},W. Sahara,R\n
239,{},Wallis and Futuna Is.,R\n
240,{},Yemen,R\n
241,{},Zambia,R\n
242,{},Zimbabwe,R\n""".format(*values)
    
    def expect_geojson_output(self):
        return True

    def csv_to_area_string_and_colors(self, csvfile):

        return self.order_by_example(csv.reader(csvfile), "Country", 0, 1, 2, 3, ["Afghanistan","Aland","Albania","Algeria","American Samoa","Andorra","Angola","Anguilla","Antarctica","Antigua and Barb.","Argentina","Armenia","Aruba","Australia","Austria","Azerbaijan","Bahamas","Bahrain","Bangladesh","Barbados","Belarus","Belgium","Belize","Benin","Bermuda","Bhutan","Bolivia","Bosnia and Herz.","Botswana","Br. Indian Ocean Ter.","Brazil","British Virgin Is.","Brunei","Bulgaria","Burkina Faso","Burundi","Cabo Verde","Cambodia","Cameroon","Canada","Cayman Is.","Central African Rep.","Chad","Chile","China","Colombia","Comoros","Congo","Cook Is.","Costa Rica","Cote d'Ivoire","Croatia","Cuba","Curacao","Cyprus","Czechia","Dem. Rep. Congo","Denmark","Djibouti","Dominica","Dominican Rep.","Ecuador","Egypt","El Salvador","Eq. Guinea","Eritrea","Estonia","eSwatini","Ethiopia","Faeroe Is.","Falkland Is.","Fiji","Finland","Fr. Polynesia","Fr. S. Antarctic Lands","France","Gabon","Gambia","Georgia","Germany","Ghana","Gibraltar","Greece","Greenland","Grenada","Guam","Guatemala","Guernsey","Guinea","Guinea-Bissau","Guyana","Haiti","Heard I. and McDonald Is.","Honduras","Hong Kong","Hungary","Iceland","India","Indonesia","Iran","Iraq","Ireland","Isle of Man","Israel","Italy","Jamaica","Japan","Jersey","Jordan","Kazakhstan","Kenya","Kiribati","Kosovo","Kuwait","Kyrgyzstan","Laos","Latvia","Lebanon","Lesotho","Liberia","Libya","Liechtenstein","Lithuania","Luxembourg","Macao","Macedonia","Madagascar","Malawi","Malaysia","Maldives","Mali","Malta","Marshall Is.","Mauritania","Mauritius","Mexico","Micronesia","Moldova","Monaco","Mongolia","Montenegro","Montserrat","Morocco","Mozambique","Myanmar","N. Cyprus","N. Mariana Is.","Namibia","Nauru","Nepal","Netherlands","New Caledonia","New Zealand","Nicaragua","Niger","Nigeria","Niue","Norfolk Island","North Korea","Norway","Oman","Pakistan","Palau","Palestine","Panama","Papua New Guinea","Paraguay","Peru","Philippines","Pitcairn Is.","Poland","Portugal","Puerto Rico","Qatar","Romania","Russia","Rwanda","S. Geo. and the Is.","S. Sudan","Saint Helena","Saint Lucia","Samoa","San Marino","Sao Tome and Principe","Saudi Arabia","Senegal","Serbia","Seychelles","Siachen Glacier","Sierra Leone","Singapore","Sint Maarten","Slovakia","Slovenia","Solomon Is.","Somalia","Somaliland","South Africa","South Korea","Spain","Sri Lanka","St-Barthelemy","St-Martin","St. Kitts and Nevis","St. Pierre and Miquelon","St. Vin. and Gren.","Sudan","Suriname","Sweden","Switzerland","Syria","Taiwan","Tajikistan","Tanzania","Thailand","Timor-Leste","Togo","Tonga","Trinidad and Tobago","Tunisia","Turkey","Turkmenistan","Turks and Caicos Is.","Tuvalu","U.S. Minor Outlying Is.","U.S. Virgin Is.","Uganda","Ukraine","United Arab Emirates","United Kingdom","United States of America","Uruguay","Uzbekistan","Vanuatu","Vatican","Venezuela","Vietnam","W. Sahara","Wallis and Futuna Is.","Yemen","Zambia","Zimbabwe"], [0.0 for i in range(0,242)], {"Afghanistan":"1","Aland":"2","Albania":"3","Algeria":"4","American Samoa":"5","Andorra":"6","Angola":"7","Anguilla":"8","Antarctica":"9","Antigua and Barb.":"10","Argentina":"11","Armenia":"12","Aruba":"13","Australia":"14","Austria":"15","Azerbaijan":"16","Bahamas":"17","Bahrain":"18","Bangladesh":"19","Barbados":"20","Belarus":"21","Belgium":"22","Belize":"23","Benin":"24","Bermuda":"25","Bhutan":"26","Bolivia":"27","Bosnia and Herz.":"28","Botswana":"29","Br. Indian Ocean Ter.":"30","Brazil":"31","British Virgin Is.":"32","Brunei":"33","Bulgaria":"34","Burkina Faso":"35","Burundi":"36","Cabo Verde":"37","Cambodia":"38","Cameroon":"39","Canada":"40","Cayman Is.":"41","Central African Rep.":"42","Chad":"43","Chile":"44","China":"45","Colombia":"46","Comoros":"47","Congo":"48","Cook Is.":"49","Costa Rica":"50","Cote d'Ivoire":"51","Croatia":"52","Cuba":"53","Curacao":"54","Cyprus":"55","Czechia":"56","Dem. Rep. Congo":"57","Denmark":"58","Djibouti":"59","Dominica":"60","Dominican Rep.":"61","Ecuador":"62","Egypt":"63","El Salvador":"64","Eq. Guinea":"65","Eritrea":"66","Estonia":"67","eSwatini":"68","Ethiopia":"69","Faeroe Is.":"70","Falkland Is.":"71","Fiji":"72","Finland":"73","Fr. Polynesia":"74","Fr. S. Antarctic Lands":"75","France":"76","Gabon":"77","Gambia":"78","Georgia":"79","Germany":"80","Ghana":"81","Gibraltar":"82","Greece":"83","Greenland":"84","Grenada":"85","Guam":"86","Guatemala":"87","Guernsey":"88","Guinea":"89","Guinea-Bissau":"90","Guyana":"91","Haiti":"92","Heard I. and McDonald Is.":"93","Honduras":"94","Hong Kong":"95","Hungary":"96","Iceland":"97","India":"98","Indonesia":"99","Iran":"100","Iraq":"101","Ireland":"102","Isle of Man":"103","Israel":"104","Italy":"105","Jamaica":"106","Japan":"107","Jersey":"108","Jordan":"109","Kazakhstan":"110","Kenya":"111","Kiribati":"112","Kosovo":"113","Kuwait":"114","Kyrgyzstan":"115","Laos":"116","Latvia":"117","Lebanon":"118","Lesotho":"119","Liberia":"120","Libya":"121","Liechtenstein":"122","Lithuania":"123","Luxembourg":"124","Macao":"125","Macedonia":"126","Madagascar":"127","Malawi":"128","Malaysia":"129","Maldives":"130","Mali":"131","Malta":"132","Marshall Is.":"133","Mauritania":"134","Mauritius":"135","Mexico":"136","Micronesia":"137","Moldova":"138","Monaco":"139","Mongolia":"140","Montenegro":"141","Montserrat":"142","Morocco":"143","Mozambique":"144","Myanmar":"145","N. Cyprus":"146","N. Mariana Is.":"147","Namibia":"148","Nauru":"149","Nepal":"150","Netherlands":"151","New Caledonia":"152","New Zealand":"153","Nicaragua":"154","Niger":"155","Nigeria":"156","Niue":"157","Norfolk Island":"158","North Korea":"159","Norway":"160","Oman":"161","Pakistan":"162","Palau":"163","Palestine":"164","Panama":"165","Papua New Guinea":"166","Paraguay":"167","Peru":"168","Philippines":"169","Pitcairn Is.":"170","Poland":"171","Portugal":"172","Puerto Rico":"173","Qatar":"174","Romania":"175","Russia":"176","Rwanda":"177","S. Geo. and the Is.":"178","S. Sudan":"179","Saint Helena":"180","Saint Lucia":"181","Samoa":"182","San Marino":"183","Sao Tome and Principe":"184","Saudi Arabia":"185","Senegal":"186","Serbia":"187","Seychelles":"188","Siachen Glacier":"189","Sierra Leone":"190","Singapore":"191","Sint Maarten":"192","Slovakia":"193","Slovenia":"194","Solomon Is.":"195","Somalia":"196","Somaliland":"197","South Africa":"198","South Korea":"199","Spain":"200","Sri Lanka":"201","St-Barthelemy":"202","St-Martin":"203","St. Kitts and Nevis":"204","St. Pierre and Miquelon":"205","St. Vin. and Gren.":"206","Sudan":"207","Suriname":"208","Sweden":"209","Switzerland":"210","Syria":"211","Taiwan":"212","Tajikistan":"213","Tanzania":"214","Thailand":"215","Timor-Leste":"216","Togo":"217","Tonga":"218","Trinidad and Tobago":"219","Tunisia":"220","Turkey":"221","Turkmenistan":"222","Turks and Caicos Is.":"223","Tuvalu":"224","U.S. Minor Outlying Is.":"225","U.S. Virgin Is.":"226","Uganda":"227","Ukraine":"228","United Arab Emirates":"229","United Kingdom":"230","United States of America":"231","Uruguay":"232","Uzbekistan":"233","Vanuatu":"234","Vatican":"235","Venezuela":"236","Vietnam":"237","W. Sahara":"238","Wallis and Futuna Is.":"239","Yemen":"240","Zambia":"241","Zimbabwe":"242"})
