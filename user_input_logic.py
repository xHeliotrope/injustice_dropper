import itertools
from pull_from_dataset import *

"""could add some more thorough splitting to deal with punctuation"""

def inputted_name_permuter(nameString):
    tallWords=[]
    for preWord in nameString.split():
        for word in preWord.split(','):
            tallWords.append(word)
    finalOutput={'firstLast':[],'libraryStyle':[]}
    for t in itertools.permutations(tallWords,3):
        finalOutput['firstLast'].append({'first_name':t[0],'last_name':t[1]})
        finalOutput['libraryStyle'].append({'defendant':t[0]+', '+t[1]+' '+t[2][0]})
            
    return finalOutput

#need to do some cleanup to make sure everything is lowercase    
def get_warrant_names():
    return [{'defendant':'aaron, andre l'}]
    
def get_citation_names():
    return [{'first_name':'mildred','last_name':'collins'}]    

def verify_name(nameString,recordType):
    nameString=nameString.lower()
    if recordType=='Warrants':
        namesToCheck=get_warrant_names()
        potentialNames=inputted_name_permuter(nameString)['libraryStyle']
    elif recordType=='citation':
        namesToCheck=get_citation_names()
        potentialNames=inputted_name_permuter(nameString)['firstLast']
    else:
        return "Invalid Record Type"
    #check for possible name matches and record them
    candidateName=""    
    for name in namesToCheck:
        if name in potentialNames:
            candidateName=name
            
    #print(potentialNames)
    
    if len(candidateName)>0:
        return candidateName
    else:
        return 0
            
#print(verify_name('my aaron name is andre you l','Warrants'))
#print(verify_name('collins asks what is a mildred','citation'))

#format of name will need to vary with record type
def verify_second_factor(name,response,targetedField,recordType):
    responseWords=response.split()
    for word in responseWords:
        #needs to be changed away from csv format at some point
        if recordType=='Warrants':
            queryDict={
                "Defendant":name,
                targetedField:word
            }
        elif recordType=='citations':
            queryDict={
                "first_name":name['first_name'],
                "last_name":name['last_name'],
                targetedField:word
            }
        else:
            return "Invalid record type"
        #see if any appropriate records exist    
        records=get_record_csv(queryDict,recordType)
        if type(records)!=str:
            return "VERIFIED"
    return "NO MATCH FOUND"
    
#print(verify_second_factor("AARON, ANDRE L","when I fart my dob is 07/22/1983","Date of Birth",'Warrants')) 
#print(verify_second_factor("AARON, ANDREz L","when I fart my dob is 07/22/1983","Date of Birth",'Warrants')) 
print(verify_second_factor({'first_name':'Mildred','last_name':'Collins'},"I usually poop in CHESTERFIELD","defendant_city",'citations'))         
        