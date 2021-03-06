from tennisSys import MakeSystem
from tennisSim import InitialiseSimulation

def main():
    # Initialises a simulation system by generating player lists #
    sys = MakeSystem()

    # Print lists of players and their attributes from the system #
    # sys.printLists()
    # sys.listPlayerStats("male players")
    # print(sys.playerSearch("andy murray", "all players"))

    # Choose two players for the simulation from a specified player list #
    player2 = sys.getPlayer("Rafael Nadal", "All Players")
    player1 = sys.getPlayer("Roger Federer", "All Players")

    # Create the simulation environment if player genders match #
    if player1.gender == player2.gender:
        current_sim = InitialiseSimulation(player1, player2)
    else:
        print("Simulation creation failed: the genders of the specified players don't match.")
        return 1

    # Print various useful information about the current simulation #
    # current_sim.printPlayers()
    # current_sim.printType()
    # current_sim.printResults()

    # Performs a point-playing simulation and stores the win rate of each player #
    current_sim.resetSim()
    current_sim.runSimulation("points", 100000)
    # current_sim.runSimulation("games", 1000000)
    # current_sim.runSimulation("sets", 10000)
    # current_sim.runSimulation("matches", 10000)
    # print(current_sim.win_record)
    current_sim.printResults()
    return 0

if __name__ == '__main__':
    main()