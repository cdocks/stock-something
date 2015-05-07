from __future__ import with_statement
import json
#import cPickle as pickle

'''
main function for Stock management program. the function will grab/create a dictionary
and return it.
'''
def main():

    data_store = {}

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

    return data_store
if __name__ == '__main__':
    main()
