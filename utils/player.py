import random


class Player:

    """

    Class that automatically asks for the amount of players and holds the cards for each player.

    """
    
    def __init__(self, name):
        self.name = name
        self.cards = []
        # self.turn_count = 0
        # self.number_of_cards = 0
        # self.history = []
        # moeten nog terug in __init__(...) 

 
        


    # def play(self):
    #     play.randomcard = random.randomint(self.cards)
    #     self.history.append(play.randomcard)
    #     self.cards.remove(play.randomcard)
    #     print (f'{PLAYER_NAME} {TURN_COUNT} played: {CARD_NUMBER} {CARD_SYMBOL_ICON}')
    #     return play.randomcard


class Deck:
    """
    Class to generate a full card deck and distribute it amongst the players.

    """

    def __init__(self):

        """
          Method that contains the complete deck of cards in self.cards as a list.
        """

        self.cards = []


    def fill_deck(self):
        """
        Method that is used to generate a list of a complete deck of cards (= 52 cards)

        For each icon  ['♥', '♦', '♣', '♠'] there are 13 values ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']
        with either the color Red ('R') for the icons ♥ and ♦,  or Black ('B') for the icons ♣ and ♠

        """

        for i in ['♥', '♦', '♣', '♠']:
            if i in ['♥', '♦']:
                color = "R"
            else:
                color = "B"
            for j in ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']:
                self.cards.append([i, j, color])

    def shuffle(self):
        """

        Method used to shuffle the complete deck of cards stored in self.cards.

        """
        random.shuffle(self.cards)
    
    def distribute(self):
    
        """

        Method used to distribute the cards amongst the different players.

        """
        #number of rounds
        #floor division
        #
        i = 0    
        while self.cards > 0:
            for p in List_of_players:
                card = self.cards[i]
                Player(self.cards).append(card)
                i += 1
            self.cards.pop(card)
    





