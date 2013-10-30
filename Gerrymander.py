'''
Created on Oct 28, 2013

@author: dan
'''

import sys
import VotingArea
from VotingArea import FileStupidException
import copy
import pickle
import octo
import ElectoralDistrict

LISTOFVAs = []
strLISTOFVAs = {}
DICTOFEDs = {}

#which coordinates are associated with which VAs
CordDict = {}

#Take a csv file, and parse through it. 
def importData():
    global listofVAs
    myfile = open(sys.argv[1])
    #get rid of the firstline
    myfile.readline()
    for line in myfile:
            #create a VA
            myVA =  VotingArea.VotingArea()
            try:
                myVA.parseLine(line)
            except FileStupidException:
                print "Skipping a line, file's being stupid"
            else:
                LISTOFVAs.append(myVA)
    #now all the VAs are created. should now try to calc the neighbours of all the VAs
    #any VAs that share more than 1 coordinate is a neighbour


def pickleVAs():
    global LISTOFVAs
    print "Pickling all the VAs to file: VApickled"
    pickleFile = open('tmpfiles/VApickled', 'w')
    VADict = {}
    for VA in LISTOFVAs:
        VADict[str(VA)] = VA
    pickle.dump(VADict, pickleFile)
    print "list of VAs are dumped. now try to make a dictionary of all the coordinates"
    
def runOcto():
    #temporarily change sys.argv
    print "starting server to build cord dictionary"
    tempargv = copy.deepcopy(sys.argv)
    sys.argv = ["octo.py", "server", "coordDictBuilder.py"]
    octo.main()
    sys.argv = tempargv
    print "Dictionary is built to file: tmpfiles/cordpickled"
    
def convertBack(listVA):
    global LISTOFVAs, strLISTOFVAs
    for VA in LISTOFVAs:
        strLISTOFVAs[str(VA)] = VA
    mylist = []
    for VA in listVA:
        mylist.append(strLISTOFVAs[VA])
    return mylist

def buildCordDict():
    myfile = open('tmpfiles/cordpickled','r')
    rawfile = myfile.read()
    filelist = rawfile.split("\n----------\n")
    cDict = {}
    for item in filelist:
        try:
            thing = pickle.loads(item)
            (coord, VAs) = thing
            VAinObject = convertBack(VAs)            
            cDict[coord] = VAinObject
        except (EOFError, ValueError) as e:
            print e.message
            pass
    global CordDict
    CordDict = cDict
    
def findNeighbours():
    #potentialneighbours is a thing
    global CordDict
    for cord in CordDict.keys():
        listofVAs = CordDict[cord]
        if len(listofVAs) > 1:
            for VA in listofVAs:
                try:
                    pos = listofVAs.index(VA)
                    neighbours = copy.copy(listofVAs)
                    neighbours.pop(pos)
                    VA.potentialneighbours += neighbours
                    
                except ValueError:
                    print "Can't remove something, why????"
                    print VA, listofVAs
                    
    for VA in LISTOFVAs:
        VA.confirmNeighbours()
    
def testShit():
    print "Printing list of VAs, there should be 10"
    for ED in DICTOFEDs.keys():
        myED = DICTOFEDs[ED]
        print myED.name, myED.VAs
        for VA in myED.VAs:
            print VA.adjVAs
        
def buildEDs():
    global LISTOFEDs
    for VA in LISTOFVAs:
        if VA.EDName not in DICTOFEDs.keys():
            ED = ElectoralDistrict.ElectoralDistrict()
            ED.name = VA.EDName
            DICTOFEDs[VA.EDName] = ED
        myED = DICTOFEDs[VA.EDName]
        myED.VAs.append(VA)
        VA.ED = myED

def main():
    #This is the gerry mandering project
    #To get started, we should definitely import the data first. 
    importData()    
    pickleVAs()
    runOcto() #Octo does the mapreduce algorithm, may have to the neighbour calculation with mapreduce too
    buildCordDict()
    findNeighbours()
    buildEDs()
    testShit()
    

if __name__ == '__main__':
    main()