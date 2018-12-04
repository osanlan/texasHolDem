from random import shuffle

def getDeck():
    suits = ["Spades","Hearts","Clubs","Diamonds"]
    deckOfCards = []
    for i in suits:  # Go through suits and numbers to make deck
        for n in range(1,14):
            deckOfCards.append((i,n))
    shuffle(deckOfCards)
    return deckOfCards
    
def getPlayers(n):
##    Create 'players' parameter with n players
##    Calls for dealCards(deck,players)
    players = []
    status = ""
    money = eval(input("How much money? "))
    for i in range(n):
        #name, status, money, hand, allin(0 or pot)
        players.append([input("Player name: "),status,money,[],0])
    dealCards(players)
    return players
    
def dealCards(players):
##    Deal cards to players hands
##    Move top two cards from deck to player[2]
    for pl in players:
        for i in range(2):
            pl[3].append(deck[len(deck)-1])
            deck.pop(len(deck)-1)
    return players

def dealTable():
##    Deal cards to 'table'
##    Move top five cards from deck to table
    table = []
    for i in range(5):
        table.append(deck[len(deck)-1])
        deck.pop(len(deck)-1)
    return table

#def playerTurn(player,tableCards):
##    Show what is on the table (0-5 cards) and in this players hand
##    Show what has been betted by other players
##    Show how much money player has left
##    Show how much money other players have left
##    Ask the player what they want to do: fold,raise,call,check,all_in,savegame
    # Fold: give up this round - Ready
        # Folded player cant play anymore 
    # Check: keep playing without raising - Ready
    # Call: match what has been betted by other players - Ready
    # Raise: bet more than others have - Ready but all other players are Not Ready
    # All_in: bet all your moneys, set allin to current pot - Ready
    # Savegame: game is paused and saved to file
    

#def checkWinner(players,table):
##    Compare all possible player hands
##    Start from highest hands and move down
##  Number after hand indicates ranking, 1 is best
    
##        Four of a kind 3 Hihgest or kicker wins
##        Full house 4 threes are better than twos
    ##        Three of a kind 7 Highest or sides win
##        Two pair 8 Highest or sides win
    ##        Pair 9 Highest or sides win
    
# If all cards are different and
# if cards are all in the same suit
    ##        Straight flush 2 Highest wins  
    ##        Flush 5 Highest wins

# If cards are not all in the same suit
    ##        Straight 6 Highest wins

    ##        High 10
        
##    Determine winner
##    Prints and returns winners name and how much they won

def saveGame(name):
##    Save:
##        the part of game: flop, turn, river
##        player hands and moneys
##        acting player
##        pot
    with open("texas.txt","w") as file:
        file.write(deck,table)
##def saveWinner(nameW):
####    When game ends save the winner and much they won
##
##def cardsToText(cards):
####    Converts given cards to readable form
##    hand = []
##    # If face card convert to letters
##    for i in listOfCards:
##        if i[1] == 11:
##            hand.append("J of "+ str(i[0]))  #   i[0] = suit
##        elif i[1] == 12:
##            hand.append("Q of "+str(i[0]))
##        elif i[1] == 13:
##            hand.append("K of "+str(i[0]))
##        elif i[1] == 1:
##            hand.append("A of "+str(i[0]))
##        else:
##            hand.append(str(i[1])+ " of "+str(i[0]))
##    #print (', '.join(hand))

    
def main():
    global deck
    deck = getDeck()
    players = getPlayers(eval(input("How many players? ")))
    table = dealTable()
    pot = 0
    blind = eval(input("How much is blind? "))
    # Players take turns until every
    # player after the last raise has checked, folded, called or
    # someone saves the game
    ready = False
    blindStatus = 0
    betInc = blind
    while ready == False:
        for i in range(len(players)):
            if blindStatus == 0:
                #Must raise blind
                blindStatus = 1
                continue
            
            if player[i][1] == "fold":
                continue
            
            playerTurn(players[i], 0)
            if players[i][1][:5] == "raise":
                bet = eval(players[i][1][6:])
                pot += bet
                betInc = bet
                players[i][2] += -(bet)
                ready = False
                
            elif players[i][1] == "fold":
                ready = True
                
            elif players[i][1] == "all_in":
                pot += players[i][2]
                players[i][2] = 0
                players[i][4] = pot
                ready = True
                
            elif players[i][1] == "call":  
                pot += betInc
                ready = True
                
            elif players[i][1] == "savegame":
                savegame("homoW")
                    
            status.append(players[i][1]) #Player from index i of players -> status
            
    #while loop raise
        for player in players:
            playerTurn(player, 3)
    
    #while loop raise
        for player in players:
            playerTurn(player, 4)
    
    #while loop raise
        for player in players:
            playerTurn(player, 5)

    #Blind moves forward
    #saveWinner(checkWinner(players,table))


if __name__ == "__main__":
    main()




    
