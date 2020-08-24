"""Assignment for session 6 based on first class functions part 1"""

# Rules for the game.
rule_book = {1: {'ace-hearts','king-hearts','queen-hearts','jack-hearts', '10-hearts'}    # Royal Flush
            ,2: {'10-clubs','9-clubs','8-clubs','7-clubs', '6-clubs'}                     # Straight Flush
            ,3: {'queen-clubs','queen-hearts','queen-spades','queen-diamonds', '5-clubs'} # Four of a Kind
            ,4: {'ace-hearts','ace-spades','ace-diamonds','king-spades', 'king-hearts'}   # Full House
            ,5: {'king-hearts','8-hearts','6-hearts','4-hearts', '2-hearts'}              # Flush
            ,6: {'8-hearts','7-clubs','6-diamonds','5-spades', '4-hearts'}                # Straight
            ,7: {'queen-clubs','queen-hearts','queen-spades','7-hearts', '2-clubs'}       # Three of a Kind
            ,8: {'jack-diamonds','jack-hearts','9-spades','9-diamonds', '5-clubs'}        # Two Pair
            ,9: {'king-hearts','king-spades','9-diamonds','8-spades', '4-hearts'}         # One Pair
            ,10: {'ace-hearts','queen-clubs','6-hearts','4-spades', '2-diamonds'}         # High Card
            }

# Setting up global variables
vals = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'jack', 'queen', 'king', 'ace']
suits = ['spades', 'clubs', 'hearts', 'diamonds']

# TODO: Implement single expression that includes lambda, zip and map functions to select create 52 cards in a deck - 50 pts
# Return a deck of 52 cards using the vals and suits
deck_of_cards = sorted(list(map(lambda x : x[1]+'-'+x[0], zip(suits*len(vals),vals*len(suits)))))


# TODO: Implement normal function without using lambda, zip, and map function to create 52 cards in a deck
# Return a deck of 52 cards using the vals and suits
def prep_deck(vals_lst: list = vals, suits_lst: list = suits) -> list:
    """Takes list of faces of cards and suits and returns a deck of 52 cards
    Inputs:
        vals_lst: list of values of faces of p1_cards
        suits_lst: list of suits
    Returns:
        deck: list of all 52 cards in a deck"""

    ##### Validations #####
    if sorted(vals_lst) != sorted(vals):
        raise ValueError(f"Incorrect list of faces of cards ")
    if sorted(suits_lst) != sorted(suits):
        raise ValueError(f"Incorrect list of suits of cards ")

    deck = []
    for value in vals_lst:
        for suit in suits_lst:
            deck.append(value+'-'+suit)

    return sorted(deck)


# TODO: Implement normal function without using lambda, zip, and map function to create 52 cards in a deck
# Return a deck of 52 cards using the vals and suits
def decide_winner(player_1_cards: list, player_2_cards: list ) -> str:
    """Compares the cards with the list of ranked group of cards from
    the rule_book as per the rules of the game. Decide the result based
    on who's cards matches with the higher rank cards.
    If none of the players cards are matched, results winner as none.
    Inputs:
        player_1_cards: list of cards from first Player
        player_2_cards: list of cards from second Player
    Returns:
        The winner of game or None in case no one wins
    """
    p1_cards=set(player_1_cards)
    p2_cards=set(player_2_cards)
    p1_rank = 0
    p2_rank = 0
    deck = sorted(list(map(lambda x : x[1]+'-'+x[0], zip(suits*len(vals),vals*len(suits)))))

    ##### Validations #####
    if not p1_cards.issubset(deck):
        raise ValueError(f"Player 1 cards are not valid")
    if not p2_cards.issubset(deck):
        raise ValueError(f"Player 2 cards are not valid")
    if p1_cards & p2_cards:
        raise ValueError(f"Both sets of cards are not from same deck")
    if not 2<len(p1_cards)<6:
        raise ValueError(f"Player 1 gave {len(p1_cards)}, Only sets of 3 or 4 or 5 cards allowed")
    if not 2<len(p2_cards)<6:
        raise ValueError(f"Player 2 gave {len(p2_cards)}, Only sets of 3 or 4 or 5 cards allowed")
    if len(p1_cards) != len(player_1_cards):
        raise ValueError(f"Player1 is using same card multiple times")
    if len(p2_cards) != len(player_2_cards):
        raise ValueError(f"Player2 is using same card multiple times")
    if len(p1_cards) != len(p2_cards):
        raise ValueError(f"Both players should use same number of cards")

    # Select winner
    for i in range(1,11):
        # Get rules from rule book and match it with players cards
        player1_match = p1_cards.issubset(rule_book[i])
        player2_match = p2_cards.issubset(rule_book[i])

        if player1_match and not player2_match: # Player 1 cards didn't match but Player 2 matched
            p1_rank = i
        elif player2_match and not player1_match: # Player 2 cards didn't match but Player 1 matched
            p2_rank = i
        elif player1_match and player2_match: # Both players cards didn't match
            continue
        elif p1_rank and (p1_rank == p2_rank): # Both players cards matched
            return('Tie')

    if p1_rank == 0 and p2_rank == 0:
        return('None') # None of the player's cards mathched and no one won
    elif p1_rank == 0 and p2_rank != 0: # Only P2 matched
        return("Player 2 won, Player 1 cards didn't match the cards")
    elif p2_rank == 0 and p1_rank != 0: # Only P1 matched
        return("Player 1 won, Player 2 cards didn't match the cards")
    elif p1_rank < p2_rank: # P1 has better rank
        return('Player 1')
    elif p2_rank < p1_rank: # P2 has better rank
        return('Player 2')
