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
        return """cartogram_id,Region Data,Region Name,Inset
1,{},Afghanistan,L
2,{},Aland,L
3,{},Albania,L
4,{},Algeria,L
5,{},American Samoa,L
6,{},Andorra,L
7,{},Angola,L
8,{},Anguilla,L
9,{},Antarctica,L
10,{},Antigua and Barb.,L
11,{},Argentina,L
12,{},Armenia,L
13,{},Aruba,L
14,{},Australia,L
15,{},Austria,L
16,{},Azerbaijan,L
17,{},Bahamas,L
18,{},Bahrain,L
19,{},Bangladesh,L
20,{},Barbados,L
21,{},Belarus,L
22,{},Belgium,L
23,{},Belize,L
24,{},Benin,L
25,{},Bermuda,L
26,{},Bhutan,L
27,{},Bolivia,L
28,{},Bosnia and Herz.,L
29,{},Botswana,L
30,{},Br. Indian Ocean Ter.,L
31,{},Brazil,L
32,{},British Virgin Is.,L
33,{},Brunei,L
34,{},Bulgaria,L
35,{},Burkina Faso,L
36,{},Burundi,L
37,{},Cabo Verde,L
38,{},Cambodia,L
39,{},Cameroon,L
40,{},Canada,L
41,{},Cayman Is.,L
42,{},Central African Rep.,L
43,{},Chad,L
44,{},Chile,L
45,{},China,L
46,{},Colombia,L
47,{},Comoros,L
48,{},Congo,L
49,{},Cook Is.,L
50,{},Costa Rica,L
51,{},Cote d'Ivoire,L
52,{},Croatia,L
53,{},Cuba,L
54,{},Curacao,L
55,{},Cyprus,L
56,{},Czechia,L
57,{},Dem. Rep. Congo,L
58,{},Denmark,L
59,{},Djibouti,L
60,{},Dominica,L
61,{},Dominican Rep.,L
62,{},Ecuador,L
63,{},Egypt,L
64,{},El Salvador,L
65,{},Eq. Guinea,L
66,{},Eritrea,L
67,{},Estonia,L
68,{},eSwatini,L
69,{},Ethiopia,L
70,{},Faeroe Is.,L
71,{},Falkland Is.,L
72,{},Fiji,L
73,{},Finland,L
74,{},Fr. Polynesia,L
75,{},Fr. S. Antarctic Lands,L
76,{},France,L
77,{},Gabon,L
78,{},Gambia,L
79,{},Georgia,L
80,{},Germany,L
81,{},Ghana,L
82,{},Gibraltar,L
83,{},Greece,L
84,{},Greenland,L
85,{},Grenada,L
86,{},Guam,L
87,{},Guatemala,L
88,{},Guernsey,L
89,{},Guinea,L
90,{},Guinea-Bissau,L
91,{},Guyana,L
92,{},Haiti,L
93,{},Heard I. and McDonald Is.,L
94,{},Honduras,L
95,{},Hong Kong,L
96,{},Hungary,L
97,{},Iceland,L
98,{},India,L
99,{},Indonesia,L
100,{},Iran,L
101,{},Iraq,L
102,{},Ireland,L
103,{},Isle of Man,L
104,{},Israel,L
105,{},Italy,L
106,{},Jamaica,L
107,{},Japan,L
108,{},Jersey,L
109,{},Jordan,L
110,{},Kazakhstan,L
111,{},Kenya,L
112,{},Kiribati,L
113,{},Kosovo,L
114,{},Kuwait,L
115,{},Kyrgyzstan,L
116,{},Laos,L
117,{},Latvia,L
118,{},Lebanon,L
119,{},Lesotho,L
120,{},Liberia,L
121,{},Libya,R
122,{},Liechtenstein,R
123,{},Lithuania,R
124,{},Luxembourg,R
125,{},Macao,R
126,{},Macedonia,R
127,{},Madagascar,R
128,{},Malawi,R
129,{},Malaysia,R
130,{},Maldives,R
131,{},Mali,R
132,{},Malta,R
133,{},Marshall Is.,R
134,{},Mauritania,R
135,{},Mauritius,R
136,{},Mexico,R
137,{},Micronesia,R
138,{},Moldova,R
139,{},Monaco,R
140,{},Mongolia,R
141,{},Montenegro,R
142,{},Montserrat,R
143,{},Morocco,R
144,{},Mozambique,R
145,{},Myanmar,R
146,{},N. Cyprus,R
147,{},N. Mariana Is.,R
148,{},Namibia,R
149,{},Nauru,R
150,{},Nepal,R
151,{},Netherlands,R
152,{},New Caledonia,R
153,{},New Zealand,R
154,{},Nicaragua,R
155,{},Niger,R
156,{},Nigeria,R
157,{},Niue,R
158,{},Norfolk Island,R
159,{},North Korea,R
160,{},Norway,R
161,{},Oman,R
162,{},Pakistan,R
163,{},Palau,R
164,{},Palestine,R
165,{},Panama,R
166,{},Papua New Guinea,R
167,{},Paraguay,R
168,{},Peru,R
169,{},Philippines,R
170,{},Pitcairn Is.,R
171,{},Poland,R
172,{},Portugal,R
173,{},Puerto Rico,R
174,{},Qatar,R
175,{},Romania,R
176,{},Russia,R
177,{},Rwanda,R
178,{},S. Geo. and the Is.,R
179,{},S. Sudan,R
180,{},Saint Helena,R
181,{},Saint Lucia,R
182,{},Samoa,R
183,{},San Marino,R
184,{},Sao Tome and Principe,R
185,{},Saudi Arabia,R
186,{},Senegal,R
187,{},Serbia,R
188,{},Seychelles,R
189,{},Siachen Glacier,R
190,{},Sierra Leone,R
191,{},Singapore,R
192,{},Sint Maarten,R
193,{},Slovakia,R
194,{},Slovenia,R
195,{},Solomon Is.,R
196,{},Somalia,R
197,{},Somaliland,R
198,{},South Africa,R
199,{},South Korea,R
200,{},Spain,R
201,{},Sri Lanka,R
202,{},St-Barthelemy,R
203,{},St-Martin,R
204,{},St. Kitts and Nevis,R
205,{},St. Pierre and Miquelon,R
206,{},St. Vin. and Gren.,R
207,{},Sudan,R
208,{},Suriname,R
209,{},Sweden,R
210,{},Switzerland,R
211,{},Syria,R
212,{},Taiwan,R
213,{},Tajikistan,R
214,{},Tanzania,R
215,{},Thailand,R
216,{},Timor-Leste,R
217,{},Togo,R
218,{},Tonga,R
219,{},Trinidad and Tobago,R
220,{},Tunisia,R
221,{},Turkey,R
222,{},Turkmenistan,R
223,{},Turks and Caicos Is.,R
224,{},Tuvalu,R
225,{},U.S. Minor Outlying Is.,R
226,{},U.S. Virgin Is.,R
227,{},Uganda,R
228,{},Ukraine,R
229,{},United Arab Emirates,R
230,{},United Kingdom,R
231,{},United States of America,R
232,{},Uruguay,R
233,{},Uzbekistan,R
234,{},Vanuatu,R
235,{},Vatican,R
236,{},Venezuela,R
237,{},Vietnam,R
238,{},W. Sahara,R
239,{},Wallis and Futuna Is.,R
240,{},Yemen,R
241,{},Zambia,R
242,{},Zimbabwe,R""".format(*values)
    
    def expect_geojson_output(self):
        return True

    def csv_to_area_string_and_colors(self, csvfile):

        return self.order_by_example(csv.reader(csvfile), "Country", 0, 1, 2, 3, ["Afghanistan","Aland","Albania","Algeria","American Samoa","Andorra","Angola","Anguilla","Antarctica","Antigua and Barb.","Argentina","Armenia","Aruba","Australia","Austria","Azerbaijan","Bahamas","Bahrain","Bangladesh","Barbados","Belarus","Belgium","Belize","Benin","Bermuda","Bhutan","Bolivia","Bosnia and Herz.","Botswana","Br. Indian Ocean Ter.","Brazil","British Virgin Is.","Brunei","Bulgaria","Burkina Faso","Burundi","Cabo Verde","Cambodia","Cameroon","Canada","Cayman Is.","Central African Rep.","Chad","Chile","China","Colombia","Comoros","Congo","Cook Is.","Costa Rica","Cote d'Ivoire","Croatia","Cuba","Curacao","Cyprus","Czechia","Dem. Rep. Congo","Denmark","Djibouti","Dominica","Dominican Rep.","Ecuador","Egypt","El Salvador","Eq. Guinea","Eritrea","Estonia","eSwatini","Ethiopia","Faeroe Is.","Falkland Is.","Fiji","Finland","Fr. Polynesia","Fr. S. Antarctic Lands","France","Gabon","Gambia","Georgia","Germany","Ghana","Gibraltar","Greece","Greenland","Grenada","Guam","Guatemala","Guernsey","Guinea","Guinea-Bissau","Guyana","Haiti","Heard I. and McDonald Is.","Honduras","Hong Kong","Hungary","Iceland","India","Indonesia","Iran","Iraq","Ireland","Isle of Man","Israel","Italy","Jamaica","Japan","Jersey","Jordan","Kazakhstan","Kenya","Kiribati","Kosovo","Kuwait","Kyrgyzstan","Laos","Latvia","Lebanon","Lesotho","Liberia","Libya","Liechtenstein","Lithuania","Luxembourg","Macao","Macedonia","Madagascar","Malawi","Malaysia","Maldives","Mali","Malta","Marshall Is.","Mauritania","Mauritius","Mexico","Micronesia","Moldova","Monaco","Mongolia","Montenegro","Montserrat","Morocco","Mozambique","Myanmar","N. Cyprus","N. Mariana Is.","Namibia","Nauru","Nepal","Netherlands","New Caledonia","New Zealand","Nicaragua","Niger","Nigeria","Niue","Norfolk Island","North Korea","Norway","Oman","Pakistan","Palau","Palestine","Panama","Papua New Guinea","Paraguay","Peru","Philippines","Pitcairn Is.","Poland","Portugal","Puerto Rico","Qatar","Romania","Russia","Rwanda","S. Geo. and the Is.","S. Sudan","Saint Helena","Saint Lucia","Samoa","San Marino","Sao Tome and Principe","Saudi Arabia","Senegal","Serbia","Seychelles","Siachen Glacier","Sierra Leone","Singapore","Sint Maarten","Slovakia","Slovenia","Solomon Is.","Somalia","Somaliland","South Africa","South Korea","Spain","Sri Lanka","St-Barthelemy","St-Martin","St. Kitts and Nevis","St. Pierre and Miquelon","St. Vin. and Gren.","Sudan","Suriname","Sweden","Switzerland","Syria","Taiwan","Tajikistan","Tanzania","Thailand","Timor-Leste","Togo","Tonga","Trinidad and Tobago","Tunisia","Turkey","Turkmenistan","Turks and Caicos Is.","Tuvalu","U.S. Minor Outlying Is.","U.S. Virgin Is.","Uganda","Ukraine","United Arab Emirates","United Kingdom","United States of America","Uruguay","Uzbekistan","Vanuatu","Vatican","Venezuela","Vietnam","W. Sahara","Wallis and Futuna Is.","Yemen","Zambia","Zimbabwe"], [0.0 for i in range(0,242)], {"Afghanistan":"1","Aland":"2","Albania":"3","Algeria":"4","American Samoa":"5","Andorra":"6","Angola":"7","Anguilla":"8","Antarctica":"9","Antigua and Barb.":"10","Argentina":"11","Armenia":"12","Aruba":"13","Australia":"14","Austria":"15","Azerbaijan":"16","Bahamas":"17","Bahrain":"18","Bangladesh":"19","Barbados":"20","Belarus":"21","Belgium":"22","Belize":"23","Benin":"24","Bermuda":"25","Bhutan":"26","Bolivia":"27","Bosnia and Herz.":"28","Botswana":"29","Br. Indian Ocean Ter.":"30","Brazil":"31","British Virgin Is.":"32","Brunei":"33","Bulgaria":"34","Burkina Faso":"35","Burundi":"36","Cabo Verde":"37","Cambodia":"38","Cameroon":"39","Canada":"40","Cayman Is.":"41","Central African Rep.":"42","Chad":"43","Chile":"44","China":"45","Colombia":"46","Comoros":"47","Congo":"48","Cook Is.":"49","Costa Rica":"50","Cote d'Ivoire":"51","Croatia":"52","Cuba":"53","Curacao":"54","Cyprus":"55","Czechia":"56","Dem. Rep. Congo":"57","Denmark":"58","Djibouti":"59","Dominica":"60","Dominican Rep.":"61","Ecuador":"62","Egypt":"63","El Salvador":"64","Eq. Guinea":"65","Eritrea":"66","Estonia":"67","eSwatini":"68","Ethiopia":"69","Faeroe Is.":"70","Falkland Is.":"71","Fiji":"72","Finland":"73","Fr. Polynesia":"74","Fr. S. Antarctic Lands":"75","France":"76","Gabon":"77","Gambia":"78","Georgia":"79","Germany":"80","Ghana":"81","Gibraltar":"82","Greece":"83","Greenland":"84","Grenada":"85","Guam":"86","Guatemala":"87","Guernsey":"88","Guinea":"89","Guinea-Bissau":"90","Guyana":"91","Haiti":"92","Heard I. and McDonald Is.":"93","Honduras":"94","Hong Kong":"95","Hungary":"96","Iceland":"97","India":"98","Indonesia":"99","Iran":"100","Iraq":"101","Ireland":"102","Isle of Man":"103","Israel":"104","Italy":"105","Jamaica":"106","Japan":"107","Jersey":"108","Jordan":"109","Kazakhstan":"110","Kenya":"111","Kiribati":"112","Kosovo":"113","Kuwait":"114","Kyrgyzstan":"115","Laos":"116","Latvia":"117","Lebanon":"118","Lesotho":"119","Liberia":"120","Libya":"121","Liechtenstein":"122","Lithuania":"123","Luxembourg":"124","Macao":"125","Macedonia":"126","Madagascar":"127","Malawi":"128","Malaysia":"129","Maldives":"130","Mali":"131","Malta":"132","Marshall Is.":"133","Mauritania":"134","Mauritius":"135","Mexico":"136","Micronesia":"137","Moldova":"138","Monaco":"139","Mongolia":"140","Montenegro":"141","Montserrat":"142","Morocco":"143","Mozambique":"144","Myanmar":"145","N. Cyprus":"146","N. Mariana Is.":"147","Namibia":"148","Nauru":"149","Nepal":"150","Netherlands":"151","New Caledonia":"152","New Zealand":"153","Nicaragua":"154","Niger":"155","Nigeria":"156","Niue":"157","Norfolk Island":"158","North Korea":"159","Norway":"160","Oman":"161","Pakistan":"162","Palau":"163","Palestine":"164","Panama":"165","Papua New Guinea":"166","Paraguay":"167","Peru":"168","Philippines":"169","Pitcairn Is.":"170","Poland":"171","Portugal":"172","Puerto Rico":"173","Qatar":"174","Romania":"175","Russia":"176","Rwanda":"177","S. Geo. and the Is.":"178","S. Sudan":"179","Saint Helena":"180","Saint Lucia":"181","Samoa":"182","San Marino":"183","Sao Tome and Principe":"184","Saudi Arabia":"185","Senegal":"186","Serbia":"187","Seychelles":"188","Siachen Glacier":"189","Sierra Leone":"190","Singapore":"191","Sint Maarten":"192","Slovakia":"193","Slovenia":"194","Solomon Is.":"195","Somalia":"196","Somaliland":"197","South Africa":"198","South Korea":"199","Spain":"200","Sri Lanka":"201","St-Barthelemy":"202","St-Martin":"203","St. Kitts and Nevis":"204","St. Pierre and Miquelon":"205","St. Vin. and Gren.":"206","Sudan":"207","Suriname":"208","Sweden":"209","Switzerland":"210","Syria":"211","Taiwan":"212","Tajikistan":"213","Tanzania":"214","Thailand":"215","Timor-Leste":"216","Togo":"217","Tonga":"218","Trinidad and Tobago":"219","Tunisia":"220","Turkey":"221","Turkmenistan":"222","Turks and Caicos Is.":"223","Tuvalu":"224","U.S. Minor Outlying Is.":"225","U.S. Virgin Is.":"226","Uganda":"227","Ukraine":"228","United Arab Emirates":"229","United Kingdom":"230","United States of America":"231","Uruguay":"232","Uzbekistan":"233","Vanuatu":"234","Vatican":"235","Venezuela":"236","Vietnam":"237","W. Sahara":"238","Wallis and Futuna Is.":"239","Yemen":"240","Zambia":"241","Zimbabwe":"242"})
