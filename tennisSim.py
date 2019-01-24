from random import random

class InitialiseSimulation:
    def __init__(self, player1, player2):
        self.player1 = player1
        self.player2 = player2
        self.type = "Not yet specified"
        self.repeats = "Not yet specified"
        self.run_yet = False
        self.win_record = {"points":[0, 0], "sets":[0, 0], "games":[0, 0], "matches":[0, 0]}
        self.win_rate_record = {"points":[0, 0], "sets":[0, 0], "games":[0, 0], "matches":[0, 0]}
    
    def printType(self):
        print("The current simulation is for", self.type)

    def printPlayers(self):
        print("The players in the current simulation are {0} and {1}.".format(self.player1, self.player2))

    def printResults(self):
        if self.run_yet:
            print("\n {0} {1} were simulated. Here are the results:".format(self.repeats, self.type))
            print("\t{0} won {1} {2} ({3:.1%} win rate)".format(self.player1, self.win_record[self.type][0], self.type, self.win_rate_record[self.type][0]))
            print("\t{0} won {1} {2} ({3:.1%} win rate)".format(self.player2, self.win_record[self.type][1], self.type, self.win_rate_record[self.type][1]))          
        else:
            print("The current simulation hasn't been run yet.")

    def resetSim(self):
        self.type = "Not yet specified"
        self.repeats = "Not yet specified"
        self.run_yet = False
        self.win_record = {"points":[0, 0], "sets":[0, 0], "games":[0, 0], "matches":[0, 0]}
        self.win_rate_record = {"points":[0, 0], "sets":[0, 0], "games":[0, 0], "matches":[0, 0]}

    def runSimulation(self, type, repeats):
        self.repeats = repeats
        if type == "points":
            self.type = "points"
            for i in range(repeats):
                self.playPoint()
        elif type == "sets":
            self.type = "sets"
            for i in range(repeats):
                self.playSet()
        elif type == "games":
            self.type = "games"
            for i in range(repeats):
                self.playGame()
        elif type == "matches":
            self.type = "matches"
            for i in range(repeats):
                self.playMatch()
        else:
            print("Simulation type not defined.")
        self.run_yet = True
        self.updateWinRates()

    def playPoint(self):
        while (True):
            if random() > self.player1.skill:
                self.win_record["points"][1] += 1
                return self.player2
                break
            if random() > self.player2.skill:
                self.win_record["points"][0] += 1
                return self.player1
                break
    
    def playSet(self):
        player1points = 0
        player2points = 0
        set_winner = "None"
        set_ongoing = True
        while set_ongoing:
            # print("\nScore:\n\t{0}: {1}\t{2}: {3}".format(self.player1, player1points, self.player2, player2points))
            point_winner = self.playPoint()
            if point_winner == self.player1:
                if player1points == 45:
                    if player2points == 45:
                        player1points = "AD"
                    elif player2points =="AD":
                        player2points = 45
                elif player1points == "AD":
                    player1points = 60
                else:
                    player1points += 15

            elif point_winner == self.player2:
                if player2points == 45:
                    if player1points == 45:
                        player2points = "AD"
                    elif player1points =="AD":
                        player1points = 45
                elif player2points == "AD":
                    player2points = 60
                else:
                    player2points += 15

            if player1points == 60:
                set_winner = self.player1
                self.win_record["sets"][0] += 1
                set_ongoing = False
            elif player2points == 60:
                set_winner = self.player2
                self.win_record["sets"][1] += 1
                set_ongoing = False
        return 

    def updateWinRates(self):
        if self.type != "Not yet specifed":
            self.win_rate_record[self.type] = [self.win_record[self.type][0] / self.repeats, self.win_record[self.type][1] / self.repeats]
        else:
            print("Can't update win rates because simulation hasn't been run yet.")