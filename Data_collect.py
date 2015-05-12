'''
ask user for part number and cross reference against dictionary.
this file can use either json or pickle to save dictionaries. uncomment
the one that will be used and comment out or remove the other.
'''
from __future__ import with_statement
import json, stock
#import cPickle as pickle


#userPart = raw_input('Please enter a part number: ').upper()

# Take the user input and returns or stores the appropriate values
def live_or_die(user_part, parts):

    user_description = ""


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

#live_or_die(userPart, stock.main())
