import sys

###########################################################
# Computer Project 4
# Text Editor - This program asks the user a command to
# edit a piece of text. It works as follows:
# Show MENU and prompt user for command
# While command entered is not exit
#    Perform task on string
#    Display resulting string after operation
#    Prompt user for another command
###########################################################

# Here is the MENU so you don't have to type it in.
MENU = '''
--------------------------------------
Commands available:
    'n': Move to next word
    'p': Move to previous word
    'i': Insert a word
    'e': Erase current word
    'r': Replace current word
    'c': Cut word, move to copy buffer
    'v': Paste word from copy buffer to before current word
    'l': Load a string
--------------------------------------
'''

# Print MENU
print(MENU)
prev, cur, next, buffer = '', '', '', ''
# Prompt user for a command
cmd = input('Enter a command (h for MENU; q to quit): ')
# Keep prompting user for new commands / run text editor
while (cmd != 'q'):
    # Print help
    if (cmd == 'h'):
        print(MENU)
    # Load a new string
    elif (cmd == 'l'):
        inputStr = input('Input a string: ')
        prev = ''
        cur = inputStr[:inputStr.find(' ')]
        next = inputStr[inputStr.find(' '):][1:]
        print('[ ' + prev + ' ] ' + '[ ' + cur + ' ] ' + '[ ' + next + ' ]')
    # Insert a word
    elif (cmd == 'i'):
        prev = input('Input input string: ')
        print('[ ' + prev + ' ] ' + '[ ' + cur + ' ] ' + '[ ' + next + ' ]')
    # Replace current word
    elif (cmd == 'r'):
        cur = input('Input input string: ')
        print('[ ' + prev + ' ] ' + '[ ' + cur + ' ] ' + '[ ' + next + ' ]')
    # Erase current word
    elif (cmd == 'e'):
        cur = next[:next.find(' ')]
        next = next[next.find(' '):][1:]
        print('[ ' + prev + ' ] ' + '[ ' + cur + ' ] ' + '[ ' + next + ' ]')
    # Cut current word and copy it to buffer
    elif (cmd == 'c'):
        buffer = cur
        if (next.find(' ') < 0):
            cur = next
            next = ''
        else:
            cur = next[:next.find(' ')]
            next = next[next.find(' '):]
        print('[ ' + prev + ' ] ' + '[ ' + cur + ' ] ' + '[ ' + next + ' ]')
    # Paste word from copy buffer
    elif (cmd == 'v'):
        if (prev == ''):
            prev = buffer
        else:
            prev = prev + ' ' + buffer
        print(prev, cur, next)
    # Move to next word
    elif (cmd == 'n'):
        if (prev != ''):
            if (cur != ''):
                prev = prev + ' ' + cur
        else:
            prev = cur
        if (next.find(' ') < 0):
            cur = next
            next = ''
        else:
            cur = next[:next.find(' ')]
            next = next[next.find(' '):][1:]
        print('[ ' + prev + ' ] ' + '[ ' + cur + ' ] ' + '[ ' + next + ' ]')
    # Move to previous word
    elif (cmd == 'p'):
        if (cur != ''):
            if (next == ''):
                next = cur
            else:
                next = cur + ' ' + next
        if (prev.find(' ') < 0):
            cur = prev
            prev = ''
        else:
            cur = prev[prev.rfind(' '):][1:]
            prev = prev[:prev.rfind(' ')]
        print('[ ' + prev + ' ] ' + '[ ' + cur + ' ] ' + '[ ' + next + ' ]')
    else:
        print('Invalid command, try again.')

    # Promt user for new command
    cmd = input('Enter a command (h for MENU; q to quit): ')

if (cmd == 'q'):
    sys.exit()
