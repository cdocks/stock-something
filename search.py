"""
this def is to find the requested part and return it.
"""

import stock
import Data_collect

userRequest = raw_input("Which part did you need? ").upper()

def findPart(part, partsList):

    parts = partsList
    if parts == {}:
        print "Please import or add parts to the inventory"
        addornot = raw_input("Would you like to add this part? yes or no. ").lower()
        print addornot
        while addornot != "yes" or addornot != "no":
            addornot = raw_input("Please only choose yes or no. ").lower()
            if addornot == "yes":
                Data_collect.live_or_die(userRequest, parts)
                break
            else:
                return
    # need to add a counter and a while statement to allow the whole list to be searched
    for key in parts:
        if key == part:
            return key + parts[key]
        else:
            addornot = raw_input("Part not in stock. Would you like to add it? yes or no. ").lower()
            while addornot != "yes" or addornot != "no":
                addornot = raw_input("Please only choose yes or no. ").lower()
                if addornot == "yes":
                    return Data_collect.live_or_die(userRequest, parts)
                else:
                    return



findPart(userRequest, stock.main())