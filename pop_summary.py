import csv
import json

import os

import itertools

def get_analytics_raw(courtName):
    #get the raw court data from geojson    
    json_data=open('C:/Users/Alexander/Documents/GitHub/injustice_dropper/data/courts.geojson.txt').read()
    rawData = json.loads(json_data)
    #a big list of all possible court data with summary data
    courtKeys={}
    courtNames=[]
    for courtRecord in rawData['features']:
        for key in courtRecord['properties']:
            #record data for the specific court when appropriate
            #print(courtRecord)
            if courtName.lower()==courtRecord['properties']['court_name'].lower():
                specificCourt=courtRecord['properties']
            if key not in courtKeys:
                courtKeys[key]={'total':0,'sum':0,'type':type(courtRecord['properties'][key]),'masterList':[]}
            courtKeys[key]['masterList'].append(courtRecord['properties'][key])
            try:
                if courtRecord['properties']['court_name'] not in courtNames:
                    print "try"
                    print courtNames
                    print courtRecord['properties']['court_name']
                    floatValue=float(courtRecord['properties'][key].replace(",",""))
                    courtKeys[key]['total']+=1
                    courtKeys[key]['sum']+=floatValue
                    courtNames.append(courtRecord['properties']['court_name'])
            except ValueError:
                'do nothing'
    comparisons={}
    for key in specificCourt:
        try:
            if float(courtKeys[key]['sum'])!=0 and float(courtKeys[key]['total'])!=0:
                comparisons[key]={
                    'userValue':specificCourt[key],
                    'average':float(courtKeys[key]['sum'])/courtKeys[key]['total'],
                    'percentDiff':(float(specificCourt[key])-float(courtKeys[key]['sum'])/courtKeys[key]['total'])/(float(courtKeys[key]['sum'])/courtKeys[key]['total'])
                }  
            else:
                comparisons[key]={
                    'userValue':specificCourt[key],
                    'average':0,
                    'percentDiff':0
                }  
        except ValueError:
                'do nothing'                    
    
    return {'comparisons':comparisons,'allData':courtKeys}
    
data =get_analytics_raw('country club hills')['allData']
