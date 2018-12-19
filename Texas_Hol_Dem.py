from random import shuffle

def getDeck():
    suits = ["Spades","Hearts","Clubs","Diamonds"]
    deckOfCards = []
    for i in suits:  # Go through suits and numbers to make deck
        for n in range(1,14):
            deckOfCards.append((n,i))
    shuffle(deckOfCards)
    return deckOfCards
    
def getPlayers(n):
##    Create 'players' parameter with n players
##    Calls for dealCards(deck,players)
    players = []
    status = ""
    #money = eval(input("How much money? "))
    for i in range(1,n+1):
        #name, status, money, hand, ammount bet, if all-in 1/0
        #players.append([input("Player name: "),status,money,[],0,0])
        players.append([i,status,50,[],0,0])
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

##    Show what is on the table (0-5 cards) and in this players hand
##    Show what has been betted by other players
##    Show how much money player has left
##    Show how much money other players have left
##    Ask the player what they want to do: fold,raise,call,check,all_in,savegame
def playerTurn(player,tableC,tA):
    print("Table ", cardsToText(tA[0][:tableC]))
    print("Player",player[0],"last turn:",player[1],"money:",player[2],"in pot",tA[1])
    print("You have betted",player[4])
    print("Your hand:",cardsToText(player[3]))
    return (input("Check, fold, call, raise/all in or savegame:"))
    
def checkWinner(players,table):
    hands = []
    suits = ["Spades","Hearts","Clubs","Diamonds"]
    players[0][3] = [(1, "Spades"), (2, "Spades")]
    table = [(10, "Spades"), (9, "Hearts"),(3,"Spades"),(4,"Spades"),(5,"Spades")]
    for i in range(len(players)):
        hands.append([players[i][3]+table,players[i]])
        
##    Compare all possible player hands
##    Start from highest hands and move down
##  Number after hand indicates ranking, 1 is best

    for hand in hands:
        for i in range(1,14):
            
##        Four of a kind 3 Highest or kicker wins
            if hand[0][0].count(i) == 4:
                hands[hands.index(hand)] = (hand,3,i,0)
                break
            
##        Full house 4 threes are better than twos
            elif hand[0][0].count(i) == 3:
                for j in range(1,14):
##        Three of a kind 7 Highest or sides win
                    if i != j and hand[0][0].count(j) == 2:
                        hands[hands.index(hand)] = (hand,4,i,j)
                        break
                hands[hands.index(hand)] = (hand,7,i,0)
                
##        Two pair 8 Highest or sides win
            elif hand[0][0].count(i) == 2:
                for j in range(1,14):
##        Pair 9 Highest or sides win
                    if i != j and hand[0][0].count(j) == 2:
                        hands[hands.index(hand)] = (hand,8,0)
                        break
                hands[hands.index(hand)] = (hand,9,0)

        for s in suits:
            if hand[0][1].count(s) > 4:#flush
                v = s
                kj = hand[0][1].findAll(v)#straight
##        Straight flush 2 Highest wins 
                if sorted(kj) == range(min(kj), max(kj)+1):
                    hands[hands.index(hand)] = (hand,2,0)
                    print("straight flush")

##        Flush 5 Highest wins                  
                hands[hands.index(hand)] = (hand,8,0)

##        Straight 6 Highest wins
##        High 10

    print("END")
    print(max(hands,key=lambda x:x[1]))


def saveGame(name):
##    Save:
##        the part of game: flop, turn, river
##        player hands and moneys
##        acting player
##        pot
    with open("texas.txt","w") as file:
        file.write(str(deck))#,table))
        
##def saveWinner(nameW):
####    When game ends save the winner and much they won

def cardsToText(cards):
##    Converts given cards to readable form
    hand = []
    # If face card convert to letters
    for i in cards:
        if i[1] == 11:
            hand.append("J of "+ str(i[0]))  #   i[0] = suit
        elif i[1] == 12:
            hand.append("Q of "+str(i[0]))
        elif i[1] == 13:
            hand.append("K of "+str(i[0]))
        elif i[1] == 1:
            hand.append("A of "+str(i[0]))
        else:
            hand.append(str(i[1])+ " of "+str(i[0]))
    return (', '.join(hand))

