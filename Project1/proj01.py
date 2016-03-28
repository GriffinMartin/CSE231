# Input two numbers print their sum and product
###########################################################
    #  PreLab 01
    #
    #Griffin Martin
    #A45789968
    #mart1444@msu.edu
    ###########################################################
num_str1 = input('Enter the debt value: ')
num_str2 = input('Enter a denomination currency: ')

val1_int = int(num_str1)
val2_float = float(num_str2)  

bills = val1_int / val2_float 
distance_inches = 0.0043 * bills
distance_miles = distance_inches / 63360
moon_distance = 238857
distance_moon = distance_miles / moon_distance

#sum_float = val1_int + val2_float  # adding an int and a float results in a float
#prod_float = val1_int * val2_float # the product of an int and a float is a float

print('The debt',val1_int, 'as a height in miles of',val2_float,'\'s', distance_miles)
print('That is:',distance_moon, 'times the average distance from the earth to the moon')

