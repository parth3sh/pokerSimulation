import poker

def dealCards(deck):
    return 0
def run():
    #get number of players
    numPlayers = input("Number of players:")
    #play game
    play(numPlayers)

def play(numPlayer):
    continueGame = True
    #while game is being played
    while continueGame:
        #take blind bets
        blindBets()
        #deal 2 cards to each player
        dealCards(deck)
        #preflop betting round
        preflopBets()
        #flop
        flop()
        flopBets()
        #turn
        turnbets()
        #river
        riverbets()
        #showdown
        showdown()
        #deal another hand?
        checkGame()

if __name__ == "__main__":
    run()



