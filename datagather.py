# apitest.py
import requests
import json
import os

CONVERSIONDICT = {
    "AL": "Alabama",
    "AK": "Alaska",
    "AZ": "Arizona",
    "AR": "Arkansas",
    "CA": "California",
    "CO": "Colorado",
    "CT": "Connecticut",
    "DE": "Delaware",
    "FL": "Florida",
    "GA": "Georgia",
    "HI": "Hawaii",
    "ID": "Idaho",
    "IL": "Illinois",
    "IN": "Indiana",
    "IA": "Iowa",
    "KS": "Kansas",
    "KY": "Kentucky",
    "LA": "Louisiana",
    "ME": "Maine",
    "MD": "Maryland",
    "MA": "Massachusetts",
    "MI": "Michigan",
    "MN": "Minnesota",
    "MS": "Mississippi",
    "MO": "Missouri",
    "MT": "Montana",
    "NE": "Nebraska",
    "NV": "Nevada",
    "NH": "New Hampshire",
    "NJ": "New Jersey",
    "NM": "New Mexico",
    "NY": "New York",
    "NC": "North Carolina",
    "ND": "North Dakota",
    "OH": "Ohio",
    "OK": "Oklahoma",
    "OR": "Oregon",
    "PA": "Pennsylvania",
    "RI": "Rhode Island",
    "SC": "South Carolina",
    "SD": "South Dakota",
    "TN": "Tennessee",
    "TX": "Texas",
    "UT": "Utah",
    "VT": "Vermont",
    "VA": "Virginia",
    "WA": "Washington",
    "WV": "West Virginia",
    "WI": "Wisconsin",
    "WY": "Wyoming"
}


# get ready to export to email
# read in all active cases currently 
# write function to loop over 
# CONCATENATE NEW DATA WHEN IT COMES into json files 
# make allergy filter and make new notify python file that tells u if 



#dont need
# def adress_to_latlon(file: json) ->list:
#     geolocator = Nominatim(user_agent="getLoc")

#     locDict={
#           "city":data["results"][0]["city"],
#           "state":CONVERSIONDICT[data["results"][0]["state"]],
#           "country":"United States of America"
#     }
#     location = geolocator.geocode(locDict)
#     return location.latitude, location.longitude


# print(adress_to_latlon(data))






def get_active_cases(offset:int,folder="recalldata") ->dict:
    
    final_dict={

    }
    
    if(folder=="recallData"):
        path=os.path.join("knight",folder)
    else:
        path=os.path.join(folder)
    
    #get in states, then get nationwide and if id are not the same then add it in to json
    for key in list(CONVERSIONDICT.keys()):  
        r=requests.get(f'https://api.fda.gov/food/enforcement.json?search=distribution_pattern:"{key}"+AND+status:"Ongoing"+AND+(classification:"Class II"+classification:"Class I")&limit=500')
        
        if(r.status_code==200):
            recallData=r.json()

            final_dict[f"{key}"]=recallData

            with open(f'{path}/{key}.json', 'w') as json_file1:
                    json.dump(recallData, json_file1, indent=4)

        else: 
            print(f"ERROR: RESPONSE CODE{r.status_code} at {key}")

    for value in list(CONVERSIONDICT.values()): 
            r=requests.get(f'https://api.fda.gov/food/enforcement.json?search=distribution_pattern:"{value}"+AND+status:"Ongoing"+AND+(classification:"Class II"+classification:"Class I")&limit=500')
            
            if(r.status_code==200):
                recallData=r.json()

                final_dict[f"{value}"]=recallData

                with open(f'{path}/{value}.json', 'w') as json_file2:
                        json.dump(recallData, json_file2, indent=4)

            else: 
                print(f"ERROR: RESPONSE CODE{r.status_code} at {value}")

    return final_dict
    

    

def merge_json_results(json1_filename:str, json2_filename:str, makes_files:bool, folder='recalldata'):
    # Construct full file paths
    json1_path = os.path.join(folder, json1_filename)
    json2_path = os.path.join(folder, json2_filename)

    # Load JSON data from files
    with open(json1_path, 'r') as file1:
        json1 = json.load(file1)
    
    with open(json2_path, 'r') as file2:
        json2 = json.load(file2)
    
    # Concatenate the 'results' lists from both JSON objects
    if 'results' in json1 and 'results' in json2:
        json3 = json1  # Start with json1
        json3['results'] = json1['results'] + json2['results']  # Concatenate results from both
    else:
        raise KeyError("One or both JSONs do not contain a 'results' key.")

    # Overwrite json1 file with the new json3 content
    if(makes_files):
        with open(json1_path, 'w') as file1:
            json.dump(json3, file1, indent=4)
        
        print(f"Successfully merged and saved to {json1_path}")

        if os.path.exists(json2_path):
            os.remove(json2_path)
            print(f"Deleted {json2_path}")
        else:
            print(f"{json2_path} does not exist.")
    return json3



def collect_data(offset:int,folder="recalldata"):  #call this function to collect all data
        
    get_active_cases(offset,folder=folder)
    for i in range(0,50-offset):
        key=list(CONVERSIONDICT.keys())[i]
        value=list(CONVERSIONDICT.values())[i]
        merge_json_results(f'{key}.json', f'{value}.json',makes_files=True,folder=folder)



# collect_data(1)




    