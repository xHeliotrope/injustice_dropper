"""
the functions
    get_record_csv
    get_court_id
are intended to be the closest interface points with the front end.
each has comments on its function prior to its definition and a series of demonstrative example calls afterwards

get_records_csv will require some changes to work with a db - it has been written to hopefully make this easy
get_court_id will eventually need a change to its file path on line 134
"""


import csv
import json

import os

import itertools

    
#this is a helper function intended to be called by another function making a data call that produces a (pseudo) list of dictionaries    
def match_in_list(requiredFields,pseudoList):
    matches=[]
    for citationDict in pseudoList:
        #default is no match
        match=1
        for key in requiredFields.keys():
            if requiredFields[key]==citationDict[key]:
                "nothing happens"
            else:
                match=0
        if match==1:
            matches.append(citationDict)
    if len(matches)>0:
        return matches
    else:
        return "No match was found!"

#this function is an example of a type intended to be called from the front end
#this function will be superseded by a similar one which makes a database call  
def get_record_csv(requiredFields,targetData):        
    if type(requiredFields)!=dict:
        return 'The required fields (the first function argument) must be in dictionary format'
    #targetData must be 'citations' on 'violations'
    if targetData!='citations' and targetData!='violations' and targetData!='Warrants':
        return 'The targeted dataset (the second function argument) is invalid'
    #going to need to do something different with the path
    with open('C:\Users\Alexander\Documents\GitHub\injustice_dropper\data\\'+targetData+'.csv', 'rb') as citations:
        reader = csv.DictReader(citations)
        return match_in_list(requiredFields,reader)    

#this is a demonstrative test of a front end function        
testPositive={'court_address': '7150 Natural Bridge Road', 'first_name': 'Kathleen'}
testNegative={'court_address': 'ass road', 'first_name': 'assface'}
print(get_record_csv(testPositive,'citations'))
print(get_record_csv(testNegative,'citations'))        

testPositive={'violation_number': '682690971-01', 'violation_description': 'Improper Passing'}
testNegative={'violation_number': '12345', 'violation_description': 'dookie'}
print(get_record_csv(testPositive,'violations'))
print(get_record_csv(testNegative,'violations'))       

testPositive={'Defendant': 'AARON, ANDRE L', 'ZIP Code': '63103'}
testNegative={'Defendant': 'AARON, BOOTY L', 'ZIP Code': '99999'}
print(get_record_csv(testPositive,'Warrants'))
print(get_record_csv(testNegative,'Warrants'))       

#this is a helper function not intended to be called by the front end
#this function formats inputs for point_in_poly
def polygon_reformat(polyListCoords):
    return [(t[0],t[1]) for t in polyListCoords]

#polygon vs multi polygon key is in the same layer as coordinates
#this function deals with some issues related to non simply connected multipolygons
#this is a helper function not intended to be called by the front end
def polygon_inclusion_resolver(x,y,geometryDict):
    if geometryDict['type']=='Polygon':
        cleanedList=[polygon_reformat(geometryDict['coordinates'][0])]
    if geometryDict['type']=='MultiPolygon':
        cleanedList=[]
        for polygon in geometryDict['coordinates'][0]:
            cleanedList.append(polygon_reformat(polygon)) 
    #count how many polygons the point is contained in from the list    
   
    containedCount=0
    for i,polygonList in enumerate(cleanedList):
        if point_in_poly(x,y,polygonList)=="IN":
            containedCount+=1
    if containedCount%2==1:
        return "IN"
    else:
        return "OUT"
                    
        
#poly is a list of (x,y) tuples
#this is a helper function not intended to be called by the front end
def point_in_poly(x,y,poly):

   # check if point is a vertex
   if (x,y) in poly: return "IN"

   # check if point is on a boundary
   for i in range(len(poly)):
      p1 = None
      p2 = None
      if i==0:
         p1 = poly[0]
         p2 = poly[1]
      else:
         p1 = poly[i-1]
         p2 = poly[i]
      if p1[1] == p2[1] and p1[1] == y and x > min(p1[0], p2[0]) and x < max(p1[0], p2[0]):
         return "IN"
      
   n = len(poly)
   inside = False

   p1x,p1y = poly[0]
   for i in range(n+1):
      p2x,p2y = poly[i % n]
      if y > min(p1y,p2y):
         if y <= max(p1y,p2y):
            if x <= max(p1x,p2x):
               if p1y != p2y:
                  xints = (y-p1y)*(p2x-p1x)/(p2y-p1y)+p1x
               if p1x == p2x or x <= xints:
                  inside = not inside
      p1x,p1y = p2x,p2y

   if inside: return "IN"
   else: return "OUT"

"""
example key structure to get to the actual list of coordinates
test['features'][0]['geometry']['coordinates'][0]
example key structure to get to court properties
test['features'][0]['properties']

the 0 is just to pull the first record in the list as an example
"""
#this function takes latitude and longitude coords and returns a dictionary mapping court id to full court data
#this function is intended to be called from the front end
def get_court_id(lat,long):
    json_data=open('C:/Users/Alexander/Documents/GitHub/injustice_dropper/data/courts.geojson.txt').read()
    
    rawData = json.loads(json_data)
    courtIdDict={}
    for courtRecord in rawData['features']:
        #the code needs lat and long to be flipped because it was written in the middle of the night
        if polygon_inclusion_resolver(long,lat,courtRecord['geometry'])=="IN":
            courtIdDict[courtRecord['properties']['court_id']]=courtRecord['properties']
    return courtIdDict

#this is a demonstrative test of a front end function      
#on the boundary of florissant and unincorpated county        
print(get_court_id(38.8086707727844,-90.2860498354983))    
#just unincorporated county
print(get_court_id(38.80867077279,-90.2860498354983))
#the vinita terrace courthouse
print(get_court_id(38.685607,-90.329282))
#in the indian ocean somewhere, produces an empty dict
print(get_court_id(0,0))    

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
            if courtName.lower()==courtRecord['properties']['court_name'].lower():
                specificCourt=courtRecord['properties']
            if key not in courtKeys:
                courtKeys[key]={'total':0,'sum':0,'type':type(courtRecord['properties'][key]),'masterList':[]}
            courtKeys[key]['masterList'].append(courtRecord['properties'][key])
            try:
                if courtRecord['court_name'] not in courtNames:
                    floatValue=float(courtRecord['properties'][key].replace(",",""))
                    courtKeys[key]['total']+=1
                    courtKeys[key]['sum']+=floatValue
                    courtNames.append(courtRecord['court_name'])
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
    
print(get_analytics_raw('country club hills')['comparisons'])

def name_input_permuter(nameString):
    tallWords=[]
    for preWord in nameString.split():
        for word in preWord.split(','):
            tallWords.append(word)
    finalOutput={'firstLast':[],'libraryStyle':[]}
    for t in itertools.permutations(tallWords,3):
        finalOutput['firstLast'].append((t[0],t[1]))
        finalOutput['libraryStyle'].append(t[0]+','+t[1]+' '+t[2][0])
            
    return finalOutput
    
    
