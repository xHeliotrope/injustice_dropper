import csv
import json

def get_citation_record(requiredFields,targetData):
    if type(requiredFields)!=dict:
        return 'The required fields (the first function argument) must be in dictionary format'
    #targetData must be 'citations' on 'violations'
    if targetData!='citations' and targetData!='violations':
        return 'The targeted dataset (the second function argument) is invalid'
    #going to need to do something different with the path
    with open('C:\Users\Alexander\Documents\GitHub\injustice_dropper\data\\'+targetData+'.csv', 'rb') as citations:
        reader = csv.DictReader(citations)
        for citationDict in reader:
            #default is no match
            match=0
            for key in requiredFields.keys():
                if requiredFields[key]==citationDict[key]:
                    match=1
                else:
                    match=0
            if match==1:
                return citationDict
        return "No match was found!"
        
testPositive={'court_address': '7150 Natural Bridge Road', 'first_name': 'Kathleen'}
testNegative={'court_address': 'ass road', 'first_name': 'assface'}
print get_citation_record(testPositive,'citations')
print get_citation_record(testNegative,'citations')        

testPositive={'violation_number': '682690971-01', 'violation_description': 'Improper Passing'}
testNegative={'violation_number': '12345', 'violation_description': 'dookie'}
print get_citation_record(testPositive,'violations')
print get_citation_record(testNegative,'violations')        

#poly is a list of (x,y) tuples
def point_in_poly(x,y,polyByList):

   poly=[(t[0],t[1]):t in polyByList]


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

# Test a vertex for inclusion
poligono = [(-33.416032,-70.593016), (-33.415370,-70.589604),
(-33.417340,-70.589046), (-33.417949,-70.592351),
(-33.416032,-70.593016)]
lat= -33.416032
lon= -70.593016

print point_in_poly(lat, lon, poligono)

# test a boundary point for inclusion
poly2 = [(1,1), (5,1), (5,5), (1,5), (1,1)]
x = 3
y = 1
print point_in_poly(x, y, poly2)

def get_court_id(x,y):
    json_data=open('C:\Users\Alexander\Documents\GitHub\injustice_dropper\data\courts.geojson.txt').read()
    
    data = json.loads(json_data)    

    return data                                