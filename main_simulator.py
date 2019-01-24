import tennisSys
import tennisSim

# Initialises a simulation system by generating player lists #
sys = tennisSys.MakeSystem()

# Print various useful lists from the system #
# sys.printLists()
# sys.listPlayerStats("All players")

# Choose two players for the simulation from a specified player list #
player1 = sys.getPlayer("Andy Murray", "All players")
player2 = sys.getPlayer("Roger Federer", "All players")

# Create the simulation environment #
current_sim = tennisSim.MakeSimulation(player1, player2)

# Print various useful information about the current simulation #
current_sim.printPlayers
current_sim.printResults

# Performs a point-playing simulation and stores the win rate of each player #
current_sim.simulatePoints(10000)
current_sim.printResults()