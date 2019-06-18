
"""
draw_barcode.py
Draw barcode representing a ZIP code using Turtle graphics
Author: Saud Aljandal
"""
import turtle

ENCODINGS = [[1, 1, 0, 0, 0],	# encoding for '0'
             [0, 0, 0, 1, 1],	# encoding for '1'
             [0, 0, 1, 0, 1],   # encoding for '2'
             [0, 0, 1, 1, 0],	# encoding for '3'
             [0, 1, 0, 0, 1],	# encoding for '4'
             [0, 1, 0, 1, 0],	# encoding for '5'
             [0, 1, 1, 0, 0],	# encoding for '6'
             [1, 0, 0, 0, 1],	# encoding for '7'
             [1, 0, 0, 1, 0],	# encoding for '8'
             [1, 0, 1, 0, 0]	# encoding for '9'
            ]

SINGLE_LENGTH = 25	# length of a short bar, long bar is twice as long

def compute_check_digit(digits):
    """
    Compute the check digit for use in ZIP barcodes
    args:
        digits: list of 5 integers that make up zip code
    returns:
        check digit as an integer
    """
    sum = 0
    for i in range(len(digits)):
        sum = sum + digits[i]
    check_digit = 10 - (sum % 10)
    if (check_digit == 10):
        check_digit = 0
    return check_digit

def draw_bar(my_turtle, digit):
    
    """
    Takes in a digit (either 0 or 1), draws a single length bar or a double length bar
    and returns the turtle right in front of the previous bar ready to draw a new one.
    args:
        digit: either a 0 or 1 depending on the Encoding
    Output:
        Draws a single or double length bar using the Turtle
    """
    my_turtle.left(90)
    if digit == 0:
        length = SINGLE_LENGTH
    else:
        length = 2 * SINGLE_LENGTH
    my_turtle.forward(length)
    my_turtle.up()
    my_turtle.backward(length)
    my_turtle.right(90)
    my_turtle.forward(10)
    my_turtle.down()


def draw_zip(my_turtle, zip):
    """
    Draws the postal barcode of each inputted zipcode using Turtle
    args:
        zip: the zipcode of the desired postal barcode
    Output:
        Draws the postal barcode of the desired destination in Turtle 
    """
    digits = []
    digit = 0
    digit_in_zip = 0
    while (zip > 0):                  # Turns the argument zip into a list of digits
        digits = [zip % 10] + digits
        zip = zip // 10
    draw_bar(my_turtle,1)
    for i in range(5):              # Used to run through each digit in digits to access that digit in encodings
        digit_in_zip = digits[i]
        for i in range(5):          # Used to run through each list of binary in ENCODINGS to have the turtle draw each half or full line for each digit in digits
            digit = ENCODINGS[digit_in_zip][i]
            draw_bar(my_turtle,digit)
    for i in range(5):              # Used to run through the list of binary in ENCODINGS that represents the check digit
        digit = ENCODINGS[compute_check_digit(digits)][i]
        draw_bar(my_turtle,digit)
    draw_bar(my_turtle,1)

def zipToBar(zipcode):
    '''(str)->turtle'''
    '''this code will call the function draw_zip and will start drawing'''
    my_turtle = turtle.Turtle()
    my_turtle.penup()
    my_turtle.goto(-120,0)
    my_turtle.pendown()
    zipcode=int(zipcode)
    return(draw_zip(my_turtle, zipcode))
