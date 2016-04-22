import pylab

###########################################################
# Computer Project 7
# The program promps the user for a year between 1990 
# and 2014
#   Returns average income for year input
#   Returns median income for year input
#   Displays graph for income
#   Prompts for range or percent of income
###########################################################

MIN_YEAR = 1990
MAX_YEAR = 2014
PLOT_RANGE = 40

def open_file():
    prompt = 'Enter a year where ' + str(MIN_YEAR) + ' <= year <= ' + str(MAX_YEAR) + ': ' 
    year = int(input(prompt))
    if (year in range(MIN_YEAR, MAX_YEAR + 1)):
        filename = 'year' + str(year) + '.txt'
        try:
            return [open(filename, 'r'), year] # Return file pointer and year
        except:
            print('Error in file name: ' + filename + '. Please try again.\n')
            open_file()
    else:
        print('Error in year. Please try again.\n')
        open_file()

def read_file():
    [fp, year] = open_file() # Open file
    data_list = [] # Initialize data structure
    for line in fp: # Loop through each line of the file
        line = line.split() # Split by spaces
        line.pop(1) # Remove hyphen for range
        data_list.append(line) # Add to data structure
    data_list = data_list[2:len(data_list)] # Remove header and return list
    data_list[len(data_list) - 1][1] = '-1'
    for line in data_list: # Convert each entry to numbers
        for i in range(7):
            line[i] = line[i].replace(',', '')
            if i in [2, 3]:
                line[i] = int(line[i])
            else:
                line[i] = float(line[i])
    data_list[len(data_list) - 1][1] = float('Inf') # Replace 'over' by infinity
    return [data_list, year] # Return data structure and year

def get_range(data_list, percent):
    for line in data_list: 
        if line[4] >= percent: # Check percentage is >= to percent
            return ([line[0], line[1]], line[4], line[6]) # Return tuple

def get_percent(data_list, income):
    for line in data_list: 
        if income in range(int(line[0]), int(line[1]) + 1): # Check if income is in range
            return ([line[0], line[1]], line[4], line[6]) # Return tuple

def find_average(data_list):
    num = sum(line[5] for line in data_list) # Sum all entries for total salary
    denum = data_list[len(data_list) - 1][3] # Get total number of individuals
    average = int(num / denum) 
    average = '{:,}'.format(average) # Format with ','
    return average

def find_median(data_list):
    for line in data_list: 
        if line[4] < 50: # Find values (closest below and above 50)
            bot = line
        else:
            top = line
            break
    if abs(bot[4] - 50) < abs(top[4] - 50): # Check which one is closest to 50
        return '{:,}'.format(bot[6])
    else:
        return '{:,}'.format(top[6])

def do_plot(x_vals, y_vals, year):
    pylab.xlabel('Income')
    pylab.ylabel('Cumulative Percent')
    title = 'Cumulative Percent for Income in ' + str(year)
    pylab.title(title)
    pylab.plot(x_vals, y_vals)
    pylab.show()

# Main program starts here
def main():
    [data_list, year] = read_file()
    print('\nFor the year ' + str(year) + ':')
    avg = find_average(data_list) # Get average
    med = find_median(data_list) # Get median
    print('The average income was $' + str(avg))
    print('The median income was $' + str(med) + '\n')

    x_vals = [line[0] for line in data_list][:PLOT_RANGE] # Fetch x values
    y_vals = [line[4] for line in data_list][:PLOT_RANGE] # Fetch y values
    do_plot(x_vals, y_vals, year)

    cmd = input('Enter a choice to get (r)ange, (p)ercent, or nothing to stop: ')
    while (cmd != ''):
        if cmd == 'r':
            pct = input('Enter a percentage: ')
            inc = get_range(data_list, float(pct))[0][1]
            print(str(pct) + '% of incomes are below $' + str(inc + 0.01) + '.\n')
        elif cmd == 'p':
            inc = input('Enter an income: ')
            pct = get_percent(data_list, int(inc))[1]
            print('An income of $' + str(inc) + ' is in the top ' + str(pct) + '% of incomes.\n')
        else:
            print('Invalid command. Try again.\n')
        cmd = input('Enter a choice to get (r)ange, (p)ercent, or nothing to stop: ')

main() #Runs Program
