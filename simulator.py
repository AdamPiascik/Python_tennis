import tennis

# Creates an empty list and populates it with players from the specified file #
all_players = []
tennis.addPlayersFromFile("players.txt", all_players)

# Lists all the players in the specified list, along with their attributes. #
# tennis.listPlayerStats(all_players)

# Choose two players for the simulation #
player1 = tennis.playerSearch("Andy Murray", all_players)
player2 = tennis.playerSearch("Roger Federer", all_players)

# Choose how many runs the simulation performs #
sim_repeats = 1000000

# Performs a point-playing simulation and stores the win rate of each player #
test_results = tennis.simulatePoints(player1, player2, sim_repeats)
player1_win_rate = 100 * test_results.count(player1.name) / sim_repeats
player2_win_rate = 100 * test_results.count(player2.name) / sim_repeats

# Print the results of the point-playing simulation. #
print("Out of {0} points played, {1} won {2:.2f}% and {3} won {4:.2f}%.".format(sim_repeats, player1.name, player1_win_rate, player2.name, player2_win_rate))

