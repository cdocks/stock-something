'''
ask user for part number and cross reference against dictionary.
this file can use either json or pickle to save dictionaries. uncomment
the one that will be used and comment out or remove the other.
'''
from __future__ import with_statement
import json
#import cPickle as pickle

data_store = {}
userPart = raw_input('Please enter a part number: ').upper()

try:
    with open('jparts_data.json', 'r') as fh:
        data_store = json.load(fh)
except IOError:
    with open('jparts_data.json', 'w') as fh:
        json.dump(data_store, fh)

'''
try:
    with open('parts_data.txt', 'rb') as fh:
        data_store = pickle.load(fh)
        print(data_store)
except IOError:
    with open('parts_data.txt', 'wb') as fh:
        pickle.dump(data_store, fh, 0)
'''

# Take the user input and returns or stores the appropriate values
def live_or_die(user_part, parts):
    user_description =""

    print(parts)

    if parts == {}:
        user_description = raw_input('Please enter a description: ')
        parts[user_part] = parts.get(user_part, (user_description, 0,))
    else:
        user_description = raw_input('Please enter a description: ')
        parts[user_part] = parts.get(user_part, (user_description, 0,))
    with open('jparts_data.json', 'w') as fh:
        json.dump(parts, fh)
    print(parts)
    #for key in partDict:

live_or_die(userPart, data_store)
