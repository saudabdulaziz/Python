
'''
Art Show
Author: Saud Aljandal
this function will use the "turtle" and "random" from tha python library
to randomly draw 5 lines going to random directions. eventually, the 5 lines will
draw a nice random art!.
'''
import random
from turtle import *

def art_show_stup():
    """once the code starts, it will start drowing"""
    """
    t1=Pen()
    t1.color('red')
    t2=Pen()
    t2.color('orange')
    t3=Pen()
    t3.color('green')
    t4=Pen()
    t4.color('blue')
    t5=Pen()
    t5.color('black')
    count=0
    
    while count<300:
        hideturtle()
        turtles=[t1,t2,t3,t4,t5]
        for i in turtles :
            i.hideturtle()
            i.speed(400)
            length=random.randrange(10,20)
            angle=random.randrange(-180,181)
            i.fd(length)
            i.rt(angle)

        count+=1
        """
    pass
    return None

def art_show():
    """once the code starts, it will start drowing"""
    t1=Pen()
    t1.color('red')
    t2=Pen()
    t2.color('orange')
    t3=Pen()
    t3.color('green')
    t4=Pen()
    t4.color('blue')
    t5=Pen()
    t5.color('black')
    count=0
    
    while count<300:
        turtles=[t1,t2,t3,t4,t5]
        for i in turtles :
            i.hideturtle()
            i.speed(0)
            length=random.randrange(5,10)
            angle=random.randrange(-180,181)
            i.fd(length)
            i.rt(angle)

        count+=1
    return None


art_show()
