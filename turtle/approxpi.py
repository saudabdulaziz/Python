"""
approximating pi
Author: Saud Aljandal
give the approximate pi "Monte Calro simulation" with number of darts from
a non built in function. after that, it will draw the Monte Calro simulation and
print a report incloding the pi value that I made and compare it with the math library
value and find if there is a percentage error.
"""
import random
import math
from turtle import *


def montePi_stub(numDarts):
    """(integer)-> float
    return a value that will be a Monte Carli pi as many as
    the number of Darts
    examples:
    >>> montePi(200)
    3.26
    >>> montePi(10000)
    3.1476
    """
    return #pi
    pass
def isInCircle_stub(x,y,r):
    """(numebr, number, number)-> boolean
    this function will check if the three parameters,
    x and y values of a point, and a radius, r are in the range of the wanted area
    of the circle and depends on that will return True or False.
    examples:
    >>> isInCircle(.5, .5, 1)
    True
    >>> isInCircle(1, 2, 1)
    False
    """
    return #bool
    pass
    
def isInCircle(x,y,r):
    """(numebr, number, number)-> boolean
    this function will check if the three parameters,
    x and y values of a point, and a radius, r are in the range of the wanted area
    of the circle and depends on that will return True or False.
    examples:
    >>> isInCircle(.5, .5, 1)
    True
    >>> isInCircle(1, 2, 1)
    False
    """
    d=math.sqrt(x**2 + y**2)
    
    return d <= r

def montePi(numDarts):
    """(integer)-> float
    return a value that will be a Monte Carli pi as many as
    the number of Darts
    examples:
    >>> montePi(200)
    3.26
    >>> montePi(10000)
    3.1476
    """
    inCircle=0
    
    for i in range(numDarts):
        x = random.random()
        y = random.random()
        
        d=math.sqrt(x**2 + y**2)
        if isInCircle(x,y,1):
            inCircle += 1
        else:
            pi = inCircle/numDarts * 4
    
    return pi
def showMontePi(numDarts):

    Screen()
    setworldcoordinates(-2,-2,2,2)
    hideturtle()
    up()
    goto(-1,0)
    down()
    goto(1,0)    
    up()
    goto(0,1)
    down()
    goto(0,-1)
    circle = 0
    up()

    for i in range(numDarts):

        speed(0)
        hideturtle()
        x = random.random()
        y = random.random()
        d = math.sqrt(x**2 + y**2)
        goto(x,y)

        if d <= 1:
            circle = circle + 1
            color("green")
        else:
            color("red")

        dot()

    libpi = math.pi
    pi = circle/numDarts * 4
    exitonclick()

    
    print ("\nWith",numDarts,"iterations(darts):\n\nmy approximate value for pi is:",pi,"\n\nmath lib pi value is:",libpi,"\n\nThis is a %.2f percent error."%((abs(pi-libpi)/(libpi))*100),"\n\n")
    return pi
