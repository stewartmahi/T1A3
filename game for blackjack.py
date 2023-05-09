import random

class Card:
    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank
        
    def __str__(self):
        return f"{self.rank} of {self.suit}"

class Deck:
    def __init__(self):
        self.cards = []
        suits = ["Hearts", "Diamonds", "Clubs", "Spades"]
        ranks = ["Ace", "2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "King"]
        for suit in suits:
            for rank in ranks:
                self.cards.append(Card(suit, rank))
        random.shuffle(self.cards)
        
    def deal_card(self):
        return self.cards.pop()

class Hand:
    def __init__(self):
        self.cards = []
        self.value = 0
        self.aces = 0
        
    def add_card(self, card):
        self.cards.append(card)
        if card.rank == "Ace":
            self.aces += 1
        self.value += self.card_value(card)
        
    def card_value(self, card):
        if card.rank in ["2", "3", "4", "5", "6", "7", "8", "9", "10"]:
            return int(card.rank)
        elif card.rank in ["Jack", "Queen", "King"]:
            return 10
        else:
            return 11
        
    def adjust_for_ace(self):
        while self.value > 21 and self.aces:
            self.value -= 10
            self.aces -= 1

class Chips:
    def __init__(self, total=100):
        self.total = total
        self.bet = 0
        
    def win_bet(self):
        self.total += self.bet
        
    def lose_bet(self):
        self.total -= self.bet

def take_bet(chips):
    while True:
        try:
            chips.bet = int(input("How many chips would you like to bet? "))
        except ValueError:
            print("Sorry, a bet must be an integer!")
        else:
            if chips.bet > chips.total:
                print(f"Sorry, your bet can't exceed {chips.total}")
            else:
                break

def hit(deck, hand):
    hand.add_card(deck.deal_card())
    hand.adjust_for_ace()

def hit_or_stand(deck, hand):
    global playing
    while True:
        x = input("Would you like to Hit or Stand? Enter 'h' or 's' ")
        if x[0].lower() == 'h':
            hit(deck, hand)
        elif x[0].lower() == 's':
            print("Player stands. Dealer is playing.")
            playing = False
        else:
            print("Sorry, please try again.")
            continue
        break

def show_some(player, dealer):
    print("\nDealer's Hand:")
    print(" <card hidden>")
    print("", dealer.cards[1])
    print("\nPlayer's Hand:", *player.cards, sep='\n ')
    
def show_all(player, dealer):
    print("\nDealer's Hand:", *dealer.cards, sep='\n ')
    print("Dealer's Hand =", dealer.value)
    print("\nPlayer's Hand:", *player.cards, sep='\n ')
    print("Player's Hand =", player.value)

def player_busts(player, dealer, chips):
    print("Player busts!")
    chips.lose_bet()

def play_again():
    while True:
        choice = input("Do you want to play again? (Y/N): ").lower()
        if choice == 'y':
            return True
        elif choice == 'n':
            return False
        else:
            print("Invalid input. Please enter 'Y' or 'N'.")



def player_wins(player_hand, dealer_hand, chips):
    chips.win_bet()
    print("Player wins!")
    print("Player's hand:", player_hand)
    print("Dealer's hand:", dealer_hand)
    print("Player's chips:", chips.total)
    play_again()

def dealer_wins(player_hand, dealer_hand, chips):
    chips.lose_bet()
    print("Dealer wins!")
    print("Player's hand:", player_hand)
    print("Dealer's hand:", dealer_hand)
    print("Player's chips:", chips.total)
    play_again()

def play_game():
    print("Welcome to Blackjack!\n")

    # Create the deck and the player's and dealer's hands
    deck = Deck()
    player_hand = Hand()
    dealer_hand = Hand()

    # Create the player's chips
    player_chips = Chips()

    while True:
        # Take the player's bet
        take_bet(player_chips)

        # Deal two cards to the player and the dealer
        player_hand.add_card(deck.deal_card())
        player_hand.add_card(deck.deal_card())
        dealer_hand.add_card(deck.deal_card())
        dealer_hand.add_card(deck.deal_card())

        # Show the player's cards and one of the dealer's cards
        show_some(player_hand, dealer_hand)

        # Let the player hit or stand
        playing = True
        while playing:
            hit_or_stand(deck, player_hand)
            show_some(player_hand, dealer_hand)

            if player_hand.value > 21:
                player_busts(player_hand, dealer_hand, player_chips)
                break

        # If the player hasn't busted, play the dealer's hand
        if player_hand.value <= 21:
            while dealer_hand.value < 17:
                hit(deck, dealer_hand)

            # Show all the cards
            show_all(player_hand, dealer_hand)

            # Determine the winner
            if dealer_hand.value > 21:
                dealer_busts(player_hand, dealer_hand, player_chips)
            elif dealer_hand.value > player_hand.value:
                dealer_wins(player_hand, dealer_hand, player_chips)
            elif dealer_hand.value < player_hand.value:
                player_wins(player_hand, dealer_hand, player_chips)
            else:
                push(player_hand, dealer_hand, player_chips)

        # Ask the player if they want to play again
        if not play_again():
            break

    print("Thanks for playing!")

