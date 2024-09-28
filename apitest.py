# apitest.py
import requests
import pandas as pd
import numpy as np
import json
from geopy.geocoders import Nominatim   

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


# function to get lat and lon from adress 
# other helper functions
# gonna start with active ones (make api call for that)
# read in apropriate data from API and put it in a dictionary  
# get ready to export to email


with open("food_recall_data.json", "r") as file:
    data = json.load(file)

def adress_to_latlon(file: json) ->list:
    geolocator = Nominatim(user_agent="getLoc")

    locDict={
          "city":data["results"][0]["city"],
          "state":CONVERSIONDICT[data["results"][0]["state"]],
          "country":"United States of America"
    }
    location = geolocator.geocode(locDict)
    return location.latitude, location.longitude


print(adress_to_latlon(data))



    