# apitest.py
import requests
import json
import os
import time

from datagather import CONVERSIONDICT,collect_data

def check_for_new_recalls(offset:int)->dict: # states affected returns 
   
    print("checking for new recalls")
    
    if not os.path.exists(f"./tempdata"):
        
        os.mkdir("./tempdata")

    new_recalls = {
        "AL": [],
        "AK": [],
        "AZ": [],
        "AR": [],
        "CA": [],
        "CO": [],
        "CT": [],
        "DE": [],
        "FL": [],
        "GA": [],
        "HI": [],
        "ID": [],
        "IL": [],
        "IN": [],
        "IA": [],
        "KS": [],
        "KY": [],
        "LA": [],
        "ME": [],
        "MD": [],
        "MA": [],
        "MI": [],
        "MN": [],
        "MS": [],
        "MO": [],
        "MT": [],
        "NE": [],
        "NV": [],
        "NH": [],
        "NJ": [],
        "NM": [],
        "NY": [],
        "NC": [],
        "ND": [],
        "OH": [],
        "OK": [],
        "OR": [],
        "PA": [],
        "RI": [],
        "SC": [],
        "SD": [],
        "TN": [],
        "TX": [],
        "UT": [],
        "VT": [],
        "VA": [],
        "WA": [],
        "WV": [],
        "WI": [],
        "WY": []
    }


    collect_data(offset=offset,folder="tempdata")

    for key in new_recalls.keys():
        print(key)
    
        with open (f"./knight/recalldata/{key}.json","r") as p:
            base_json=json.load(p)
        with open (f"./tempdata/{key}.json","r" ) as w:
            inspecting_json=json.load(w)

        if 'results' in inspecting_json and base_json:
            results1 = inspecting_json['results']
            results2 = base_json['results']
            
            

            new_entries = [entry for entry in results2 if entry not in results1]
            #print(new_entries)

            if(new_entries):
                new_recalls[key]+=new_entries
            #else:
                #print("no new entries")

        else: 
            raise KeyError("One or both jsons do not contain a 'meta' key")
        
    
    return new_recalls

            
# print(check_for_new_recalls(0))
    



# time.sleep(10)

