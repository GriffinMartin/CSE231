import cards

# ------------------------------------------------------------------------------
# Computer Project 10
# ------------------------------------------------------------------------------
# This program implements the game of Alaska solitaire. The user has 5 options:
#   - Restart the game with new cards (R)
#   - See choice options (H)
#   - Move a tableau card to a foundation pile (F x y)
#   - Move a tableau sub-pile of size c to another tableau pile (T x y c)
# ==============================================================================

RULES = '''
Alaska Card Game:
     Foundation: Columns are numbered 1, 2, 3, 4
                 Built up by rank and by suit from Ace to King.
                 The top card may be moved.
     Tableau: Columns are numbered 1,2,3,4,5,6,7
              Built up or down by rank and by suit.
              The top card may be moved.
              Complete or partial face-up piles may be moved.
              An empty spot may be filled with a King or a pile starting with a King.
     To win, all cards must be in the Foundation.'''

MENU = '''
Input options:
    F x y : Move card from Tableau column x to Foundation y.
    T x y c: Move pile of length c >= 1 from Tableau column x to Tableau column y.
    R: Restart the game (after shuffling)
    H: Display the menu of choices
    Q: Quit the game
'''

FNDTN_TEMPLATE = '┃{:>4s}{:>5s}{:>5s}{:>5s}  │  Moves: {:>3d}  ┃'
TAB_TEMPLATE = '┃{:>4s}{:>5s}{:>5s}{:>5s}{:>5s}{:>5s}{:>5s}  ┃'
FRAME_TOP = '\n┏' + '━' * 21 + '┯' + '━' * 14 + '┓'
FRAME_MID = '┠' + '─' * 21 + '┴' + '─' * 14 + '┨'
FRAME_BOT = '┗' + '━' * 36 + '┛'

WIN_CASTLE = '''
                 .
                 │ZZzzz
                 │
    .            │            .
    │ZZzzz      /^\           │ZZzzz
    │          |~~~|          │
    │        ┌^^^^^^^┐       /^\\
   /^\       │[]+    │      │~~~│
┌^^^^^^^┐    │    +[]│      │   │
│    +[]│/\/\/\/\=/\/\/\/\┌^^^^^^^┐
│+[]+   ├~~~~~~~~~~~~~~~~~┤    +[]│
│       │  []   /^\   []  │+[]+   │
│   +[]+│  []  ╭───╮  []  │   +[]+│
│[]+    │  xx  │o  │  xx  │[]+    │
┕━━━━━━━┷━━┷┷━━┷━━━┷━━┷┷━━┷━━━━━━━┙
'''

# ------------------------------------------------------------------------------
# FUNCTION  valid_move(c1, c2)
#   Returns True if suits are the same and ranks differ by 1; c1 & c2 are cards.
# ------------------------------------------------------------------------------
def valid_move(c1, c2):
    return (c1.suit() == c2.suit() and abs(c1.rank() - c2.rank()) == 1)

# ------------------------------------------------------------------------------
# FUNCTION  tableau_move(tableau, x, y, c)
#   Moves pile of length c >= 1 from Tableau column x to Tableau column y.
# Returns True if successful.
# ------------------------------------------------------------------------------
def tableau_move(tableau, x, y, c):
    # Error checking for given inputs
    try: # Valid types
        x, y, c = int(x), int(y), int(c)
    except:
        print('Error! Incorrect type of arguments.')
        return False
    # Valid values
    if (x not in range(1, 8) or y not in range(1, 8) or c < 1):
        print('Error! Incorrect parameter values.')
        return False

    # Decrement to index at 0
    x -= 1
    y -= 1
    src, dst = tableau[x], tableau[y]

    if (src == []): # No cards to move
        print('Error! No cards to move.\n')
        return False
    elif (len(src) < c): # Not enough cards to move
        print('Error! Not enough cards to move.\n')
        return False
    else: # Enough cards, but need to check if top card is facing up
        pile = tableau[x][-c:]
        go_card = pile[0]
        to_card = [] if dst == [] else dst[-1]
        if (not go_card.is_face_up()):
            print('Error! Trying to move undisclosed cards.')
            return False

    if (to_card == [] and go_card.rank() == 13):
        del tableau[x][-c:]
        tableau[y] += pile
        disclose_card(tableau, x)
        return True

    # Initial logic test passed, now check if legal game move
    if (valid_move(go_card, to_card)):
        del tableau[x][-c:]
        tableau[y] += pile
        disclose_card(tableau, x)
        return True

    # Invalid move
    else:
        print('Error! Move not allowed.')
        return False

# ------------------------------------------------------------------------------
# FUNCTION  disclose_card(tableau, x)
#   Discloses (flips) new card if it's the last in a column and it's face down.
# ------------------------------------------------------------------------------
def disclose_card(tableau, x):
    src = tableau[x] # Get tableau column
    t_card = [] if src == [] else src[-1] # Get card
    if (t_card == []): # If no card in column, nothing to do
        return False
    else:
        if (not t_card.is_face_up()): # Else check card is face up
            tableau[x][-1].flip_card() # If not, flip it
        return True

