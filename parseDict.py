# Assumes dict d of information about a citation is given
# Need to marry these functions with whichever keys are options
# This really just gives some of the basic logic for how to display the pulled data
# User input could be from a menu of numbers, validation will be taken care of by Twilio
# Something like...
# 0 Display all info
# 1 Court Address, inkey = "address"
# 2 Violation Description, inkey = "violation_description"
# 3 Citation Number, inkey = "citation_number"
# etc.

# Check that dict[key] value is not blank.
def notBlank(s):
	if(s == ''):
		return 'unavailable'
	else:
		return s

# Pass key and dict of info
# Modify according to options available to user
def printKey(key, d):
	if (key == 'hours'): # Modify for other options where key is plural
		print("Court %s are %s.", (key, notBlank(d[key])))
	elif (key in ['court', 'violation_description', 'violation_number']):
		print("Your %s is %s." % (key.replace('_', ' '), notBlank(d[key])))
	else:
		print("The %s is %s." %(key.replace('_', ' '), notBlank(d[key])))

# List of key names in the dict
# In actual implementation, list these in the order you want them displayed
keyList = dict.fromkeys(range(0, d.__len__()+1)) # change d.__len__() to number of options available to user
keyList[0] = 'all'
i = 1
for key in d.keys():
	keyList[i] = key
	i = i + 1
		
def getInfo(ind):
	# Initialize check for valid input
	if(keyList[ind] == 'all'):
		for i in range(1, d.__len__()+1): # Iterate through ordered list of keys
			printKey(keyList[i], d)
	else:
		printKey(keyList[ind], d)