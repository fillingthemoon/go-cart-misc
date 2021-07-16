import settings
import handlers.base_handler
import csv

class CartogramHandler(handlers.base_handler.BaseCartogramHandler):

    def get_name(self):
        return "Washington (U.S. State)"

    def get_gen_file(self):
        return "{}/washington_processedmap.json".format(settings.CARTOGRAM_DATA_DIR)
    
    def validate_values(self, values):

        if len(values) != 39:
            return False
        
        for v in values:
            if type(v) != float:
                return False

        return True
    
    def gen_area_data(self, values):
        return """cartogram_id,Region Data,Region Name,Inset
1,{},Adams,L
2,{},Asotin,L
3,{},Benton,L
4,{},Chelan,L
5,{},Clallam,L
6,{},Clark,L
7,{},Columbia,L
8,{},Cowlitz,L
9,{},Douglas,L
10,{},Ferry,L
11,{},Franklin,L
12,{},Garfield,L
13,{},Grant,L
14,{},Grays Harbor,L
15,{},Island,L
16,{},Jefferson,L
17,{},King,L
18,{},Kitsap,L
19,{},Kittitas,L
20,{},Klickitat,R
21,{},Lewis,R
22,{},Lincoln,R
23,{},Mason,R
24,{},Okanogan,R
25,{},Pacific,R
26,{},Pend Oreille,R
27,{},Pierce,R
28,{},San Juan,R
29,{},Skagit,R
30,{},Skamania,R
31,{},Snohomish,R
32,{},Spokane,R
33,{},Stevens,R
34,{},Thurston,R
35,{},Wahkiakum,R
36,{},Walla Walla,R
37,{},Whatcom,R
38,{},Whitman,R
39,{},Yakima,R""".format(*values)
    
    def expect_geojson_output(self):
        return True

    def csv_to_area_string_and_colors(self, csvfile):

        return self.order_by_example(csv.reader(csvfile), "County", 0, 1, 2, 3, ["Adams","Asotin","Benton","Chelan","Clallam","Clark","Columbia","Cowlitz","Douglas","Ferry","Franklin","Garfield","Grant","Grays Harbor","Island","Jefferson","King","Kitsap","Kittitas","Klickitat","Lewis","Lincoln","Mason","Okanogan","Pacific","Pend Oreille","Pierce","San Juan","Skagit","Skamania","Snohomish","Spokane","Stevens","Thurston","Wahkiakum","Walla Walla","Whatcom","Whitman","Yakima"], [0.0 for i in range(0,39)], {"Adams":"1","Asotin":"2","Benton":"3","Chelan":"4","Clallam":"5","Clark":"6","Columbia":"7","Cowlitz":"8","Douglas":"9","Ferry":"10","Franklin":"11","Garfield":"12","Grant":"13","Grays Harbor":"14","Island":"15","Jefferson":"16","King":"17","Kitsap":"18","Kittitas":"19","Klickitat":"20","Lewis":"21","Lincoln":"22","Mason":"23","Okanogan":"24","Pacific":"25","Pend Oreille":"26","Pierce":"27","San Juan":"28","Skagit":"29","Skamania":"30","Snohomish":"31","Spokane":"32","Stevens":"33","Thurston":"34","Wahkiakum":"35","Walla Walla":"36","Whatcom":"37","Whitman":"38","Yakima":"39"})
