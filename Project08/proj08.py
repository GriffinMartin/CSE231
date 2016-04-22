# ==============================================================================
# Computer Project 8
# ------------------------------------------------------------------------------
# This program builds a dictionary based on a sample database from MSU. The user
# can perform several operations:
#   1) Add by NetID
#   2) Add by name
#   3) Add by NetIDs read from a file (one entry per line)
#   4) Add by names read from a file (one entry per line)
#   5) Display dictionary
#   6) Remove entry from dictionary by NetID
#   7) Write dictionary to file
# Originally, data was supposed to be scrapped from the MSU website.
# ==============================================================================

NETID_LENGTH = 8 # Maximum number of character for NetID
DATABASE_FILE = 'MSU_DB.txt' # File name to save database

# ------------------------------------------------------------------------------
# FUNCTION  query_MSU_online_database(payload)
#   This function replaces the original query_MSU_online_database function.
# That function retrieved information from a web page; this function pretends to
# do the same thing: it takes a payload in the form of a NetID or name and
# returns information about that person.
# ------------------------------------------------------------------------------
def query_MSU_online_database(payload):
    netids = ['hillbob','wangalle','hopperg','wozsteve']
    names = [('Hill','Bob'),('Wang','Allen'),('Hopper','Grace'),('Wozniak','Steve')]

    if ('nid' not in payload) and \
       ('fst' not in payload or 'lst' not in payload):
        raise ValueError

    # Sample database
    samples = [
        {'hillbob' : ['Hill, Bob Fred',
                      '61 Noff Rd Morris, MI 48458',
                      '810-225-8275',
                      '',
                      '',
                      'hillbob@msu.edu',
                      'Student',
                      'Freshman',
                      'Mechanical Engineering']},
        {'wangalle' : ['Wang, Allen',
                       '16 Chandler Rd Apt 123 East Lansing, MI 48823',
                       '714-970-7265',
                       '8106 Adding Dr Walloon Lake, MI 48390',
                       '238-160-3230',
                       'wangalle@msu.edu',
                       'Student',
                       'Sophomore',
                       'Computer Engineering']},
        {'hopperg'  : ['Hopper, Grace',
                       '127 Harrison Rd, East Lansing, MI 48823',
                       '517-123-4567',
                       '27 Main St., South Haven, MI 49090',
                       '269-123-9876',
                       'hopperg@msu.edu',
                       'Student',
                       'Senior',
                       'Mathematics']},
        {'wozsteve' : ['Wozniak, Steve',
                       '345 University Dr., East Lansing, MI 48823',
                       '408-293-2468',
                       '1 Infinite Loop, Cupertino, CA 95015',
                       '408-123-2568',
                       'wozsteve@msu.edu',
                       'Student',
                       'Sophomore',
                       'Computer Engineering']}
                       ]
    result = {}

    # If NetID
    if 'nid' in payload:
        if payload['nid'] in netids:
            result = samples[netids.index(payload['nid'])]
    # Else name
    elif 'fst' in payload and 'lst' in payload:
        if (payload['lst'], payload['fst']) in names:
            result = samples[names.index((payload['lst'], payload['fst']))]

    if not result: # If result is empty
        return result

    ls = list(result.items())
    name = ls[0][0]
    data = ls[0][1]

    # Print information neatly formatted
    print ("-" * 50)
    print("[ + ] Name: {}".format(data[0]))
    print ("-" * 50)
    print("[ + ] Current Address: {}".format(data[1]))
    print("[ + ] Current Phone: {}".format(data[2]))
    print("[ + ] Permanent Address: {}".format(data[3]))
    print("[ + ] Permanent Phone: {}".format(data[4]))
    print("[ + ] Mail ID: {}".format(data[5]))
    print("[ + ] Title: {}".format(data[6]))
    print("[ + ] Status: {}".format(data[7]))
    print("[ + ] Major: {}".format(data[8]))
    print ("-" * 50)

    return result

