import json

with open('raw_data.json') as f:
    d = json.load(f)

d = d["results"]
state_count = {
    "AL": 0,  # Alabama
    "AK": 0,  # Alaska
    "AZ": 0,  # Arizona
    "AR": 0,  # Arkansas
    "CA": 0,  # California
    "CO": 0,  # Colorado
    "CT": 0,  # Connecticut
    "DE": 0,  # Delaware
    "FL": 0,  # Florida
    "GA": 0,  # Georgia
    "HI": 0,  # Hawaii
    "ID": 0,  # Idaho
    "IL": 0,  # Illinois
    "IN": 0,  # Indiana
    "IA": 0,  # Iowa
    "KS": 0,  # Kansas
    "KY": 0,  # Kentucky
    "LA": 0,  # Louisiana
    "ME": 0,  # Maine
    "MD": 0,  # Maryland
    "MA": 0,  # Massachusetts
    "MI": 0,  # Michigan
    "MN": 0,  # Minnesota
    "MS": 0,  # Mississippi
    "MO": 0,  # Missouri
    "MT": 0,  # Montana
    "NE": 0,  # Nebraska
    "NV": 0,  # Nevada
    "NH": 0,  # New Hampshire
    "NJ": 0,  # New Jersey
    "NM": 0,  # New Mexico
    "NY": 0,  # New York
    "NC": 0,  # North Carolina
    "ND": 0,  # North Dakota
    "OH": 0,  # Ohio
    "OK": 0,  # Oklahoma
    "OR": 0,  # Oregon
    "PA": 0,  # Pennsylvania
    "RI": 0,  # Rhode Island
    "SC": 0,  # South Carolina
    "SD": 0,  # South Dakota
    "TN": 0,  # Tennessee
    "TX": 0,  # Texas
    "UT": 0,  # Utah
    "VT": 0,  # Vermont
    "VA": 0,  # Virginia
    "WA": 0,  # Washington
    "WV": 0,  # West Virginia
    "WI": 0,  # Wisconsin
    "WY": 0   # Wyoming
}

state_recalls = {
    "AL": [],  # Alabama
    "AK": [],  # Alaska
    "AZ": [],  # Arizona
    "AR": [],  # Arkansas
    "CA": [],  # California
    "CO": [],  # Colorado
    "CT": [],  # Connecticut
    "DE": [],  # Delaware
    "FL": [],  # Florida
    "GA": [],  # Georgia
    "HI": [],  # Hawaii
    "ID": [],  # Idaho
    "IL": [],  # Illinois
    "IN": [],  # Indiana
    "IA": [],  # Iowa
    "KS": [],  # Kansas
    "KY": [],  # Kentucky
    "LA": [],  # Louisiana
    "ME": [],  # Maine
    "MD": [],  # Maryland
    "MA": [],  # Massachusetts
    "MI": [],  # Michigan
    "MN": [],  # Minnesota
    "MS": [],  # Mississippi
    "MO": [],  # Missouri
    "MT": [],  # Montana
    "NE": [],  # Nebraska
    "NV": [],  # Nevada
    "NH": [],  # New Hampshire
    "NJ": [],  # New Jersey
    "NM": [],  # New Mexico
    "NY": [],  # New York
    "NC": [],  # North Carolina
    "ND": [],  # North Dakota
    "OH": [],  # Ohio
    "OK": [],  # Oklahoma
    "OR": [],  # Oregon
    "PA": [],  # Pennsylvania
    "RI": [],  # Rhode Island
    "SC": [],  # South Carolina
    "SD": [],  # South Dakota
    "TN": [],  # Tennessee
    "TX": [],  # Texas
    "UT": [],  # Utah
    "VT": [],  # Vermont
    "VA": [],  # Virginia
    "WA": [],  # Washington
    "WV": [],  # West Virginia
    "WI": [],  # Wisconsin
    "WY": []   # Wyoming
}

for i in range(len(d)):
    states = d[i]["distribution_pattern"]
    product_id = d[i]["event_id"]

    for x in state_count:
        if( x in states):
            state_count[x] += 1
            state_recalls[x].append(product_id)

