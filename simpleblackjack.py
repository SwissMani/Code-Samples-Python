"""
   Black Jack Game 
   
"""
 
import random
 
 
CHECK = 21
BREAKER = "--------------------------------------"
 
 
class Deck:
    """
   Create a deck object
   """
 
    def __init__(self):
        self.cards = ['2', '3', '4', '5', '6', '7', '8', '9', '10',
                      'J', 'Q', 'K', 'A']
        self.faces = ['♣', '♥', '♠', '♦']
        self.deck = [face + card for face in self.faces for card in self.cards]
 
    def remove_card(self, cards):
        """
       :param cards: Player's cards
       :type cards: list
       """
        for i in cards:
            if i in self.deck:
                self.deck.remove(i)
 
    def shuffle_deck(self):
        """
       Shuffles the deck on spot
       """
        random.shuffle(self.deck)
 
 
class Player(Deck):
    """
   Create a PLAYER object
   """
 
    def __init__(self, name):
        """
       Create a PLAYER with a name
       :type name: str
       """
        Deck.__init__(self)
        self.name = name
        self.chips = 100
        self.cards = []
        self.amountbet = 0
        self.a_value = 11
        self.wonstate = False
        self.betstate = False
 
    def bet(self, amount):
        """
       :param amount: Amount of chips to bet
       :type amount: int
       """
        self.amountbet = amount
        if self.chips >= amount:
            self.chips -= amount
            print(
                f"{self.name} has successfully placed a bet of {amount} chips"
            )
            print(f"Chip balance: {self.chips}")
            self.betstate = True
        else:
            print(f"{self.name} has insufficient amount of chips!")
            print(f"Your balance: {self.chips}")
            print(f"Bet amount: {amount}")
            self.betstate = False
 
    def deal(self):
        """
       Deal 2 cards to PLAYER
       """
        # noinspection PyUnusedLocal
        self.cards += [random.choice(self.deck) for i in range(2)]
 
    def show(self, hidden=False):
        """
       :param hidden: True if you want to hide player's first card
       :type hidden: bool
       """
        if self.name == "DEALER":
            if hidden:
                cardl = self.cards.copy()
                cardl[0] = ""
                multi_line_print(cardl, hidden=True)
            else:
                multi_line_print(self.cards)
        else:
            print(BREAKER)
            print("Player's Cards: ")
            multi_line_print(self.cards)
 
    def hit(self):
        """
       PLAYER hits and asks for a card
       """
        # noinspection PyUnusedLocal
        self.cards += [random.choice(self.deck) for i in range(1)]
 
    def won(self):
        """
       doubles the amount of chips that player bet
       won state to true
       :return: nothing
       """
        self.chips += self.amountbet * 2
        self.wonstate = True
 
    @property
    def sumofcards(self):
        """
       calculates sum of cards
       :return: sum of cards
       """
        sum_cards = 0
        for i in self.cards:
            card_value = list(i)[1]
            if card_value in ["J", "Q", "K", "1"]:
                card_value = 10
            elif card_value == "A":
                card_value = self.a_value
            sum_cards += int(card_value)
        return sum_cards
 
    def __len__(self):
        return len(self.cards)
 
    def reset(self):
        """
       reset
           cards
           wonstate
           betstate
           bet amount
       :return: nothing
       """
        self.cards = []
        self.wonstate = False
        self.betstate = False
        self.amountbet = 0
 
    def buy_chips(self, cash_to_chips):
        """
 
       :param cash_to_chips: cash amount to chips
       :return: nothing
       """
        self.chips += cash_to_chips * 2
 
    def a_value_change(self):
        """
       Changes the A card value if needed
       :return: bool if value was changed or not
       """
        for i in self.cards:
            card_value = list(i)[1]
            if card_value == "A":
                self.a_value = 1
        return self.a_value == 1
 
 
def multi_line_print(list_to, hidden=False):
    """
   :param list_to: list of PLAYER's cards
   :param hidden: True or False if PLAYER's first card is hidden
   :type list_to: list
   :type hidden: bool
   """
    cards = []
    for i, card_to_print in enumerate(list_to):
        if hidden and i == 0:
            cards += [f"""
               ----------
               |  .••.  |
               |  .••.  |
               |  .••.  |
               ----------
           """]
        elif card_to_print in ['♣10', '♥10', '♠10', '♦10']:
            cards += [f"""
               ----------
               |{card_to_print}     |
               |        |
               |     {card_to_print}|
               ----------
           """]
        else:
            cards += [f"""
               ----------
               |{card_to_print}      |
               |        |
               |      {card_to_print}|
               ----------
           """]
    strings_by_column = [s.split('\n') for s in cards]
    strings_by_line = zip(*strings_by_column)
    max_length_by_column = [
        max([len(s) for s in col_strings])
        for col_strings in strings_by_column
    ]
    for parts in strings_by_line:
        # Pad strings in each column so they are the same length
        padded_strings = [
            parts[i].ljust(max_length_by_column[i])
            for i in range(len(parts))
        ]
        print(''.join(padded_strings))
 
 
