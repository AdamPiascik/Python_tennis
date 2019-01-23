import tennis

all_players = [tennis.Player("Andy Murray", 0.8), tennis.Player("Jamie Murray", 0.7)]

tennis.listPlayerStats(all_players)

def playerSearch(name, list):
        for player in list:
                if player.name == name:
                        break
        return player

player1 = playerSearch("Andy Murray", all_players)
player2 = playerSearch("Jamie Murray", all_players)

sim_repeats = 10000
test_results = tennis.simulatePoints(player1, player2, sim_repeats)
player1_win_rate = 100 * test_results.count(player1.name) / sim_repeats
player2_win_rate = 100 * test_results.count(player2.name) / sim_repeats
print("Out of {0} points played, {1} won {2:.2f}% and {3} won {4:.2f}%.".format(sim_repeats, player1.name, player1_win_rate, player2.name, player2_win_rate))