# ------------------------------------------------------------------------------
# FUNCTION  banner()
#   Displays welcoming banner to the user.
# ------------------------------------------------------------------------------
def banner():
    asciitext = '''
     __  __ ____  _   _   ____  _        _ _
    |  \/  / ___|| | | | / ___|| |_ __ _| | | _____ _ __
    | |\/| \___ \| | | | \___ \| __/ _` | | |/ / _ \ '__|
    | |  | |___) | |_| |  ___) | || (_| | |   <  __/ |
    |_|  |_|____/ \___/  |____/ \__\__,_|_|_|\_\___|_|

      ____           _             _
     / ___|___ _ __ | |_ _ __ __ _| |
    | |   / _ \ '_ \| __| '__/ _` | |
    | |__|  __/ | | | |_| | | (_| | |
     \____\___|_| |_|\__|_|  \__,_|_| CSE 231 - Spring 2016
     '''
    print(asciitext)

# User menu
MENU = '''
  1. NetID
  2. Firstname Lastname
  3. Multiple NetIDs from file
  4. Multiple Firstname Lastname pairs from file
  5. Display dictionary
  6. Remove name from dictionary
  7. Write dictionary
  x. Exit
  '''

masterD = {} # The master dictionary of names collected

# ------------------------------------------------------------------------------
# FUNCTION  netid_query()
#   Forms a query based on NetID and add info to the master dictionary if it
# can be found.
# ------------------------------------------------------------------------------
def netid_query(masterD, netid):
    payload = {'nid':netid}
    D = query_MSU_online_database(payload)
    masterD[netid] = D

# ------------------------------------------------------------------------------
# FUNCTION  fstlst_query()
#   Forms a query based on first and last name and add info to the master
# dictionary if it can be found.
# ------------------------------------------------------------------------------
def fstlst_query(masterD, fst, lst):
    payload = {'fst': fst, 'lst': lst}
    D = query_MSU_online_database(payload)
    if (D == {}): # If cannot find NetID, return -1
        return -1
    else: # Else return corresponding NetID
        netid = list(D.keys())[0]
        masterD[netid] = D
        return netid

# ------------------------------------------------------------------------------
# FUNCTION  search_by_id()
#   Displays information matching NetID (if it exists) and add it to master
# dictionary. Inform user if ID format is invalid or if no match is found.
# ------------------------------------------------------------------------------
def search_by_id():
    prompt = 'Enter NetID: '
    given_netid = input(prompt) # Prompt user for ID
    while (given_netid != ''):
        if (len(given_netid) > NETID_LENGTH): # Verify if format is valid
            print('Invalid NetID. Please try again.') 
            given_netid = input(prompt) # Ask for another ID
        netid_query(masterD, given_netid) # Try to match ID with user
        if (masterD[given_netid] == {}): # If it's not possible
            print('NetID not found. Please try again.') 
            del masterD[given_netid] # Delete empty entry from dictionary
            given_netid = input(prompt) # Ask for another key
        else: 
            break
    print(MENU)

# ------------------------------------------------------------------------------
# FUNCTION  search_by_name()
#   Displays information matching first and last name (if it exists) and add it
# to master dictionary. Inform user if name format is invalid or if no match is
# found.
# ------------------------------------------------------------------------------
def search_by_name():
    prompt = 'Enter first and last name: '
    fst_lst = input(prompt) # Prompt user for first and last names
    while (fst_lst != ''):
        name = fst_lst.split() # Try to split into First and Last
        if (len(name) != 2): # If it doesn't match this exact format, inform user
            print('Invalid format. Names must be of the form First Last.')
            fst_lst = input(prompt) # Ask for another name
            continue
        netid = fstlst_query(masterD, name[0], name[1]) # Try to get matching ID
        if (netid == -1): # If ID doesn't exist
            print('User not found. Please try again.') 
            fst_lst = input(prompt) # Ask for another name
        else:
            break 
    print(MENU) 

# ------------------------------------------------------------------------------
# FUNCTION  search_by_file_ids()
#   Displays information matching NetIDs in filename (if it exists) and add them
# to master dictionary. NetIDs in file need to be on a separate line. Invalid
# NetIDs will simply be discarded.
# ------------------------------------------------------------------------------
def search_by_file_ids():
    prompt = 'Enter a file name with NetIDs: '
    filename = input(prompt) # Prompt user for file name
    while (filename != ''):
        try: # Attempt to open file
            fp = open(filename, 'r')
        except: # If file doesn't exist
            print('File not found. Please try again.') # Inform user
            filename = input(prompt) # Ask for another file name
            continue
        netids = fp.read().splitlines() # Get all IDs into list
        for netid in netids: # Loop through them
            netid_query(masterD, netid) # Attempt to match them with database
            if (masterD[netid] == {}): # If it's not possible
                del masterD[netid] # Delete empty entry from dictionary
        break
    print(MENU) 

