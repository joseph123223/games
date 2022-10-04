from cgi import print_arguments
import random
suits = ('Hearts', 'Diamonds','Spades','Clubs')
ranks = ('Two','Three','Four','Five','Six','Seven','Eight','Nine','Ten','Jack','Queen','King','Ace')
values = {'Two':2, 'Three':3, 'Four':4, 'Five':5, 'Six':6, 'Seven':7, 'Eight':8, 'Nine':9, 'Ten':10, 'Jack':11, 'Queen':12, 'King':13, 'Ace':14}

class Card:

    def __init__(self,suit,rank) -> None:
        self.suit = suit
        self.rank = rank
        self.value = values[rank]
    
    def __str__(self) -> str:
        return self.rank + " of " + self.suit

class Deck:

    def __init__(self) -> None:
        self.all_cards = []

        for suit in suits:
            for rank in ranks:
                #Create Card Object
                created_card = Card(suit,rank)
                self.all_cards.append(created_card)
    
    def shuffle_card(self):
        random.shuffle(self.all_cards)
    
    def deal_one_card(self):
        return self.all_cards.pop()

class Player:

    def __init__(self,name) -> None:
        self.name = name
        self.all_card = []

    def remove_one(self):
        return self.all_card.pop(0)

    def add_cards(self,new_cards):
        if type(new_cards) == type([]):
            self.all_card.extend(new_cards)
        else:
            self.all_card.append(new_cards)

    def __str__(self) -> str:
        return f"Player {self.name} has {len(self.all_card)} cards!"

if __name__ == '__main__':
    # game setup
    new_deck = Deck()
    new_deck.shuffle_card()
    player_one = Player("P1")
    player_two = Player("P2")

    #cards deal
    for i in range(26):
        player_one.add_cards(new_deck.deal_one_card())
        player_two.add_cards(new_deck.deal_one_card())
    
    #Game Start!
    game_on = True
    gameround = 0

    while game_on:

        if len(player_one.all_card) == 0:
            print("Player 1 Out of the cards! Player 2 Win!")
            game_on = False
            break
        if len(player_two.all_card) == 0:
            print("Player 2 Out of the cards! Player 1 Win!")
            game_on = False
            break

        gameround+=1
        print(f"It's round {gameround}")

        # New round started
        player_one_cards = []
        player_one_cards.append(player_one.remove_one())

        player_two_cards = []
        player_two_cards.append(player_two.remove_one())

        war = True
        # War started
        while war:

            if player_one_cards[-1].value > player_two_cards[-1].value:
                player_one.add_cards(player_one_cards)
                print(f"Player 1 has the card: {player_one_cards[-1]}")
                player_one.add_cards(player_two_cards)
                print(f"Player 2 has the card: {player_two_cards[-1]}")
                print("Player 1 Win the round")
                war = False

            elif player_one_cards[-1].value < player_two_cards[-1].value:
                player_two.add_cards(player_two_cards)
                print(f"Player 1 has the card: {player_one_cards[-1]}")
                player_two.add_cards(player_one_cards)
                print(f"Player 2 has the card: {player_two_cards[-1]}")
                print("Player 2 Win the round")
                war = False
            
            # multiple wars!
            else:
                print("War started!")

                if len(player_one.all_card) < 3:
                    print("Player 1 have less than 5 cards, can't attend wars!")
                    print("Player 2 Wins!")
                    game_on = False
                    break
                
                elif len(player_two.all_card) < 3:
                    print("Player 2 have less than 5 cards, can't attend wars!")
                    print("Player 1 Wins!")
                    game_on = False
                    break

                else:
                    for n in range(3):
                        player_one_cards.append(player_one.remove_one())
                        player_two_cards.append(player_two.remove_one())