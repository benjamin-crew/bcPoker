from random import shuffle as shuffle

players = 4

# FIXME: Add suits
def get_shuffled_deck():
    """Returns a shuffled deck.
    No suits as of yet."""
    
    deck = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]*4
    shuffle(deck)

    return deck

# FIXME: Think about how to allow users to come and go
#        How to use usernames + accounts etc.
def create_players(num):
    """Creates the amount of players inputted by user."""
    players = {f"player_{i}":1000 for i in range(1,num+1)}

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

print(players_dict)
