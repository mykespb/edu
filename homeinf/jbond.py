#!/usr/bin/env python

# Mikhail (myke) Kolodin, 2022
# 2022-04-30 2022-04-30 1.1
# jbond.py

from pprint import pp

agent = {"name": {"first": "James", "last": "Bond"}, "age": 30, "gender": "male", "country": "UK", "address": {"city": "London", "street": "85 Albert Embankment"}, "duty": {"title": "Commander", "organization": "Secret Intelligence Service", "org_code": "MI6", "coordinates": "51°29′14″N 00°07′27″W", "personal_code": "007", "occupation": "Intelligence Agent"}}

print(agent, "\n\n")
pp(agent, width=50)

# ~ {'name': {'first': 'James', 'last': 'Bond'}, 'age': 30, 'gender': 'male', 'country': 'UK', 'address': {'city': 'London', 'street': '85 Albert Embankment'}, 'duty': {'title': 'Commander', 'organization': 'Secret Intelligence Service', 'org_code': 'MI6', 'coordinates': '51°29′14″N 00°07′27″W', 'personal_code': '007', 'occupation': 'Intelligence Agent'}} 


# ~ {'name': {'first': 'James', 'last': 'Bond'},
 # ~ 'age': 30,
 # ~ 'gender': 'male',
 # ~ 'country': 'UK',
 # ~ 'address': {'city': 'London',
             # ~ 'street': '85 Albert Embankment'},
 # ~ 'duty': {'title': 'Commander',
          # ~ 'organization': 'Secret Intelligence '
                          # ~ 'Service',
          # ~ 'org_code': 'MI6',
          # ~ 'coordinates': '51°29′14″N 00°07′27″W',
          # ~ 'personal_code': '007',
          # ~ 'occupation': 'Intelligence Agent'}}
# ~ {'name': {'first': 'Sherlock', 'last': 'Holmes'}, 'address': {'country': 'UK', 'city': 'London', 'street': '221b Baker St.'}, 'occupation': 'Private detective', 'nationality': 'British'} 


detective = {
    "name": {"first": "Sherlock",
        "last": "Holmes"},
    "address": {"country": "UK",
        "city": "London",
        "street": "221b Baker St."},
    "occupation": "Private detective",
    "nationality": "British"
    }

print(detective, "\n\n")
pp(detective, width=50)

# ~ {'name': {'first': 'Sherlock', 'last': 'Holmes'}, 'address': {'country': 'UK', 'city': 'London', 'street': '221b Baker St.'}, 'occupation': 'Private detective', 'nationality': 'British'} 


# ~ {'name': {'first': 'Sherlock', 'last': 'Holmes'},
 # ~ 'address': {'country': 'UK',
             # ~ 'city': 'London',
             # ~ 'street': '221b Baker St.'},
 # ~ 'occupation': 'Private detective',
 # ~ 'nationality': 'British'}
