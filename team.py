from batter import *

class Team:
    
    def __init__(self, name, batterData, pitcherData):
        self.name = name
        self.battingOrder = []
        
        for index in range(0, 9):
            self.battingOrder.append(batterData[index])
            
        self.startingPitcher = pitcherData[0]
            
    def getName(self):
        return self.name
    
    def getBatter(self, spotInOrder):
        return self.battingOrder[spotInOrder]