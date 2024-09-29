import json


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


dir = "recalldata/"
for x in state_count.keys():
    with open(dir+ x+ '.json') as f:
        d = json.load(f)

    count = int(d['meta']['results']['total'])
    state_count[x] += count

f = open('state_counter.txt', 'w')
for x in state_count.values():
    f.write(str(x) + '\n')