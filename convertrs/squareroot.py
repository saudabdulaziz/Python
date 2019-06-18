"""
Approximate Square Root
Author: Saud Aljandal
give the approximate square root with number of iterations 
from a non built in function.
"""
from math import sqrt
def sqrt_compare_stub(num,iterations):
    """(numebr, number)-> float

    return a value that will be square rooted as many as
    the number of iterations
    examples:
    >>> sqrt_compare(1000, 5)
    41.24542607499115
    >>> sqrt_compare(12,44)
    3.4641016151377544


    the function will also print a report showing the differnces between
    the built-in sqrt and the sqrt that used in the sqrt_compare function.
    example:
    >>> sqrt_compare(9,5)
    For 9 using 5 iterations:
    my_sqrt value is: 3.000000001396984 
    math lib sqrt value is: 3.0 
    This is a 0.00 percent error.
    3.000000001396984
    """
    pass
    return #value

def sqrt_compare(num,iterations):
    """(numebr, number)-> float

    return a value that will be square rooted as many as
    the number of iterations
    examples:
    >>> sqrt_compare(1000, 5)
    41.24542607499115
    >>> sqrt_compare(12,44)
    3.4641016151377544


    the function will also print a report showing the differnces between
    the built-in sqrt and the sqrt that used in the sqrt_compare function.
    example:
    >>> sqrt_compare(9,5)
    For 9 using 5 iterations:
    my_sqrt value is: 3.000000001396984 
    math lib sqrt value is: 3.0 
    This is a 0.00 percent error.
    3.000000001396984
    """
    value=1
    for i in range(iterations):
        value=.5*(value+(num/value))
        libvalue= sqrt(num)
    print ("For",num,"using",iterations,"iterations:\nmy_sqrt value is:",value,"\nmath lib sqrt value is:",libvalue,"\nThis is a %.2f percent error."%(((value-libvalue))*10),"\n")
    return value
