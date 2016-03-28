###########################################################
# Computer Project 6
# Transposable Integers - This programs prompts the user for
# a file name containing a range (start and end) to work
# with. For each integer in that range, it checks if it is
# transposable (with and without a leading zero). If so,
# it prints the number, its multiplier and the transposable
# product.
###########################################################
def rotate(s):
    return s[-1] + s[:-1] #slicing

#takes two strings and rotates string1, returns true is s1=s2
def is_transpose(string1, string2):
    for s in range(len(string1)):
        string1 = rotate(string1)
        if string1 == string2:
            return True
    return False
#checks transposability by calling is_transpose
def get_transposability(number):
    for i in range(2, 10):
        number_multiply = number * i
        if is_transpose(str(number), str(number_multiply)):
            print(number, '*', i, '=', number_multiply)

def get_transposability_zero(number):
    number_padded = '0' + str(number)
    for i in range(2, 10):
        number_multiply = number * i
        if is_transpose(str(number_multiply), number_padded):
            print(number_padded, '*', i, '=', number_multiply)
#prompts for file input
def open_file():
    filename = input('\nEnter a file name: ')
    try:
        return open(filename, 'r')
    except:
        print('File not found, try again.')
        open_file()
#calls open_file, extractsd values and runs functions
def process_file():
    fp = open_file()
    line = fp.readlines()[1].split()
    start, end = int(line[0]), int(line[1])
    print('\nTransposed numbers from ', start, ' to ', end, '\n')

    for i in range(start, end):
        get_transposability(i)
        get_transposability_zero(i)
#runs process_file
def main():
    process_file()