# ------------------------------------------------------------------------------
# FUNCTION  foundation_move(tableau, foundation, x, y)
#   Moves card from Tableau x to Foundation y. Return Trues if successful.
# ------------------------------------------------------------------------------
def foundation_move(tableau, foundation, x, y):
    try: # Validate types
        x, y = int(x), int(y)
    except:
        print('Error! Incorrect type of arguments.')
        return False

    x, y = x - 1, y - 1 # Decrement to index at 0, so tableau[0] is column 1
    if (x not in range(8) or y not in range(4)): # Validate values
        print('Error! Incorrect parameter values.')
        return False

    src, dst = tableau[x], foundation[y] # Get source and destination piles
    if (src == []): # No cards to move
        print('Error! No cards to move.\n')
        return False

    t_card = src[-1] # Get tableau card
    f_card = [] if dst == [] else dst[-1] # Get foundation card

    # Base case
    if (f_card == []): # If foundation pile is empty
        if (t_card.rank() == 1): # And card to move is an Ace
            foundation[y].append(tableau[x].pop()) # Move it to foundation
            disclose_card(tableau, x) # Disclose new card if necessary
            return True
        else:
            print('Error! Move not allowed.')
            return False

    # General case
    elif (t_card.suit() == f_card.suit() and t_card.rank() == f_card.rank() + 1):
        foundation[y].append(tableau[x].pop()) # Move it to foundation
        disclose_card(tableau, x) # Disclose new card if necessary
        return True

    else:
        print('Error! Move not allowed.')
        return False

# ------------------------------------------------------------------------------
# FUNCTION  win(tableau, foundation)
#   Returns True if the game is won, i.e. if all foundation piles are full.
# ------------------------------------------------------------------------------
def win(tableau, foundation):
    return (sum(map(len, foundation)) == 52)

# ------------------------------------------------------------------------------
# FUNCTION  init_game()
#   Initializes and returns the tableau, and foundation.
#     - foundation is a list of 4 empty lists
#     - tableau is a list of 7 lists
#     - deck is shuffled and then all cards dealt to the tableau
# ------------------------------------------------------------------------------
def init_game():
    deck = cards.Deck() # Create new card deck
    deck.shuffle() # Shuffle it; uncomment for testing
    tableau = [[deck.deal()]] # Deal first card
    for i in range(6, 12): # For the remaining 6 columns
        stack = [] # Create empty stack
        for j in range(i): # Deal appropriate number of cards
            card = deck.deal()
            if i - j > 5: # Flip card according to Alaska's rules
                card.flip_card()
            stack.append(card) # Add card to stack
        tableau.append(stack) # Add stack to tableau

    foundation = [[] for _ in range(4)] # Initialize foundation with empty piles
    return tableau, foundation

# ------------------------------------------------------------------------------
# FUNCTION  display_game(tableau, foundation ,moves)
#   Displays foundation with tableau below. Formats as described in specs.
# Also shows the number of moves so far.
# ------------------------------------------------------------------------------
def display_game(tableau, foundation, moves):
    max_col = max(map(len, tableau)) # Get number of rows to display
    matrix = [] # Initialize empty matrix
    for col in tableau: # Extend current tableau to square matrix by padding
        new_col = list(col) # with empty strings ''
        col_size = len(new_col)
        if col_size < max_col:
            new_col.extend(['' for _ in range(max_col - col_size)])
        matrix.append(new_col)
    transposed = list(map(list, zip(*matrix))) # Transpose matrix
    # Computations done, now we print
    print(FRAME_TOP)
    # Get top card in each foundation pile
    found = ['' if p == [] else str(p[-1]) for p in foundation]
    if (moves > 999): # Print 999 if # of moves exceeds 999
        moves = 999
    found.append(moves)
    print(FNDTN_TEMPLATE.format(*found))
    print(FRAME_MID)
    for row in transposed: # Print tableau
        line = tuple(map(str, row)) # Convert each line to a string
        print(TAB_TEMPLATE.format(*line)) # Print row
    print(FRAME_BOT)

# ------------------------------------------------------------------------------
# MAIN PROGRAM STARTS HERE
# ------------------------------------------------------------------------------
print(RULES) # Print game rules
print(MENU) # Print menu once
tableau, foundation = init_game() # Initialize game
moves = 0 # Set number of moves to zero
display_game(tableau, foundation, moves) # Display game to user
choice = input("\nEnter a choice: ") # Ask for input
choice = choice.split() # Split input by spaces
while (len(choice) == 0): # If no input was provided, ask user again
    print('Error! Please enter a command.')
    choice = input("\nEnter a choice: ")
    choice = choice.split()

while (choice[0].lower() != 'q'):
    # Restart game
    if (len(choice) == 1 and choice[0].lower() == 'r'):
        moves = 0 # Restart number of moves
        print('\nRestarting game...')
        tableau, foundation = init_game() # Restart game
    # Move from tableau to foundation
    elif (len(choice) == 1 and choice[0].lower() == 'h'):
        print(MENU) # Print menu again
    elif (choice[0].lower() == 'f'):
        if (len(choice) == 3):
            x, y = choice[1], choice[2]
            if (foundation_move(tableau, foundation, x, y)):
                moves += 1 # Increment number of moves (if valid)
        else:
            print('Error! Incorrect number of arguments.')
    # Move from tableau to tableau
    elif (choice[0].lower() == 't'):
        if (len(choice) == 4):
            x, y, c = choice[1], choice[2], choice[3]
            if (tableau_move(tableau, x, y, c)):
                moves += 1 # Increment number of moves (if valid)
        else:
            print('Error! Incorrect number of arguments.')
    else:
        print('Error! Incorrect command.')

    display_game(tableau, foundation, moves)
    # Check for a winning configuration
    if win(tableau, foundation):
        print(WIN_CASTLE) # Print awesome castle
        print('Congratulations! You won in ' + str(moves) + ' moves!')
        print(MENU)
    # Prompt user for new command
    choice = input("\nEnter a choice: ")
    while (len(choice) == 0):
        print('Error! Please enter a command.')
        choice = input("\nEnter a choice: ")
    choice = choice.split()