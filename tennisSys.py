# This is the class of fundamental objects for creating a new simulation. It
# contains lists of Player objects, categorised in different ways, from which
# players for a simulation can be selected.
class MakeSystem:
        # This creates a new system for simulations and initialise player lists
        # as a dictionary with format: {"List Name":[Player, Player, Player...]}.
        # Player is a Player object
        def __init__(self):
                self.player_lists = {}
                self.addAllPlayersFromFile()
                self.makeGenderLists()

        # This prints the names of all available player lists, each on it's
        # own line.
        def printLists(self):
                print("The available player lists are:")
                for list in self.player_lists:
                        print("\t{0}".format(list))

        # This prints the names and attributes of all players in a given list.
        def listPlayerStats(self, list_name):
                print("\nHere are all the players listed in '{0}' along with their attributes:\n".format(list_name.title()))
                if list_name.title() == "Male Players" or list_name.title() == "Female Players":
                        for player in self.player_lists[list_name.title()]:
                                player.printProfile(skip="gender")
                else:
                        for player in self.player_lists[list_name.title()]:
                                player.printProfile()
        
        # This searches a player list (using the playerSearch function) for the
        # name of a player. If found, it returns the player as a Player object.
        # If not found, it prints a message.
        def getPlayer(self, name, list):
                if self.playerSearch(name, list):
                        for player in self.player_lists[list.title()]:
                                if player.name == name:
                                        return player
                else:
                        print("That player isn't listed in", list)

        # This searches a player list for the name of a player. If found, it
        # returns True; if not, False.
        def playerSearch(self, searched_name, list):
                player_in_list = False
                for player in self.player_lists[list.title()]:
                        if player.name.lower() == searched_name.lower():
                                player_in_list = True
                                break
                return player_in_list

        # Creates and populates a player list called "All Players", based on
        # entries in a text file. The function expects a CSV file with one entry
        # per line.
        def addAllPlayersFromFile(self):
                self.player_lists["All Players"] = []
                players_file = open("players.txt", "r")
                for line in players_file:
                        name, gender, skill = line.split(",")
                        self.player_lists["All Players"].append(Player(name, gender, float(skill)))
                players_file.close()

        # Creates and populates two lists for male and female players, based on
        # entries in the "All Players" list.
        def makeGenderLists(self):
                self.player_lists["Male Players"] = []
                self.player_lists["Female Players"] = []
                for player in self.player_lists["All Players"]:
                        if player.gender == "Male":
                                self.player_lists["Male Players"].append(player)
                        elif player.gender == "Female":
                                self.player_lists["Female Players"].append(player)                                

# This is the class for creating Player objects. It has methods for printing
# information about each player.
class Player:  
        # Creates a new Player object and initialises it with some attributes.
        def __init__(self, name, gender, skill):
                self.name = name
                self.gender = gender 
                self.skill = skill
        # Changes how the Player object is displayed if printed.
        def __repr__(self):
                return self.name
    
        # Creates a dictionary of player attributes
        def stats(self):
                stats = {"Gender":self.gender, "Skill":self.skill}
                return stats

        # Prints a list of all player attributes
        def printProfile(self, skip="none"):
                print(self.name)
                player_stats = self.stats()                
                if skip == "gender":
                        for stat in player_stats:
                                if stat != "Gender":
                                        print("  ",stat, ":", player_stats[stat])
                else:
                        for stat in player_stats:
                                print("  ",stat, ":", player_stats[stat])