# ------------------------------------------------------------------------------
# FUNCTION  search_by_file_ids()
#   Displays information matching names in filename (if it exists) and add them
# to master dictionary. Names in file need to be on a separate line. Invalid
# names will simply be discarded.
# ------------------------------------------------------------------------------
def search_by_file_names():
    prompt = 'Enter a file name with first and last names: '
    filename = input(prompt) # Prompt user for file name
    while (filename != ''):
        try: # Attempt to open file
            fp = open(filename, 'r')
        except: # If file doesn't exist
            print('File not found. Please try again.') # Inform user
            filename = input(prompt) # Ask for another file name
            continue
        raw_names = fp.read().splitlines() # Get all names into list
        names = [] # Create list of first and last names
        for fst_lst in raw_names: # For each entry
            name = fst_lst.split() # Split them as first and last
            if (len(name) != 2): # If the format doesn't match
                break # Discard entry
            names.append(name) # Otherwise put them into list of names
        for name in names: # For each name in file
            netid = fstlst_query(masterD, name[0], name[1]) # Match their ID
            if (netid == -1): # If it's not possible
                break # Discard entry as well
        break
    print(MENU) # Shows menu to user

# ------------------------------------------------------------------------------
# FUNCTION  display_dict()
#   Display the current dictionary to the user. If the dictionary is empty, a
# message is shown to the user.
# ------------------------------------------------------------------------------
def display_dict():
    if len(list(masterD.keys())) == 0: # Check if current dictionary is empty
        print('Dictionary is currently empty.') 
    else:
        for netid in list(masterD.keys()): # Otherwise display all entry
            netid_query(masterD, netid) # one after the other
    print(MENU) 

# ------------------------------------------------------------------------------
# FUNCTION  remove_from_dict()
#   Deletes key from current dictionary. If NetID cannot be matched in the
# database, a message is shown to the user.
# ------------------------------------------------------------------------------
def remove_from_dict():
    prompt = 'Enter a NetID to remove: '
    given_netid = input(prompt) # Prompt the user for ID
    while (given_netid != ''):
        try: # Attempt to delete it from dictionary if it's in there
            del masterD[given_netid]
        except: 
            print('NetID not found. Please try again.')
            given_netid = input(prompt) # Prompt user for another ID
            continue
        print('Key successfully removed!')
        break
    print(MENU) # Shows menu to user

# ------------------------------------------------------------------------------
# FUNCTION  write_dictionary()
#   Saves the current dictionary to DATABASE_FILE. 
# ------------------------------------------------------------------------------
def write_dictionary():
    with open('MSU_DB.txt', 'w') as f: # Save dictionary
        f.write(str(masterD))
    print('File successfully written!') # Inform user the write was a success

# ------------------------------------------------------------------------------
# MAIN PROGRAM STARTS HERE
# ------------------------------------------------------------------------------
def main():
    banner() # Print the banner
    print(MENU) # Show menu to the user
    cmd = input('Choose a command: ') # Ask a first command

    while (cmd != 'x'): # Constantly ask for a command until user presses exit
        if (cmd == '1'):
            search_by_id()
            cmd = input('Choose a command: ')
            continue
        if (cmd == '2'):
            search_by_name()
            cmd = input('Choose a command: ')
            continue
        if (cmd == '3'):
            search_by_file_ids()
            cmd = input('Choose a command: ')
            continue
        if (cmd == '4'):
            search_by_file_names()
            cmd = input('Choose a command: ')
            continue
        if (cmd == '5'):
            display_dict()
            cmd = input('Choose a command: ')
            continue
        if (cmd == '6'):
            remove_from_dict()
            cmd = input('Choose a command: ')
            continue
        if (cmd == '7'):
            write_dictionary()
            cmd = input('Choose a command: ')
            continue
        else:
            print('Invalid command. Please try again.\n')
            cmd = input('Choose a command: ')

main() # Run program
