#prompt for size and shape
num_str1 = input('Enter the starting length > 10: ')
val1_int = int(num_str1)

num_str2 = input('Enter 1 for Square or 2 for Circle: ')
val2_int = int(num_str2)

#quit functionality sys
import sys
if (val1_int > 10):
    print("Almost read to form Shape!")
elif (val1_int < 10):
    sys.exit("Enter a number greater than 10")
    
print (val2_int)    
if (val2_int != 1 and val2_int != 2):
    sys.exit("Please enter 1 for Square or 2 for Circle")
    
    
#divide input by 10 to account totale times to re-create shape
repeat_int = int(val1_int / 10)

# use Turtle to draw a randomly colored line

import turtle,random,time

if (val2_int == 1): #if/slese for square or circle 
# draw the square figure (line in this case)for k in range(repeat_int):
    for k in range(repeat_int):
        turtle.begin_fill()
        (r,g,b) = (random.random(), random.random(), random.random())
        turtle.pencolor(r,g,b)
        turtle.fillcolor(r,g,b)
        for i in range (4):
            turtle.forward(val1_int)
            turtle.left(90)
        val1_int = val1_int - 10
        turtle.end_fill()  # complete color filling
elif (val2_int == 2): 
    # draw the circle figure (line in this case)
    for k in range(repeat_int):
        turtle.begin_fill() # Set up random coloring
        (r,g,b) = (random.random(), random.random(), random.random()) # get three random values for red, green, and blue shades
        turtle.pencolor(r,g,b)
        turtle.fillcolor(r,g,b)
        turtle.circle(val1_int)
        val1_int = val1_int - 10
        turtle.end_fill()  # complete color filling


# let the figure be displayed for 5 seconds before it disappears
time.sleep(5)
turtle.bye()