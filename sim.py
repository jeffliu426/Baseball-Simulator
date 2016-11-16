import csv     # imports the csv module
import sys      # imports the sys module
from batter import *
from pitcher import *
from team import *
from baseballGame import *

def readFile(filename, playerType):
    f = open(filename, "r")
    lines = f.read().split("\n") # "\r\n" if needed
    listOfBatters = []
    listOfPitchers = []

    with open(filename, 'rb') as f:
        reader = csv.reader(f)
        data = list(reader)
    
    firstLine = True
    for line in data:
        if firstLine == True:
            firstLine = False
        else:
            if playerType == "hitter":
                batter = Batter(line)
                listOfBatters.append(batter)
            elif playerType == "pitcher":
                pitcher = Pitcher(line)
                listOfPitchers.append(pitcher)
    if playerType == "hitter":
        return listOfBatters
    return listOfPitchers       
    
       
def main():
    hitter = "hitter"
    pitcher = "pitcher"
    SFGiantsHitterData = readFile("SFGiantsHitters.csv", hitter)
    SFGiantsPitcherData = readFile("SFGiantsPitchers.csv", pitcher)
    LADodgersHitterData = readFile("LADodgersHitters.csv", hitter)
    LADodgersPitcherData = readFile("LADodgersPitchers.csv", pitcher)
    
    SFGiants = Team("SF Giants", SFGiantsHitterData, SFGiantsPitcherData)
    LADodgers = Team("LA Dodgers", LADodgersHitterData, LADodgersPitcherData)
    
    game = BaseballGame(SFGiants, LADodgers)
    SFGiantsWins = 0
    LADodgersWins = 0
    numMatchups = 100
    for i in range(0, numMatchups):
        winningTeam = game.playBall()
        if winningTeam == SFGiants:
            SFGiantsWins += 1
        else:
            LADodgersWins += 1
    print("The SF Giants won " + str((float(SFGiantsWins) / numMatchups) * 100) + "% of the time.")        
    
main()     


    
    
