# EPAI Session 6 Assignment by Sachin Dangayach

This assignment is based on the concepts of "# First Class Functions Part I". We have created 2 different functions and used combination of map, zip and lambda functions. session6.py contains the code for these functions and test_session6.py file contains the various tests for these functions.

# Rules for winner-
I am not aware of poker rules and I am not sure we need to consider the combinations of suits. I am considering the snapshot given in assignment as the rule to win and the order is again in same way as mentioned in the assignment. Hence to get the royal flush, one has to get   'ace-hearts','king-hearts','queen-hearts','jack-hearts', '10-hearts' only.
## Rules for the game.
Rule book: Ranks are in order from top to down. Rank 1 is best and a player getting lower rank like 1 will be winner in comparison to a player with higher ranks
1: {'ace-hearts','king-hearts','queen-hearts','jack-hearts', '10-hearts'} # Royal Flush
2: {'10-clubs','9-clubs','8-clubs','7-clubs', '6-clubs'}  # Straight Flush
3: {'queen-clubs','queen-hearts','queen-spades','queen-diamonds', '5-clubs'} # Four of a Kind
4: {'ace-hearts','ace-spades','ace-diamonds','king-spades', 'king-hearts'}   # Full House
5: {'king-hearts','8-hearts','6-hearts','4-hearts', '2-hearts'} # Flush
6: {'8-hearts','7-clubs','6-diamonds','5-spades', '4-hearts'}  # Straight
7: {'queen-clubs','queen-hearts','queen-spades','7-hearts', '2-clubs'} # Three of a Kind
8: {'jack-diamonds','jack-hearts','9-spades','9-diamonds', '5-clubs'} # Two Pair
9: {'king-hearts','king-spades','9-diamonds','8-spades', '4-hearts'} # One Pair
10: {'ace-hearts','queen-clubs','6-hearts','4-spades', '2-diamonds'} # High Card

# Below are key functions in session6.py file.

### 1. Use of map, zip and lambda function to prepare a deck of cards
We have used list of values and suits to generate a pack of cards by the help of map, zip and lambda functions.

### 2. prep_deck
This function returns a deck of cards (52 cards) as a list.  IT takes list of faces of cards and suits and returns a deck of 52 cards
    Inputs:
        vals_lst: list of values of faces of p1_cards
        suits_lst: list of suits
    Returns:
        deck: list of all 52 cards in a deck
### 3. decide_winner
This function compares the cards with the list of ranked group of cards from the rule_book as per the rules of the game. Decides the result based on who's cards matches with the higher rank cards. If none of the players cards are matched, results winner as none.
    Inputs:
        player_1_cards: list of cards from first Player
        player_2_cards: list of cards from second Player
    Returns:
        The winner of game or None in case no one wins

# Below are test cases functions in test_session6.py file.

## 1. test_readme_exists :
Test for readme exists

## 2. test_readme_contents :
Test for readme contents are mor than 500 words

## 3. test_readme_proper_description :
Test for all important functions/class described well in your README.md file

## 4. test_readme_file_for_formatting :
Test for readme formatting

## 5. test_indentations :
Test for source code formatting. No tabs but four spaces are used for indentation

## 6. test_function_name_had_cap_letters :
Test for no function is with capitals in source code

## 7. test_deck_by_lambda:
Test time it by calling print multiple times and a non zero avg time for function calls is received

## 8. test_prep_deck_output :
Test deck generated by prep_deck by comparing it against a manually generated deck

## 9. test_prep_deck_input_values :
Test prep_deck and throw error in case of incorrect arguments  are passed

## 10. test_prep_deck_doc_string :
Test and throw error in case doc string is missing for prep_deck function

## 11. test_decide_winner_doc_string :
Test for annotations string for decide_winner function

## 12. test_test_decide_winner_annotations :
Test and throw error in case doc string is missing decide_winner function

## 13. test_decide_winner_incorrect_players_cards :
Check for the valid cards are provided by players

## 14. test_decide_winner_only_one_deck :
Check for the cards from both players are from same deck and hence there can't be any repetition of card

## 15. test_decide_winner_number_of_cards :
Check for the cards from both players are more than 2 and less than 6

## 16. test_decide_winner_same_cards_by_player :
Check for a player can't use same cards multiple times in one game

## 17. test_decide_winner_same_num_of_cards_by_players :
Check for both player are using same number of cards in one game

## 18. test_decide_winner_3cards:
Check for the winner and show the winner, 3 cards as input

## 19. test_decide_winner_4cards:
Check for the winner and show the winner, 4 cards as input

## 20. test_decide_winner_5cards:
Check for the winner and show the winner, 5 cards as input

## 21. test_decide_winner_no_one_wins :
Check for none of the player won

## 22. test_decide_solitary_winner :
Check for the case when only one players cards matched and that player won while the other players card didn't match
