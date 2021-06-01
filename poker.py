from deck_of_cards import deck_of_cards

def dealCards(deck):
    return 0

if __name__ == "__main__":
    #create deck
    deck = deck_of_cards.DeckOfCards()
    #get number of players
    numPlayers = getPlayers()
    #while game is being played
    while true:
        #take blind bets
        blindBets()
        #deal 2 cards to each player
        dealCards(deck)
        #preflop betting round
        
