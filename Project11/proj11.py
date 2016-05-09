import turtle
import time
import math
import random

# ------------------------------------------------------------------------------
# Computer Project 11
# Date: April 21, 2016
# ------------------------------------------------------------------------------
# This program prompts the user for a figure length and his/her MSU identifier.
# It then hashes the number in the ID pairwise by adding them and taking the
# result modulo HASH_MOD (10 in this case). The result is the hash value which
# corresponds to a shape type. The program finally draws one shape in each of
# the four quadrants based on the type and length using Python turtle module.
# ==============================================================================

HASH_MOD = 10 # Used when hashing

# ------------------------------------------------------------------------------
# FUNCTION  drawShape(shape, side)
#   Draws shape of corresponding type and length size.
# ------------------------------------------------------------------------------
def drawShape(shape, side):
    # Setting turtle up
    (r,g,b) = (random.random(), random.random(), random.random())
    turtle.pencolor(r,g,b)
    turtle.fillcolor(r,g,b)
    turtle.begin_fill()

    # Start drawing
    turtle.down()
    turtle.forward(side)
    turtle.left(90)
    turtle.forward(side)

    if shape == 1: # Straight line
        turtle.left(135)
        turtle.forward(math.sqrt(2*side*side))
        
    elif shape == 2: # Steps
        turtle.left(90)
        for _ in range(2):
            turtle.forward(side/2)
            turtle.left(90)
            turtle.forward(side/2)
            turtle.right(90)
        
    elif shape == 3: # Unbroken step
        turtle.left(90)
        turtle.forward(side/4)
        turtle.left(45)
        turtle.forward(math.sqrt(9*side*side/8))
        turtle.left(45)
        turtle.forward(side/4)
        
    elif shape == 4: # Convex quarter-circle
        turtle.left(90)
        turtle.circle(side, 90)
    
    elif shape == 5: # Concave quarter-circle
        turtle.left(180)
        turtle.circle(-side, 90)
    
    elif shape == 6: # Staircase
        steps = 5
        turtle.left(90)
        turtle.forward(side/steps)
        for _ in range(steps - 1):
            turtle.left(90)
            turtle.forward(side/steps)
            turtle.right(90)
            turtle.forward(side/steps)
        turtle.left(90)
        turtle.forward(side/steps)

    elif shape == 7: # Flower
        turtle.left(90)
        turtle.circle(side/2, 90)
        turtle.right(90)
        turtle.circle(side/2, 90)
        
    elif shape == 8: # Squiggle
        turtle.left(90)
        turtle.circle(side/2, 90)
        turtle.circle(-side/2, 90)
        
    elif shape == 9: # Speed Bump
        turtle.left(90)
        turtle.circle(side*2/5, 90)
        turtle.right(90)
        turtle.forward(side/5)
        turtle.left(90)
        turtle.forward(side/5)
        turtle.right(90)
        turtle.circle(side*2/5, 90)
    
    else: # shape == 0: # Knob
        turtle.left(90)
        turtle.circle(side/5, 90)
        turtle.circle(-side/5, 90)
        turtle.right(90)
        turtle.circle(side/5, 270)
        turtle.right(90)
        turtle.circle(-side/5, 90)
        turtle.circle(side/5, 90)
    
    turtle.end_fill()
    turtle.up()
    turtle.setpos(0,0)
    turtle.seth(0)

# ------------------------------------------------------------------------------
# FUNCTION  getHash(value)
#   Returns hash corresponding to value. Computed by adding the digits modulo
# HASH_MOD of value (string).
# ------------------------------------------------------------------------------
def getHash(value):
    return sum(map(int, value)) % HASH_MOD

# ------------------------------------------------------------------------------
# FUNCTIONS  drawQ?(id, side)
#   Draws shape in ? quadrant given id (ID) and size (length).
# ------------------------------------------------------------------------------
def drawQ1(id, side):
    turtle.up() # Move up turtle
    turtle.setpos(-side, 0) # Move to corresponding corner
    shape = getHash(id[1:3]) # Calculate hash for the digits 1-2
    drawShape(shape, side) # Draw shape

def drawQ2(id, side):
    turtle.up() # Move up turtle
    turtle.setpos(0, side) # Move to top corner
    turtle.right(90) # Modify orientation so it faces down
    shape = getHash(id[3:5]) # Calculate hash for the digits 3-4
    drawShape(shape, side) # Draw shape

def drawQ3(id, side):
    turtle.up() # Move up turtle
    turtle.setpos(0, -side) # Move to bottom corner
    turtle.left(90) # Modify orientation so it faces up
    shape = getHash(id[5:7]) # Calculate hash for the digits 5-6
    drawShape(shape, side) # Draw shape

def drawQ4(id, side):
    turtle.up() # Move up turtle
    turtle.setpos(side, 0) # Move to right corner
    turtle.left(180) # Modify orientation so it faces right
    shape = getHash(id[7:9]) # Calculate hash for the digits 7-8
    drawShape(shape, side) # Draw shape

# ------------------------------------------------------------------------------
# MAIN FUNCTION STARTS HERE
# ------------------------------------------------------------------------------
def main():
    while True:
        side = input("Please enter the total length of the figure: ")
        try:
            side = int(side)
        except:
            print('Please enter a valid number.\n')
            continue
        break

    while True:
        id = input("Please enter MSU ID (including the starting letter): ")
        if len(id) == 9 and id[0].isalpha() and all(d.isdigit() for d in id[1:]):
            break
        else:
            print('Please enter a valid MSU ID.\n')
            continue

    turtle.colormode(1.0)
    turtle.speed(0)

    drawQ1(id, side/2)
    drawQ2(id, side/2)
    drawQ3(id, side/2)
    drawQ4(id, side/2)

    time.sleep(20)
    turtle.bye()

if __name__ == '__main__':
    main()