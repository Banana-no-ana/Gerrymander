'''
Created on Oct 28, 2013

@author: dan
'''

#Need 3 things: mapfn(), reducefn(), source, and final()
import pickle

picklefile = open('tmpfiles/VApickled', 'r')
returnFile = open('tmpfiles/cordpickled', 'w')

finishlist = []
myVAs = pickle.load(picklefile)
    
source = myVAs

def oldcode():
    newlist = []
    num = 1
    for VA in myVAs:
        newlist.append([num, VA])
        num = num +1
    source = dict(newlist)

def mapfn(key, value):
    #key is the number, this is tossaway
    #Value is the VA object
    for cord in value.coordinates:
        yield cord, key
        
def reducefn(VAcord, VA):
    #key is the coordinate, value are the VAs associated with it
    return VAcord, VA

def final2(key, value):
    #key is the coordinate, value are the VAs
    global returnFile
    myfile = open(returnFile, 'a')
    myfile.write(pickle.dumps(value) + "\n----------\n")
    myfile.close()

def final(cord, valist):
    global returnFile
    returnFile.write(pickle.dumps(valist) + "\n----------\n")