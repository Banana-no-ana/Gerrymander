'''
Created on Oct 28, 2013
Voting area objects

@author: dan
'''
import xml.etree.ElementTree as ET

class VotingArea(object):
    '''
    classdocs
    '''
    def getCords(self, cords):
        myet =  ET.fromstring(cords)
        rawcords = myet.find('outerBoundaryIs').find('LinearRing').find('coordinates').text
        cords = rawcords.split(",0 ")
        cords[-1] = cords[-1][0:-2]
        return cords
    
    def parseInfo(self, info):
        infolist = info.split(",")[1:]
        self.EDName, self.winner, self.winnerVotes, self.runup, self.runupVotes = infolist
        self.runupVotes = self.runupVotes.rstrip()
    
    def parseLine(self, line):
        blank, coord, info =  line.split('"')
        self.coordinates = self.getCords(coord)
        self.parseInfo(info)
        
        #rawGeo, EDname, winner, winvotes, runup, runupvotes
        if 1 == 2 :
            raise FileStupidException("File is being stupid")
        
    def getEDName(self):
        return self.EDName
    
    def getaset(self, mylist):
        seen = set()
        for item in mylist:
            seen.add(item)
        return seen
    
    def confirmNeighbours(self):
        neighbours = self.potentialneighbours
        neighboursset = self.getaset(neighbours)
        for item in neighboursset:
            neighbours.remove(item)
        self.adjVAs = list(self.getaset(neighbours))
        self.potentialneighbours = []

    def __init__(self):
        '''
        Constructor
        '''
        self.coordinates = []
        self.EDName = ""
        self.winner = ""
        self.winnerVotes = 0
        self.runup = ""
        self.runupVotes = 0
        self.adjVAs = []
        self.adjEDs = []
        self.potentialneighbours = []
        self.VAnum = 0
        self.ED = ""
        
        
class FileStupidException(Exception):
    def __init__(self, message):
        Exception.__init__(self, message)