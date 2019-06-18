"""
Cricket Chirps
Author: Saud Aljandal
based on a given number of chirps, the function chirps_to_ftemp will
convert it to a number that representes the degrees celsius. After that,
a function will be called from another python file and will convert it to degrees fehrenheit.
print the estimated temparature in degrees celsius.
"""
from temperature import ctemp_to_ftemp

def chirps_to_ftemp_stub(x):
    """(number)-> float
    examples:
    >>> chirps_to_ftemp(32)
    The estimated temperature, 
    based on 32 chirps in 25 seconds, is
     58.4 degrees fahrenheit
    >>> chirps_to_ftemp(100)
    The estimated temperature, 
    based on 100 chirps in 25 seconds, is
     99.2 degrees fahrenheit
    >>> chirps_to_ftemp(5)
    The estimated temperature, 
    based on 5 chirps in 25 seconds, is
     42.2 degrees fahrenheit
    >>> 


"""
    pass
    return#ftemp

def chirps_to_ftemp(x):
    """(number)-> float
    examples:
    >>> chirps_to_ftemp(32)
    The estimated temperature, 
    based on 32 chirps in 25 seconds, is
     58.4 degrees fahrenheit
    >>> chirps_to_ftemp(100)
    The estimated temperature, 
    based on 100 chirps in 25 seconds, is
     99.2 degrees fahrenheit
    >>> chirps_to_ftemp(5)
    The estimated temperature, 
    based on 5 chirps in 25 seconds, is
     42.2 degrees fahrenheit
    >>> 


"""
    x2=(x/3)+4
    x3=ctemp_to_ftemp(x2)
    print("\nThe estimated temperature, "'\n\n'"based on "+str(x)+" chirps in 25 seconds, is\n\n"+str(x3)+" degrees fahrenheit.\n")
    return
