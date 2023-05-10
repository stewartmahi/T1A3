import random

#we have imported random, to use throughout this entire game, because uno has a lot of randomness

"""Generate UNO deck of 108 cards, Parameters: None, Return Values: Deck-List"""

def build_deck():
    deck = []

    #Examples of cards in uno include Red 9, Yellow 7, Green Skip

    colors = ["Red","Green","Yellow","Blue"]
    values = [0,1,2,3,4,5,6,7,8,9,"Draw Two", "Skip", "Reverse"]
    wilds = ["Wild","Wild Draw Four"]

    for color in colors:
        for value in values:
            card_value = f"{color} {value}"
            deck.append(card_value)
            if value != 0:
                deck.append(card_value)
    
    for i in range(4):
        deck.append(wilds[0])
        deck.append(wilds[1])
    
    return deck

# for the build_deck() we create a nested for loop to run through all the values and colors, and use the append function to add this values, to the deck which is a list of strings. We then run another for loop for the wilds and this allows us to add the 4 wild of each type to the deck as well.

"""We want to be able to shuffle the deck as well, as when we generate the deck, it will be in order. Parameters: deck (list), Return shuffled_deck (list)"""

def shuffle_deck(deck):

    for card_position in range(len(deck)):
        random_position = random.randint(0,107)
        deck[card_position], deck[random_position] = deck[random_position], deck[card_position]
    
    return deck

#this function allows us to take two positions, the card position and the random position, and allows us to switch each card in the list, with another card in a random position in the list 

"""Next we need a function to allow the player to draw cards at the beginning, throughout as well when the player cannot play their turn, parameter is int (number of cards) and it returns cards drawn (list)"""

def draw_cards(num_cards):
    cards_drawn = []
    for i in range(num_cards):
        cards_drawn.append(uno_deck.pop(0))
    
    return cards_drawn

#in this function we start off with an empty list, which we are adding strings to, we then use the append function in conjuntion with the pop function to remove a card from the deck and then add it to cards drawn


