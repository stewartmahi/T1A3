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


"""We need to create a function to print a list of players hand. Parameters are player (int) and their hand (list) and we return Nothing"""

def show_hand(player, player_hand):
    try:
        print(f"Player {player+1} it is your turn")
        print("Your Hand")
        print("-------------------")

        y = 1

        for card in player_hand:
            print(f"{y}) {card}")
            y += 1
        print("")

    except Exception as e:
        print(f"An error occurred: {e}")


#for this function, we print out the players hand, we use +1 in the player parameter, to allow us to have a better user experience. we do the same thing with starting of with y = 1, so that it makes it easier for the player to decide what card they want to pick

"""we need to check if the player can play a card, Parameters color --> string, value --> string, player_hand --> list, Return: Boolean"""

def can_play(color, value, player_hand):
    for card in player_hand:
        if 'Wild' in card:
            return True
        elif color in card or value in card:
            return True
        
    return False

#here we are checking the values, if the player has a wild card, they can play, returning true, and also if they have either color or value they can also play, if not they cannot play

uno_deck = build_deck()
uno_deck = shuffle_deck(uno_deck)
uno_deck = shuffle_deck(uno_deck)
uno_deck = shuffle_deck(uno_deck)

discards = []

#the discard pile is what will be on top, to start off with

players = []
colors = ["Red","Green","Yellow","Blue"]

while True:
    try:
        number_players = int(input("How many players? "))
        if number_players < 2 or number_players > 4:
            raise ValueError
        break
    except ValueError:
        print("Invalid input. Please enter a number between 2 and 4.")

for player in range(number_players):
    players.append(draw_cards(5))

player_turn = 0
play_direction = 1
playing = True
discards.append(uno_deck.pop(0))
split_card = discards[0].split(" ", 1)
current_color = split_card[0]

if current_color != "Wild":
    card_value = split_card[1]

else:
    card_value = "Any"

"""Simulating game environment for playing"""
#tried to add a try/exception but game broke
while playing:
    show_hand(player_turn, players[player_turn])
    print(f"Card on top of the discard pile: {discards[-1]}")

    if can_play(current_color, card_value, players[player_turn]):
        card_chosen = int(input("Which card do you want to play? "))

        while not can_play(current_color, card_value, [players[player_turn][card_chosen-1]]):
            card_chosen = int(input("Not A Valid Card, What Do you Want To Play? "))
        
        print(f"You Played {players[player_turn][card_chosen - 1]}")
        discards.append(players[player_turn].pop(card_chosen - 1))

        #Checking to see if player won

        if len(players[player_turn]) == 0:
            playing = False
            winner = f"Player {player_turn + 1}"
        
        else:
            #check for special cards
            split_card = discards[-1].split(" ", 1)
            current_color = split_card[0]
            if len(split_card) == 1:
                card_value = "Any"
            else:
                card_value = split_card[1]
            
            if current_color == "Wild":
                for x in range(len(colors)):
                    print(f"{x+1}) {colors[x]}")
                new_colour = int(input("what color would you like to choose? "))
                #this allows a player to pick another color
                current_color = colors[new_colour - 1]
            
            if card_value == "Reverse":
                play_direction = play_direction * -1

            elif card_value == "Skip":
                player_turn += play_direction

                if player_turn >= number_players:
                    player_turn = 0
                elif player_turn < 0:
                    player_turn = number_players - 1

                #goes to the next person
            
            elif card_value == "Draw Two":
                player_draw = player_turn + play_direction

                if player_draw == number_players:
                    player_draw = 0
                elif player_draw < 0:
                    player_draw = number_players - 1
                
                players[player_draw].extend(draw_cards(2))

            elif "Draw Four" in card_value:
                player_draw = player_turn + play_direction

                if player_draw == number_players:
                    player_draw = 0
                elif player_draw < 0:
                    player_draw = number_players - 1
                
                players[player_draw].extend(draw_cards(4))
            print("")
    else:
        print("you cannot play, draw a card --> ")
        players[player_turn].extend(draw_cards(1))

    player_turn += play_direction
    if player_turn >= number_players:
        player_turn = 0
    elif player_turn < 0:
        player_turn = number_players - 1 

print("game over")
print(f"{winner} is the winner!")
