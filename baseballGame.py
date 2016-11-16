class BaseballGame:
    
    
    def __init__(self, homeTeam, awayTeam):
        self.homeTeam = homeTeam
        self.awayTeam = awayTeam
        self.inning = 1
        self.topOfTheInning = True
        self.numOuts = 0
        self.numRunsForHomeTeam = 0
        self.numRunsForAwayTeam = 0
        self.runnerOnFirst = False
        self.runnerOnSecond = False
        self.runnerOnThird = False
        self.spotInOrderForHomeTeam = 0
        self.spotInOrderForAwayTeam = 0
        
    def resetGame(self):
        self.inning = 1
        self.topOfTheInning = True
        self.numOuts = 0
        self.numRunsForHomeTeam = 0
        self.numRunsForAwayTeam = 0
        self.runnerOnFirst = False
        self.runnerOnSecond = False
        self.runnerOnThird = False
        self.spotInOrderForHomeTeam = 0
        self.spotInOrderForAwayTeam = 0
    
    def playBall(self):
        self.resetGame()
        while self.inning <= 9:
            while self.topOfTheInning:
                self.playTopHalfOfInning()   
            if self.inning == 9 and self.numRunsForHomeTeam > self.numRunsForAwayTeam:
                self.printFinalScore()
                return self.homeTeam
            while not self.topOfTheInning:
                self.playBottomHalfOfInning()
            self.inning += 1
        if(self.numRunsForAwayTeam == self.numRunsForHomeTeam):
            self.playExtras()    
        self.printFinalScore()
        if(self.numRunsForAwayTeam > self.numRunsForHomeTeam):
            return self.awayTeam
        return self.homeTeam
    
    def playExtras(self):
        tied = True
        while tied:
            while self.topOfTheInning:
                self.playTopHalfOfInning()    
            while not self.topOfTheInning:
                self.playBottomHalfOfInning()
                self.inning += 1
                if(self.numRunsForAwayTeam != self.numRunsForHomeTeam):
                    tied = False
                    
    
    def playTopHalfOfInning(self):
        batter = self.awayTeam.getBatter(self.spotInOrderForAwayTeam)
        event = batter.getOutcomeOfPA()
        if(self.spotInOrderForAwayTeam == 8):
            self.spotInOrderForAwayTeam = 0
            self.update(event, self.awayTeam)
        else:
            self.spotInOrderForAwayTeam += 1
            self.update(event, self.awayTeam)
            
    def playBottomHalfOfInning(self):
        batter = self.homeTeam.getBatter(self.spotInOrderForHomeTeam)
        event = batter.getOutcomeOfPA()
        if(self.spotInOrderForHomeTeam == 8):
            self.spotInOrderForHomeTeam = 0
            self.update(event, self.homeTeam)
        else:
            self.spotInOrderForHomeTeam += 1
            self.update(event, self.homeTeam)
    
    def updateBasesIfSingle(self, team):
        if self.runnerOnSecond and self.runnerOnThird and self.runnerOnFirst:
            if team == self.homeTeam:
                self.numRunsForHomeTeam += 1
            else:
                self.numRunsForAwayTeam += 1
        elif self.runnerOnFirst and self.runnerOnSecond:
            self.runnerOnThird = True
        elif self.runnerOnFirst and self.runnerOnThird:
            self.runnerOnSecond = True
        elif self.runnerOnFirst:
            self.runnerOnSecond = True   
        else:
            self.runnerOnFirst = True
            
    def printFinalScore(self):
        awayTeamName = str(self.awayTeam.getName())
        homeTeamName = str(self.homeTeam.getName())
        homeScore = str(self.numRunsForHomeTeam)
        awayScore = str(self.numRunsForAwayTeam)
        
        if(self.numRunsForAwayTeam > self.numRunsForHomeTeam):
            print("The " + awayTeamName + " beat the " + homeTeamName + " by a score of " +
                  awayScore + " to " + homeScore + " in " + str(self.inning - 1) + " innings.")
        elif(self.numRunsForAwayTeam < self.numRunsForHomeTeam):
            print("The " + homeTeamName + " beat the " + awayTeamName + " by a score of " + 
                  homeScore + " to " + awayScore + " in " + str(self.inning - 1) + " innings.")

    
    def updateBasesIfDouble(self, team):
        if self.runnerOnFirst and self.runnerOnSecond and self.runnerOnThird:
            self.runnerOnFirst = False
            if team == self.homeTeam:
                self.numRunsForHomeTeam += 2
            else:
                self.numRunsForAwayTeam += 2
        elif self.runnerOnFirst and self.runnerOnSecond:
            self.runnerOnFirst = False
            self.runnerOnThird = True
            if team == self.homeTeam:
                self.numRunsForHomeTeam += 1
            else:
                self.numRunsForAwayTeam += 1
        elif self.runnerOnFirst and self.runnerOnThird:
            self.runnerOnFirst = False
            self.runnerOnSecond = True
            if team == self.homeTeam:
                self.numRunsForHomeTeam += 1
            else:
                self.numRunsForAwayTeam += 1
        elif self.runnerOnSecond and self.runnerOnThird:
            self.runnerOnThird = False
            if team == self.homeTeam:
                self.numRunsForHomeTeam += 2
            else:
                self.numRunsForAwayTeam += 2
        elif self.runnerOnFirst:
            self.runnerOnFirst = False
            self.runnerOnSecond = True
            self.runnerOnThird = True
        elif self.runnerOnSecond:
            if team == self.homeTeam:
                self.numRunsForHomeTeam += 1
            else:
                self.numRunsForAwayTeam += 1
        elif self.runnerOnThird:
            self.runnerOnThird = False
            self.runnerOnSecond = True
            if team == self.homeTeam:
                self.numRunsForHomeTeam += 1
            else:
                self.numRunsForAwayTeam += 1
        else:
            self.runnerOnSecond = True
            
    def updateBasesIfTriple(self, team):
        if self.runnerOnFirst and self.runnerOnSecond and self.runnerOnThird:
            self.runnerOnFirst = False
            self.runnerOnSecond = False
            if team == self.homeTeam:
                self.numRunsForHomeTeam += 3
            else:
                self.numRunsForAwayTeam += 3
        elif self.runnerOnFirst and self.runnerOnSecond:
            self.runnerOnFirst = False
            self.runnerOnSecond = False
            if team == self.homeTeam:
                self.numRunsForHomeTeam += 2
            else:
                self.numRunsForAwayTeam += 2
        elif self.runnerOnFirst and self.runnerOnThird:
            self.runnerOnFirst = False
            if team == self.homeTeam:
                self.numRunsForHomeTeam += 2
            else:
                self.numRunsForAwayTeam += 2
        elif self.runnerOnSecond and self.runnerOnThird:
            self.runnerOnSecond = False
            if team == self.homeTeam:
                self.numRunsForHomeTeam += 2
            else:
                self.numRunsForAwayTeam += 2
        elif self.runnerOnFirst:
            self.runnerOnFirst = False
            self.runnerOnThird = True
            if team == self.homeTeam:
                self.numRunsForHomeTeam += 1
            else:
                self.numRunsForAwayTeam += 1
        elif self.runnerOnSecond:
            self.runnerOnSecond = False
            self.runnerOnThird = True
            if team == self.homeTeam:
                self.numRunsForHomeTeam += 1
            else:
                self.numRunsForAwayTeam += 1
        elif self.runnerOnThird:
            if team == self.homeTeam:
                self.numRunsForHomeTeam += 1
            else:
                self.numRunsForAwayTeam += 1
        else:
            self.runnerOnThird = True
            
    def updateBasesIfHr(self, team):
        if self.runnerOnFirst and self.runnerOnSecond and self.runnerOnThird:
            self.runnerOnFirst = False
            self.runnerOnSecond = False
            self.runnerOnThird = False
            if team == self.homeTeam:
                self.numRunsForHomeTeam += 4
            else:
                self.numRunsForAwayTeam += 4
        elif self.runnerOnFirst and self.runnerOnSecond:
            self.runnerOnFirst = False
            self.runnerOnSecond = False
            if team == self.homeTeam:
                self.numRunsForHomeTeam += 3
            else:
                self.numRunsForAwayTeam += 3
        elif self.runnerOnFirst and self.runnerOnThird:
            self.runnerOnFirst = False
            self.runnerOnThird = False
            if team == self.homeTeam:
                self.numRunsForHomeTeam += 3
            else:
                self.numRunsForAwayTeam += 3
        elif self.runnerOnSecond and self.runnerOnThird:
            self.runnerOnSecond = False
            self.runnerOnThird = False
            if team == self.homeTeam:
                self.numRunsForHomeTeam += 3
            else:
                self.numRunsForAwayTeam += 3
        elif self.runnerOnFirst:
            self.runnerOnFirst = False
            if team == self.homeTeam:
                self.numRunsForHomeTeam += 2
            else:
                self.numRunsForAwayTeam += 2
        elif self.runnerOnSecond:
            self.runnerOnSecond = False
            if team == self.homeTeam:
                self.numRunsForHomeTeam += 2
            else:
                self.numRunsForAwayTeam += 2
        elif self.runnerOnThird:
            self.runnerOnThird = False
            if team == self.homeTeam:
                self.numRunsForHomeTeam += 2
            else:
                self.numRunsForAwayTeam += 2
        else:
            if team == self.homeTeam:
                self.numRunsForHomeTeam += 1
            else:
                self.numRunsForAwayTeam += 1
            
    def updateBasesIfBB(self, team):
        if self.runnerOnFirst and self.runnerOnSecond and self.runnerOnThird:
            self.numRunsForAwayTeam += 1
        elif self.runnerOnFirst and self.runnerOnSecond:
            self.runnerOnThird = True
        elif self.runnerOnFirst and self.runnerOnThird:
            self.runnerOnSecond = True
        elif self.runnerOnFirst:
            self.runnerOnSecond = True   
        else:
            self.runnerOnFirst = True
    
    def update(self, event, team):
        if(event == "out"):
            self.numOuts += 1
            if self.numOuts == 3:
                self.runnerOnFirst = False
                self.runnerOnSecond = False
                self.runnerOnThird = False
                self.numOuts = 0
                if team == self.awayTeam:
                    self.topOfTheInning = False
                elif team == self.homeTeam:
                    self.topOfTheInning = True
        elif(event == "single"):
            self.updateBasesIfSingle(team)
        elif(event == "double"):
            self.updateBasesIfDouble(team)
        elif(event == "triple"):
            self.updateBasesIfTriple(team)
        elif(event == "hr"):
            self.updateBasesIfHr(team)
        elif(event == "bb"):
            self.updateBasesIfBB(team)
        