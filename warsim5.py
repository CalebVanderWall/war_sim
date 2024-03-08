

def warsim5(n):
    i = 0
    def warmode(ci):
        ci = ci + 5
        print(ci)
        print(f"player1 {player1.hand[ci].value}, player2 {player2.hand[ci].value}")
        if len(player1.hand) >= ci and len(player2.hand) >= ci: #detected that each player has enough cards for war to take place.

            if player1.hand[ci].value > player2.hand[ci].value:
                player1.hand.extend(player2.hand[0:ci]) #puts winning cards on bottom of deck
                player1.hand.extend(player1.hand[0:ci]) #puts victorious cards on bottom of deck
                player1.hand = player1.hand[ci:] #deletes duplicate cards from victor's deck
                player2.hand = player2.hand[ci:] #deletes lost cards from loser's deck
            
            elif player1.hand[ci].value < player2.hand[ci].value:
                player1.hand.extend(player2.hand[0:ci]) #puts winning cards on bottom of deck
                player1.hand.extend(player1.hand[0:ci]) #puts victorious cards on bottom of deck
                player1.hand = player1.hand[ci:] #deletes duplicate cards from victor's deck
                player2.hand = player2.hand[ci:] #deletes lost cards from loser's deck

            else:
                warmode(ci)
        
        elif len(player1.hand) < ci or len(player2.hand) < ci:  #detected not enough cards to proceed with war
        
            if len(player1.hand) > len(player2.hand):
                i = 1
                return 1
            elif len(player1.hand) < len(player2.hand):
                i = 1
                return 2
        

    while i != n:
        import random
        import class_card
        import class_player

        
        class card:
            def __init__(self,value,suite):
                self.value = value
                self.suite = suite
        cards = []

        class player:
            def __init__(self,hand):
                self.hand = hand

        H1 = card(1,1)
        H2 = card(2,1)
        H3 = card(3,1)
        H4 = card(4,1)
        H5 = card(5,1)
        H6 = card(6,1)
        D1 = card(1,2)
        D2 = card(2,2)
        D3 = card(3,2)
        D4 = card(4,2)
        D5 = card(5,2)
        D6 = card(6,2)
        C1 = card(1,3)
        C2 = card(2,3)
        C3 = card(3,3)
        C4 = card(4,3)
        C5 = card(5,3)
        C6 = card(6,3)
        S1 = card(1,4)
        S2 = card(2,4)
        S3 = card(3,4)
        S4 = card(4,4)
        S5 = card(5,4)
        S6 = card(6,4)
        cards = [H1,H2,H3,H4,H5,H6,D1,D2,D3,D4,D5,D6,C1,C2,C3,C4,C5,C6,S1,S2,S3,S4,S5,S6]
        
        random.shuffle(cards)

        player1 = player(cards[0:12])
        player2 = player(cards[12:24])

        battle_counter = 1
        war_counter = 0
        
########################        BATTLE           
        while len(player1.hand) > 0 and len(player2.hand) > 0:
            print(f"Battle {battle_counter}")

            print("player 1 hand") 
            for card in player1.hand:
                print(card.value,card.suite)
            print("player 2 hand")      
            for card in player2.hand:
                print(card.value,card.suite)
            print(len(player1.hand))

            print(f"Battle {battle_counter} results: player1 {player1.hand[0].value}, player2 {player2.hand[0].value}")
            
            if player1.hand[0].value == player2.hand[0].value and len(player1.hand) < 5:
                return 2
            #win condition
            elif player1.hand[0].value == player2.hand[0].value and len(player2.hand) < 5:
                return 1     
            #win condition
            elif len(player1.hand) == 0 or len(player2.hand) == 0:
                if len(player1.hand) == 0:
                    i = 1
                    return 2
                elif len(player2.hand) == 0:
                    i = 1
                    return 1
             #win condition   
            elif player1.hand[0].value > player2.hand[0].value:
                player1.hand.append(player2.hand[0])
                player1.hand.append(player1.hand[0])
                player1.hand = player1.hand[1:]
                player2.hand = player2.hand[1:]

                
            elif player1.hand[0].value < player2.hand[0].value:
                player2.hand.append(player1.hand[0])
                player2.hand.append(player2.hand[0]) 
                player1.hand = player1.hand[1:]
                player2.hand = player2.hand[1:] 

            elif player1.hand[0].value == player2.hand[0].value:
                ci = 0
                print(f"War {war_counter}")
                war_counter = war_counter + 1
                warmode(ci)
                ci = 0
                
            battle_counter = battle_counter + 1
        
        if len(player1.hand) > len(player2.hand):
            return 1
        else:
            return 2
        i = 1
##            
##        
##    



 
