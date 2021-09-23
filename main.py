import random

dealer = False


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


def start_game():
    """Main game loop"""
    pass


# Get shuffled deck
deck = get_shuffled_deck()


# Create players
#num_players = int(input("How many players?: 2-6"))
# Set players to 4 for testing
num_players = 4
players_dict = create_players(num_players)
players_dict_to_list = list(players_dict)

# Set ante
small_ante = 0
while small_ante < 50 or small_ante > 200:
    small_ante = int(input("Set the small blind. 50-200: "))
big_ante = small_ante*2


# Choose dealer and blinds
if dealer is False:
    dealer = random.choice(players_dict_to_list)
else:
    dealer = players_dict_to_list[(players_dict_to_list.index(dealer) + 1) % 4]

small_blind_player = players_dict_to_list[(
    players_dict_to_list.index(dealer) + 1) % 4]
big_blind_player = players_dict_to_list[(
    players_dict_to_list.index(dealer) + 2) % 4]

# Deal the hand
for i in range(0, len(players_dict_to_list)):
    player_{i}_hand = []