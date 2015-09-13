# Assumes dict d of information about found citations is given
# Need to marry these functions with whichever keys are options
# This really just gives some of the basic logic for how to display the pulled data

# Sample inputs
# d = {'citations': [{'citation_date': '2015-03-09', 'citation_number': 789674515, 'last_name': 'Phillips', 'violations': [{'violation_number': 123455, 'violation_description': 'public intoxication'}, {'violation_number': 333333, 'violation_description': 'indecent exposure'}], 'court_location': 'COUNTRY CLUB HILLS', 'court_address': '7422 Eunice Avenue', 'court_date': '2015-11-06', 'first_name': 'Wanda'}, {'citation_date': '2015-09-16', 'citation_number': 513276502, 'court_date': '2016-01-03', 'violations': [{'violation_number': 343343, 'violation_description': 'trespassing'}], 'court_location': 'FLORISSANT', 'court_address': '315 Howdershell Road', 'first_name': 'William', 'last_name': 'Ferrell'}]}
# c = {'court_location': 'COUNTRY CLUB HILLS', 'court_address': '7422 Eunice Avenue', 'phone': '314-555-5555'}
# w = {'warrants': [{'warrant_number': '12345678-A', 'zip_code': '63139'}, {'warrant_number': '98765432-X', 'zip_code': '63101'}]}


# Function checks that dict[key] value is not blank.
def notBlank(s):
	if(s == ''):
		return 'unavailable'
	else:
		return s

# Pass key and dict of info
# Modify according to options available to user
def printKey(key, d):
	if (key in ['court_date', 'court_location', 'violation_description', 'violation_number']):
		print("Your %s is %s." % (key.replace('_', ' '), notBlank(d[key])))
	elif (key == 'phone'):
		print("The phone number is %s." % d[key])
	else:
		print("The %s is %s." %(key.replace('_', ' '), notBlank(d[key])))
		
# Ticket Lookup modeled after web interface
# Assumes match was found and dict d returned has all citation info
def listCitations(d):
	print("%d citation(s) found" % len(d['citations']))
	# Print numbered list of citations found
	for i in range(0, len(d['citations'])):
		t = d['citations'][i] # Go through list of citations
		print("%d: Cit# %d on %s to %s %s" % (i, t['citation_number'], t['citation_date'], t['first_name'], t['last_name']) )
	
# Get more info on chosen citation indCit = 0, 1, ...
# Pass it an index (selected by user) and the dict of citations
# e.g. getCitation(0, d)
def getCitation(indCit, d):
	keyList = ['court_date', 'court_location', 'court_address']
	#indCit = index of citation returned by user
	# Have not married citations with violations yet
	t = d['citations'][indCit] # Selected citation
	print("Citation # %d for %d violations" % (t['citation_number'], len(t['violations'])) )
	for i in range(0, len(keyList)):
		printKey(keyList[i], t)
	#Prompt user for violations?


# Get list of violations and descriptions
# Function is passed a list of violations v = d['citations'][indCit]['violations'] attached to user's chosen citation
def getViolations(v):
	for i in range(0, len(v)):
		print('Violation %d: %d' % (i+1, v[i]['violation_number']))
		print('For: %s \n' % v[i]['violation_description'])

# Court Lookup modeled after web interface
# Assumes court was found and dict d returned has all court 
# e.g. courtLookup(c)
# c defined at top of file
def courtLookup(d):
	# For Court Lookup
	keyList = ['court_location', 'court_address', 'phone']
	# For the given address the ticket was issued
	# d is now a dict of court information for address lookup of ticket
	for i in range(0, len(keyList)):
		printKey(keyList[i], d)
		
# Ticket Lookup modeled after web interface
# Assumes match was found and dict w returned has all warrant info
def getWarrants(w):
	print("%d warrant(s) found" % len(w['warrants']))
	# Print numbered list of citations found
	for i in range(0, len(w['warrants'])):
		t = w['warrants'][i] # Go through list of citations
		print("%d: Warrant Case # %s for ticket issued in %s" % (i, t['warrant_number'], t['zip_code']) )