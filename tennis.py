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

class Player:  
    def __init__(self, name, skill_level):
        self.name = name
        self.skill = skill_level
    
    def stats(self):
        stats = {"Skill":self.skill}
        return stats
    
    def printProfile(self):
        print(self.name)
        player_stats = self.stats()
        for stat in player_stats:
            print("  ",stat, ":", player_stats[stat])

def simulatePoints(player1, player2, num_points):
    results = []
    for point in range(num_points):
        this_point = Point(player1, player2)
        this_point.play()
        results.append(this_point.result)
    return results

def listPlayerStats(all_players):
    print("\nHere are all the players in the specified list and their attributes:\n")
    for player in all_players:
        player.printProfile()

def playerSearch(name, list):
    for player in list:
        if player.name == name:
            break
    return player

def addPlayersFromFile(filename, list):
    list_file = open(filename, "r")
    for line in list_file:
        name, skill = line.split("\t")
        list.append(Player(name, float(skill)))
    list_file.close()