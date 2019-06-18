"""
string_reverse.
Authors: Saud Aljandal
return a reversed string.
"""
def strReverseR_stub(s):
    '''(str)-> str
    recursive function.
    this code will check the input and see if its length is one or less
    and return the same input because there is nothing to reverse.
    if the input is more than 1 letters, it will take the last letter in 
    every time and print it in the biggining of the output.
    reverse string is returned.
    examples:
    >>> strReverseR("winter 2016")
    '6102 retniw'
    >>> strReverseR("SAUD Aljandal")
    'ladnajlA DUAS'
    '''
    pass
    return#reversed string in recursive way

def strReverseI_stub(s):
    '''(str)-> str
    non-recursive function.
    this code will check the input and see if its length is one or less
    and return the same input because there is nothing to reverse.
    if the input is more than 1 letters, it will take the last letter in 
    every time and print it in the biggining of the output.
    reverse string is returned.
    examples:
    >>> strReverseI("winter 2016")
    '6102 retniw'
    >>> strReverseI("SAUD Aljandal")
    'ladnajlA DUAS'
    '''
    pass
    return#reversed string in non-recurcive way







def strReverseR(s):
    '''(str)-> str
    recursive function.
    this code will check the input and see if its length is one or less
    and return the same input because there is nothing to reverse.
    if the input is more than 1 letters, it will take the last letter in 
    every time and print it in the biggining of the output.
    reverse string is returned.
    examples:
    >>> strReverseR("winter 2016")
    '6102 retniw'
    >>> strReverseR("SAUD Aljandal")
    'ladnajlA DUAS'
    '''
    if len(s) <= 1:
        return s
    else:
        return strReverseR(s[1:]) + s[0]
    return s



def strReverseI(s):
    '''(str)-> str
    non-recursive function.
    this code will check the input and see if its length is one or less
    and return the same input because there is nothing to reverse.
    if the input is more than 1 letters, it will take the last letter in 
    every time and print it in the biggining of the output.
    reverse string is returned.
    examples:
    >>> strReverseI("winter 2016")
    '6102 retniw'
    >>> strReverseI("SAUD Aljandal")
    'ladnajlA DUAS'
    '''
    if len(s) <=1:
        return s
    else:
        return s[::-1]
    return s
