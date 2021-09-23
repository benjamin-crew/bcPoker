import random
from player import Player

dealer = False

def betting():
    print("Start betting.")

    for i in range(1, num_players+1):
        making_decision = True
        first = players_dict[f"player_{i}"].first_card
        second = players_dict[f"player_{i}"].second_card
        print(f"Player {i}'s hand: {first}, {second}")
        while making_decision is True:
            making_decision = False
            decision = input(str("Call, bet, all-in or fold: ")).lower()
            if decision == "call":
                print("call")
            elif decision == "bet":
                print("How much?: ")
            elif decision == "all-in":
                print("Going all in!")
            elif decision == "fold":
                print(f"Player {i} folds.")
            else:
                print("Invalid decision.")
                making_decision = True


# FIXME: Add suits
def get_shuffled_deck():
    """Returns a shuffled deck.
    No suits as of yet."""

    deck = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]*4
    random.shuffle(deck)

    return(deck)

# FIXME: Think about how to allow users to come and go
#        How to use usernames + accounts etc.
def create_players(num):
    """Creates the amount of players inputted by user."""
    players = {f"player_{i}": 1000 for i in range(1, num+1)}

    return(players)


# def start_game():
#     """Main game loop"""
#     pass


# Get shuffled deck
deck = get_shuffled_deck()


# Create players
#num_players = int(input("How many players?: 2-6"))
# Set players to 4 for testing
num_players = 4

players_dict = {f"player_{i}": Player(money=1000, name=f"player{i}") for i in range(1, num_players+1)}
players_dict_to_list = list(players_dict)

# Set ante - set to 50 for testing
small_ante = 50
# while small_ante < 50 or small_ante > 200:
#     small_ante = int(input("Set the small blind. 50-200: "))
big_ante = small_ante*2


# Choose dealer and blinds
if dealer is False:
    dealer = random.choice(players_dict_to_list)
else:
    dealer = players_dict_to_list[(players_dict_to_list.index(dealer) + 1) % 4]

small_blind_player = players_dict_to_list[(players_dict_to_list.index(dealer) + 1) % 4]
big_blind_player = players_dict_to_list[(players_dict_to_list.index(dealer) + 2) % 4]

# Deal the hand 
# for _ in range(2):
for i in range(1, num_players+1):
    players_dict[f"player_{i}"].first_card = deck.pop(0)
    print(players_dict[f"player_{i}"].first_card)
for i in range(1, num_players+1):
    players_dict[f"player_{i}"].second_card = deck.pop(0)
    print(players_dict[f"player_{i}"].second_card)

betting()