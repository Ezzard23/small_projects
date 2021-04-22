import pandas as pd 
import json
from datetime import date
from datetime import datetime
import re

# read file

jsonFile = open('sample-data.json','r')
jsonData = jsonFile.read()

# parse 

jobj = json.loads(jsonData)
#print(jobj['aggregations'])

list1 = jobj['aggregations']
"""
print(list1)
print(list1['2']['buckets'][0]['3']['buckets'][0]['1'])
"""
# variables
name = list1['2']['buckets'][0]['3']['buckets'][0]['key']
size = list1['2']['buckets'][0]['3']['buckets'][0]['1']['value']
domain = list1['2']['buckets'][0]['key']


print("Name", name)
print("Size: ", size)
print(domain)
# export data  to json
match = re.search(r'\d{4}-\d{2}-\d{2}', name)
objDate = datetime.strptime(match.group(), '%Y-%m-%d').date()
print(objDate)

"""
exportData = {
    "@timestamp" : str(date.today()),
    "domain" : domain,
    "objectGroup": [
        {
            "name" : name,
            "date" : "objDate",
            "size" : size
        }
   ]
   }

print(exportData)


with open('ExportData.json','w' ) as f:
    json.dump(exportData, f)

"""
 