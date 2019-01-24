from random import random

class Point:
    def __init__(self, player1, player2):
        self.players = (player1, player2)
        self.result = "Not yet played"

    def play(self):
        volley_counter = 0
        while (True):
            if random() > self.players[0].skill:
                winner = self.players[1]
                break
            volley_counter += 1
            if random() > self.players[1].skill:
                winner = self.players[0]
                break
            volley_counter += 1
        self.result = winner.name

    def printPlayers(self):
        print(self.players[0], self.players[1])

class MakeSimulation:
    def __init__(self, player1, player2):
        self.player1 = player1
        self.player2 = player2
        self.type = "Not yet specified"
        self.wins = [0, 0]
        self.repeats = "Not yet specified"
        self.winRates = [0, 0]

    def updateWinRate(self):
        self.winRates = [self.wins[0] / self.repeats, self.wins[1] / self.repeats]

    def simulatePoints(self, repeats):
        self.type = "points"
        self.repeats = repeats
        for i in range(repeats):
            while (True):
                if random() > self.player1.skill:
                    self.wins[1] += 1
                    break
                if random() > self.player2.skill:
                    self.wins[0] += 1
                    break
        self.updateWinRate()

    def printResults(self):
            print("\n {0} {1} were simulated. Here are the results:".format(self.repeats, self.type))
            print("\t{0} won {1} {2} ({3:.2%} win rate)".format(self.player1.name, self.wins[0], self.type, self.winRates[0]))
            print("\t{0} won {1} {2} ({3:.2%} win rate)".format(self.player2.name, self.wins[1], self.type, self.winRates[1]))

    def resetScores(self):
        self.wins = [0, 0]

    def printPlayers(self):
        print(self.players[0], self.players[1])