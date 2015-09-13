import csv
import json
import os
import itertools

histogram={}
#going to need to do something different with the path
with open('C:\Users\Alexander\Documents\GitHub\injustice_dropper\data\\violations.csv', 'rb') as citations:
    reader = csv.DictReader(citations)
    for row in reader:
        key=row['violation_description']
        if key not in histogram:
            histogram[key]={'fine_amount':{'sum':0,'total':0},'court_cost':{'sum':0,'total':0}}
        if len(row['court_cost'])>0:
            cost=float(row['court_cost'].strip('$'))
            histogram[key]['court_cost']['sum']+=cost
            histogram[key]['court_cost']['total']+=1
        if len(row['fine_amount'])>0:
            cost=float(row['fine_amount'].strip('$'))
            histogram[key]['fine_amount']['sum']+=cost
            histogram[key]['fine_amount']['total']+=1
print histogram
output={}
for key in histogram:
    output[key]={
        'fine_amount':float(histogram[key]['fine_amount']['sum'])/float(histogram[key]['fine_amount']['total']),
        'court_cost':float(histogram[key]['court_cost']['sum'])/float(histogram[key]['court_cost']['total']),
    }
print(output)        
        