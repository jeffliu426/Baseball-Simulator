from random import random
from bisect import bisect

class Batter: 
    
    def __init__(self, data):
        self.data = data
        row = data[0].split(",")
        self.pos = str(row[1])
        self.name = str(row[2])
        self.pa = int(row[5])
        self.ab = int(row[6])
        self.r = int(row[7])
        self.hits = int(row[8])
        self.doubles = int(row[9])
        self.triples = int(row[10])
        self.hr = int(row[11])
        self.rbi = int(row[12])
        self.sb = int(row[13])
        self.cs = int(row[14])
        self.bb = int(row[15])
        self.so = int(row[16])
    
    def getSingles(self):
        return (self.hits - self.doubles - self.triples - self.hr) 
    
    def getDoubles(self):
        return self.doubles 
    
    def getTriples(self):
        return self.triples 
    
    def getHr(self):
        return self.hr 
    
    def getBB(self):
        return self.bb 
    
    def getOut(self):
        return (self.pa - self.hits - self.bb) 
    
    def getStrikeOut(self):
        return self.so
    
    def weightedChoice(self, choices):
        values, weights = zip(*choices)
        total = 0
        cum_weights = []
        for w in weights:
            total += w
            cum_weights.append(total)
        x = random() * total
        i = bisect(cum_weights, x)
        return values[i]
        
    def createWeightedEvents(self):
        weightedEvents = []
        weightedEvents.append(("single", self.getSingles()))
        weightedEvents.append(("double", self.getDoubles()))
        weightedEvents.append(("triple", self.getTriples()))
        weightedEvents.append(("hr", self.getHr()))
        weightedEvents.append(("out", self.getOut()))
        weightedEvents.append(("bb", self.getBB()))
        return weightedEvents
    
    def getOutcomeOfPA(self):
        weightedEvents = self.createWeightedEvents()
        event = self.weightedChoice(weightedEvents)
        return event
        
    def getName(self):
        return self.name
    