class MakeSystem:
        def __init__(self):
                self.player_lists = {}
                self.addAllPlayersFromFile()

        def printLists(self):
                print("The available player lists are:")
                for list in self.player_lists:
                        print("\t{0}".format(list))

        def listPlayerStats(self, list):
                print("\nHere are all the players in the specified list and their attributes:\n")
                for player in self.player_lists[list]:
                        player.printProfile()
        
        def getPlayer(self, name, list):
                if self.playerSearch(name, list):
                        for player in self.player_lists[list]:
                                if player.name == name:
                                        return player
                else:
                        print("That player isn't listed in", list)

        def playerSearch(self, searched_name, list):
                player_in_list = False
                for player in self.player_lists[list]:
                        if player.name == searched_name:
                                player_in_list = True
                                break
                return player_in_list

        def addAllPlayersFromFile(self):
                self.player_lists.update({"All players": []})
                players_file = open("players.txt", "r")
                for line in players_file:
                        name, gender, skill = line.split(",")
                        self.player_lists["All players"].append(Player(name, gender, float(skill)))
                players_file.close()

class Player:  
        def __init__(self, name, gender, skill_level):
                self.name = name
                self.gender = gender 
                self.skill = skill_level
        
        def __repr__(self):
                return self.name
    
        def stats(self):
                stats = {"Gender":self.gender, "Skill":self.skill}
                return stats
    
        def printProfile(self):
                print(self.name)
                player_stats = self.stats()
                for stat in player_stats:
                        print("  ",stat, ":", player_stats[stat])