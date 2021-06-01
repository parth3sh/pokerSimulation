from poker import Card



class Player:
    chipcount = 0
    cards = []
    def __init__(self, startingChipCount):
        self.chipcount = startingChipCount
    def setHand(self, card1, card2):
        self.cards = [card1, card2]
    def resetHand(self):
        self.cards = []


def setblinds(first, numPlayer, blindsArr):
    if numPlayer > 2:
        if first:
            blindsArr[2] = 2
            blindsArr[1] = 1
            blindsArr[0] = 0
        else:
            if bigB + 1 > numPlayer - 1:
                blindsArr[0] = blindsArr[1]
                blindsArr[1] = blindsArr[2]
                blindsArr[2] = 0 
            else:
                blindsArr[0] = blindsArr[1]
                blindsArr[1] = blindsArr[2]
                blindsArr[2] = blindsArr[2] + 1
    else:
        if first:
            blindsArr[0] = 0
            blindsArr[1] = 0
            blindsArr[2] = 1
        else:
            blindsArr[1] = blindsArr[2]
            blindsArr[2] = blindsArr[0]
            blindsArr[0] = blindsArr[1]
    return blindsArr
def play(numPlayer, startingChipCount):
    continueGame = True
    players = []
    for x in range(numPlayer):
        tempPlayer = Player(startingChipCount)
        players.append(tempPlayer)
    #set which players are big,small blind and dealer
    first = True
    blindsArr = [0,0,0]
    blindsArr = setblinds(first,numPlayer, blindsArr)
    first = False
    smallBAmt = input("Small blind amount:") 
    bibBAmt = input("Big blind amount:") 

    #while game is being played
    while continueGame:
        pot = 0        
        #take blind bets
        pot = smallBAmt + bigBAmt
        players[blindsArr[1]].chipcount = players[blindsArr[1]].chipcount - smallBAmt
        players[blindsArr[2]].chipcount = players[blindsArr[2]].chipcount - bigBAmt
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



