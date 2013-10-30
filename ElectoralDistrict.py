'''
Created on Oct 29, 2013

@author: root
'''

class ElectoralDistrict(object):
    '''
    classdocs
    '''
    def calcCords(self):
        pass
    
    def calcNeighbours(self):
        #Use the existing set of VAs
        pass
    
    def calcWinner(self):
        #Aggregate all the VA's data and return parties, counts, and diff
        pass

    def __init__(self):
        '''
        Constructor
        '''
        self.name = ""
        self.VAs = []
        self.coordinates = []
        self.neighbours = []
        self.winparty = ""
        self.wincount = 0
        self.runup = ""
        self.runupCount = 0
        self.countDiff = 0
        