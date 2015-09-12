
import csv
import json
import os

def get_court_id(lat,long):
    json_data=open(os.getcwd() + '/data/courts.geojson.txt').read()
    
    rawData = json.loads(json_data)
    courtIdDict={}
    for courtRecord in rawData['features']:
        #the code needs lat and long to be flipped because it was written in the middle of the night
        if polygon_inclusion_resolver(long,lat,courtRecord['geometry'])=="IN":
            courtIdDict[courtRecord['properties']['court_name']]=courtRecord['properties']
    return courtIdDict

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

#this is a helper function not intended to be called by the front end
#this function formats inputs for point_in_poly
def polygon_reformat(polyListCoords):
    return [(t[0],t[1]) for t in polyListCoords]

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