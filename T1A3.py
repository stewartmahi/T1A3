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