def nextRound(tA,players,i=-1):
    for pl in players:
        if pl[4] < tA[3] and  not pl[5] == 1:
            print("eka")
            return True
        
    for pl in players:
        if pl[1][:5] == "raise" and players[i][1][:5] != "raise":
            print("toka")
            return True

    if (any(pl[1] == "blind" for pl in players)):
        print("kolmas")
        return True

    if (any(pl[1] == "" for pl in players)):
        print ("newROUND!!!")
        return True

    return False

    
def main():
    global deck
    deck = getDeck()
    players = getPlayers(eval(input("How many players? ")))
    
    #[cards on table, pot, blind, highestbet
    #blind should be asked and not set by default
         #     0       1  2  3  
    tA = [dealTable(), 0, 5, 5] #tableArgs
    tA[3] = tA[2]#set highestbet to blind = 5
    
    # Players take turns until every
    # player after the last raise has checked, folded, called or
    # someone saves the game

    blindStatus = 0
    tc = 0
    won = False
    #                         0                1    2    3  4 5
    #players.append([input("Player name: "),status,money,[],0,0])
    #4 = players money in pot ;5 = all in 1/0
    
        
    for tc in [0,3,4,5]:
        print("TC ADDED =",tc)


        while True:
            if nextRound(tA,players) == False:
                print("add cards to table and begin new round")
                for pl in players:  # Reset player status
                    pl[1] = ""
                break

            for i in range(len(players)):


                if nextRound(tA,players,i):
                    print("\n seuraava pelaaja on", players[i][0])
                    #blind, fold and allin checks
                    if True:
                        if blindStatus == 0:        # 1st player must pay blind
                            print("Player",players[i][0],"has blind of",tA[2])
                            blindStatus = 1
                            players[i][1] = "blind"
                            players[i][4] = tA[2]
                            tA[1] = tA[2]
                            continue

                        if players[i][0] == "fold":
                            print("Player",players[i][0],"has folded")
                            continue

                        if players[i][5] == 1:
                            print("Player",players[i][0],"has allin'd")
                            continue

                        x = 0
                        for p in players:
                            if p[1] == "fold":
                                x += 1

                        if x == len(players)-1:
                            #If all others have folded you win
                            for p in players:
                                if p[1] != "fold":
                                    print("Others folded,",p[0],"won")
                                    break
                            won = True
                            break

                    if players[i][4] <= tA[3]:

                        while True:  # Loop escaped when a legal move is entered
                            players[i][1] = playerTurn(players[i], tc, tA)
                           
                            if players[i][1][:5] == "raise":
                                bet = eval(players[i][1][6:])
                                if bet == players[i][2]:
                                    print("allin")
                                    tA[1] += players[i][2]
                                    players[i][2] = 0  #monies to 0
                                    players[i][4] += bet
                                    players[i][5] = 1
                                    break 
                                tA[1] += bet #bet is added to pot
                                players[i][2] += -(bet) #take money from player
                                ta[3] = players[i][4]
                                print("You raised",bet)
                                print("You now have",players[i][2],"left")
                                break
                                
                            elif players[i][1] == "fold":
                                print("Player",players[i][0],"folded")
                                break

                            #tA[3] = highestBet ta[1] = pot
                            elif players[i][1] == "call":
                                if players[i][4] < tA[3]:
                                    print("You called with",tA[3]-players[i][4])
                                    tA[1] += tA[3]-players[i][4]#pot +=highbet-bettedbypl
                                    players[i][2] += -(tA[3]-players[i][4])#plmoney+=-(hb-bbpl)
                                    players[i][4] = tA[3]
                                    print("You now have",players[i][2],"left")
                                    break
                                else:
                                    print("You can't call, You just can't")
                                    continue

                            elif players[i][1] == "check":
                                if players[i][4] == tA[3]:
                                    print("Player",players[i][0],"checked")
                                    break
                                else:
                                    print("You need to match the pot")
                                    continue

                            elif players[i][1] == "savegame":
                                saveGame("homoW")
                                break
                            else:
                                print("Type proper commands!")
                                continue
                else:
                    break

        if won:
            print("voitto")
            break
        if tc == 5:
            break

    winc = []
    for pl in players:
        if pl[1] != "fold":
            winc.append(pl)
    checkWinner(winc,tA[0])
    print("game END")
    
    #Blind moves forward
    #saveWinner(checkWinner(players,table))


if __name__ == "__main__":
    main()