def won(who="PLAYER"):
    """
   :param who: if DEALER pass "DEALER" for DEALER's settings
   :type who: str
   """
    if who == "PLAYER":
        print(BREAKER)
        PLAYER.won()
        print(f"Congratulations! {PLAYER.name}")
        print(f"You have gained {PLAYER.amountbet * 2} chips")
        PLAYER.show()
        print(f"Player's score: {PLAYER.sumofcards}")
        print(f"Dealer's score: {DEALER.sumofcards}")
    elif who == "tie":
        print(BREAKER)
        print(f"Tie!")
        print("Dealer's Cards: ")
        DEALER.show()
        print(f"Dealer's score: {DEALER.sumofcards}")
        PLAYER.show()
        print(f"Player's score: {PLAYER.sumofcards}")
    else:
        print(BREAKER)
        print(f"Dealer won!")
        print("Dealer's Cards: ")
        DEALER.show()
        print(f"Dealer's score: {DEALER.sumofcards}")
        print(f"Player's score: {PLAYER.sumofcards}")
 
 
print("Welcome to BlackJack")
print("Please enter the following information")
print(BREAKER)
NAME = input("Name: ")
print(f"Thank you for playing and enjoy {NAME}")
PLAYER = Player(NAME)
DEALER = Player("DEALER")
DECK = Deck()
DECK.shuffle_deck()
 
 
def player_hit_loop():
    """
   Player loop for hitting
   :return: nothing
   """
    hit = input("Would you like to stand or hit? (stand/hit): ")
    if PLAYER.sumofcards == CHECK and PLAYER.wonstate is False:
        hit = "stand"
    while hit != "stand":
        if hit == "hit":
            PLAYER.hit()
            DECK.remove_card(PLAYER.cards)
            PLAYER.show()
        if PLAYER.sumofcards > CHECK:
            change = PLAYER.a_value_change()
            if change is False:
                break
        if PLAYER.sumofcards == CHECK:
            break
        print(BREAKER)
        hit = input("Would you like to stand or hit? (stand/hit): ")
 
 
def dealer_hit_loop():
    """
   Dealer loop for hitting
   :return: nothing
   """
    hitbycomp = True
    if DEALER.sumofcards >= 17:
        hitbycomp = False
    elif DEALER.sumofcards > CHECK:
        DEALER.a_value_change()
        hitbycomp = False
    elif DEALER.sumofcards == CHECK:
        hitbycomp = False
    elif PLAYER.wonstate is True:
        hitbycomp = False
 
    while hitbycomp and PLAYER.wonstate is False:
        print("Dealer Hits")
        DEALER.hit()
        DECK.remove_card(DEALER.cards)
        print(BREAKER)
        print("Dealer's Cards: ")
        DEALER.show(hidden=True)
 
        if DEALER.sumofcards == CHECK:
            break
        elif DEALER.sumofcards > CHECK:
            change = DEALER.a_value_change()
            if change is False:
                break
        if DEALER.sumofcards >= 17:
            break
 
 
def main():
    """
   game setup loop
   :return: nothing
   """
    run = True
    while run:
        print(BREAKER)
        print("Chips Counter: ")
        print(f"{PLAYER.name} has {PLAYER.chips} chip\\s")
        print(BREAKER)
        bet = int(input("Bet(Amount of chips): "))
        PLAYER.bet(bet)
        if PLAYER.betstate is False:
            print(BREAKER)
            buy_chips = input("Would you like to buy chips? (yes/no) ")
            if buy_chips == "yes":
                print("To play:")
                print(
                    f"\tconvert ${int((bet - PLAYER.chips) / 2)}"
                )
                print(BREAKER)
                cash_amount = int(input(
                    "Cash to Chips converter ($1 - 2 chips): $")
                )
                PLAYER.buy_chips(cash_amount)
                print(f"{PLAYER.name} now has {PLAYER.chips} chip\\s")
                if PLAYER.chips >= PLAYER.amountbet:
                    PLAYER.bet(bet)
                else:
                    PLAYER.amountbet = 0
                    break
            else:
                PLAYER.amountbet = 0
                break
 
        PLAYER.deal()
        DECK.remove_card(PLAYER.cards)
        DEALER.deal()
        DECK.remove_card(DEALER.cards)
        game()
        PLAYER.reset()
        DEALER.reset()
        run = False
 
    print(BREAKER)
    play_again = input("Would you like to continue playing? (yes/no): ")
    if play_again == "yes":
        main()
 
 
def game():
    """
   game loop
   :return: nothin
   """
    PLAYER.show()
    print(BREAKER)
    print("Dealer's Cards: ")
    DEALER.show(hidden=True)
    print(BREAKER)
    player_hit_loop()
    dealer_hit_loop()
 
    if DEALER.sumofcards == PLAYER.sumofcards:
        won("tie")
    elif DEALER.sumofcards > CHECK and PLAYER.sumofcards > CHECK:
        won("tie")
    elif PLAYER.sumofcards == CHECK:
        won()
    elif DEALER.sumofcards == CHECK:
        won("DEALER")
    elif PLAYER.sumofcards < DEALER.sumofcards <= CHECK:
        won("DEALER")
    elif DEALER.sumofcards > PLAYER.sumofcards <= CHECK:
        won()
    elif PLAYER.sumofcards > CHECK:
        won("DEALER")
    else:
        won()
 
 
if __name__ == "__main__":
    main()
 
print(BREAKER)
print(f"Thank you for playing {PLAYER.name}!")
print("Black Jack")
