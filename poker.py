import poker

class Player:
    chipcount = 0
    cards = []
    def __init__(self, startingChipCount):
        self.chipcount = startingChipCount
    def setHand(self, card1, card2):
        self.cards = [card1, card2]
    def resetHand(self):
        self.cards = []

def setblinds(first, numPlayer,bigB,smallB,dealer):
    if numPlayer > 2:
        smallB = 0
        bigB = 1


def play(numPlayer, startingChipCount):
    continueGame = True
    players = []
    for x in range(numPlayer):
        tempPlayer = Player(startingChipCount)
        players.append(tempPlayer)
    #set which players are big,small blind and dealer
    bigb,smallB,dealer
    first = True
    setblinds(first, numPlayer,bigB,smallB,dealer)
    #while game is being played
    while continueGame:
        first = False
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
        continueGame = checkGame()

def run():
    #get number of players
    numPlayers = int(input("Number of players:"))
    startingChipCount = int(input("Buy in:"))
    #play game
    play(numPlayers, startingChipCount)
if __name__ == "__main__":
    run()



