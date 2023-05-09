import random 

""" Generate Deck of uno cards which is 180 cards, parameters are none and return value of variable deck --> list"""

# we first start off with a deck that is built and has nothing in it, we know in uno there is both colors and values for each card drawn, we create lists for each, and then we use a for loop to cycle through both and create the full deck, we then add this value to our deck using append method and we do the same thing with the wild cards#

def build_deck():
    deck = []
    colors = ['red','green', 'yellow', 'blue']
    values = [0,1,2,3,4,5,6,7,8, "draw two", "skip", 'reverse']
    wild_cards = ['wild', 'wild draw four']

    for color in colors:
        for value in values:
            card_value = f"{color};{value}"
            deck.append(card_value)
    
    for i in range(4):
        deck.append(wild_cards[0])
        deck.append(wild_cards[1])

    return deck


"""Shuffle deck function that we are building, shuffles a list of item in there, Parameter is a list, that we pass in aka uno_deck, we want to shuffle the order in the deck, we will shuffle using random numbers to shuffle each deck"""

def shuffle_deck(deck):
    for card_position in range(len(deck)):
        random_position = random.randint(0,len(deck)-1)
        deck[card_position], deck[random_position] = deck[random_position], deck[card_position] #swap values#
    return deck
              

"""Draw card function that draws a specified number of cards off the top of the deck Parameters: num_cards --> integer and return cards_drawn --> list, we want to remove the card from the top of the deck, so we use the pop function from top of the deck and returns value """

def draw_cards(num_cards):
    cards_drawn = []
    for x in range(num_cards):
        cards_drawn.append(uno_deck.pop(0))
    return cards_drawn

"""print formatted list of players hand  parameter player --> which will an integer, and then we return none, the player is an integer, and player hand is the list"""

def show_hand(player, player_hand):
    print(f"player {player+1}")
    print(f"Your hand is {player_hand}")
    print('------------')
    y = 1
    for card in player_hand:
        print(f"{y} {card}")
        y += 1 # one is the first card, and it will increase with the bracket of the card#
    print("")

"""if a player can play a card or not, color is a string. value is a string and player hand is a list, and we return a boolean"""

def can_play(color, value, player_hand):
    for card in player_hand:
        if 'wild' in card:
            return True
        elif color in card or value in card:
            return True


#this will assign the uno deck we built to a variable for the deck we have#
uno_deck = build_deck()
uno_deck = shuffle_deck(uno_deck)
uno_deck = shuffle_deck(uno_deck)
discards = []
print(uno_deck)

players = []
number_players = int(input('How many players? '))

while number_players < 2 or number_players > 4:
    number_players = int(input('invalid, please enter a number of players between 2 and 4'))

for player in range(number_players):
    players.append(draw_cards(5))

player_turn = 0
play_direction= 1 #or -1 to reverse direction#
playing = True
discards.append(uno_deck.pop(0))
split_card = discards[0].split(";", 1)
current_color = split_card[0]

if current_color != 'wild':
    card_value = split_card[1]
else:
    card_value = 'any'


while playing:
    show_hand(player_turn, players[player_turn])
    print(f'card on top of discard pile {discards[-1]}')
    if can_play(current_color, card_value, players[player_turn]):
        card_chosen = int(input('what card do you want to play '))
        while not can_play(current_color, card_value,[players[player_turn][card_chosen - 1]]):

            card_chosen = int(input('not a valid card, which card do you want to play'))
        print(f"you played {players[player_turn.pop(card_chosen-1)]}")
        discards.append(players[player_turn].pop(card_chosen-1))
    else:
        print("you can't play, draw a card")
        players[player_turn].extend(draw_cards(1))
    print("")
    player_turn += play_direction

    if player_turn == number_players:
        player_turn = 0
    elif player_turn < 0: 
        player_turn = number_players - 1

