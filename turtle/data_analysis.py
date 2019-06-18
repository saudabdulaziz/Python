"""
draw chart
name: Saud Aljandal
"""

import turtle

def median (alist):
    copylist = alist [:] 
    copylist . sort ()
    if len ( copylist ) % 2 == 0: #even length
        rightmid = len(copylist)//2
        leftmid = rightmid - 1
        median = (copylist[leftmid] + copylist[rightmid])//2
    else:#odd length
        mid = len(copylist)//2
        median = copylist[mid]
    return median

def frequencyTable(alist):
    countdict = {}
    for  item in alist:
        if item in countdict:
            countdict[item] = countdict[item]+1
        else:
            countdict[item] =1
    itemlist = list(countdict.keys())
    itemlist.sort()

    print("    ITEM" , "    FREQUENCY")

    for item in itemlist:
        print("      ",item , "              ",countdict[item])


def data_freq_chart(alist):
    """
    plots frequency bar chart of elements in my_list using turtle graphics
    Args:
        my_list: list of floats (MUST BE NON-EMPTY)
    Outputs:
        frequence bar chart of elements plotted using turtle graphics
        waits for user to click on window to exit
    """
    count = {}

    for item in alist:
        if item in count:
            count[item] += 1
        else:
            count[item] = 1

    item_list = list(count.keys())
    min_item = 0
    max_item = len(item_list) - 1

    count_list = count.values()
    max_count = max(count_list)

    wn = turtle.Screen()
    chart_turtle = turtle.Turtle()
    wn.setworldcoordinates(-1, -1, max_item+1, max_count+1)
    chart_turtle.hideturtle()

    chart_turtle.up()
    chart_turtle.goto(0,0)
    chart_turtle.down()
    chart_turtle.goto(max_item,0)
    chart_turtle.up()

    chart_turtle.goto(-1,0)
    chart_turtle.write("0", font=("Helvetica",13,'bold'))
    chart_turtle.goto(-1, max_count)
    chart_turtle.write(str(max_count), font=("Helvetica", 13,'bold'))

    for index in range(len(item_list)):
        chart_turtle.goto(index, -1)
        chart_turtle.write(str(item_list[index]), font=("Helvetica",16,'bold'))
        chart_turtle.goto(index, 0)
        chart_turtle.down()
        chart_turtle.goto(index, count[item_list[index]])
        chart_turtle.up()

    wn.exitonclick()
    
