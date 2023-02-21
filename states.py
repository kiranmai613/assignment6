# 2. Create a dictionary of any 7 Indian states and their capitals. Write this into a JSON file.
import json
Capital={
    "tamilnadu":"chennai",
    "goa":"panama",
    "kerala":"kochin",
    "telangana":"hyd",
    "karnataka":"banglore"
    }
with open("sample.json","w") as outfile:
    json.dump(Capital,outfile)

