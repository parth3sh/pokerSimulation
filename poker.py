import treys
from treys import Deck
from treys import Card
import random


class Player:
    chipcount = 0
    hand = None
    def __init__(self, startingChipCount):
        self.chipcount = startingChipCount
    def setHand(self, hand):
        self.hand = hand
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
    smallBAmt = int(input("Small blind amount:"))
    bigBAmt = int(input("Big blind amount:"))

    #while game is being played
    while continueGame:
        #load deck
        deck = Deck()
        pot = 0        
        #take blind bets
        pot = smallBAmt + bigBAmt
        players[blindsArr[1]].chipcount = players[blindsArr[1]].chipcount - smallBAmt
        players[blindsArr[2]].chipcount = players[blindsArr[2]].chipcount - bigBAmt
        #deal 2 cards to each player
        for player in players:
            player.hand = deck.draw(2)
        activePlayers = players
        board = []
        for x in range (5):
            board.append(deck.draw(1))
        #preflop betting round
        if (blindsArr[2] + 1 > numPlayer - 1):
            action = 0
        else:
            action = blindsArr[2] + 1
        randomNum = random.uniform(0, 1)            
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



