"""
test list membership functions.
testing the test cases for functions is_memberR and is_memberI in
more effeciant and intelligant procces.
author: Saud Aljandal
"""
def is_memberR(alist, target):
    '''(list , int)-> bool'''
    '''
    this code will take the number,target, and put it in the middle of the list.
    if the number in the list is grater than the input, it will eleminate 
    the second half of the ,alist,parameter. And it will do the same thing with the first half.
    if the input,target, is less than the middle number in the list, it will eleminate
    the first half of the list.[mid_number]
    After that, it will will check the length of the last element in the list 
    and check if that's true.
    examples:
    >>> is_memberR([23, 24, 25, 26, 27], 5)
    False
    >>> is_memberR([0, 1, 4, 5, 6, 8], 4)
    True
    '''
    if(len(alist) ==1) and (alist[0] != target) or (len(alist) == 0):
        return False
    mid_number= len(alist)//2
    if target == alist[mid_number]:
        return True
    if target > alist[mid_number]:
        return is_memberR(alist[mid_number:], target)
    elif target < alist[mid_number]:
        return is_memberR(alist[:mid_number], target)

def is_memberI(alist, target):
    '''(list , int)-> bool'''
    '''
    this code will take the number,target, and put it in the middle of the list.
    if the number in the list is grater than the input, it will eleminate 
    the second half of the ,alist,parameter. And it will do the same thing with the first half.
    if the input,target, is less than the middle number in the list, it will eleminate
    the first half of the list.[mid_number]
    After that, it will will check the length of the last element in the list 
    and check if that's true.
    examples:
    >>> is_memberI([23, 24, 25, 26, 27], 5)
    False
    >>> is_memberI([0, 1, 4, 5, 6, 8], 4)
    True
    '''
    first = 0
    last = len(alist)-1
    result = False
    while first<=last and not result:
            mid_number = (first + last)//2
            if alist[mid_number] == target:
                    result = True
            else:
                    if target < alist[mid_number]:
                            last = mid_number-1
                    else:
                            first = mid_number+1
    return result

def test( desc, actual, anticipated ) :
    if actual == anticipated :
        return True
    else:
        return False

def test_is_member (f):
    '''(function)->(bool)'''
    '''
    this recursive function will test the test cases in the assignment page and return True if the actual and anicipated
    results are the same,either in is_memberI function or in is_memberR function, otherwise, will return False.
    '''

    if f ==(is_memberI):
        print("            ---TESTING FUNCTION is_memberI---\n")
    else:
        print("            ---TESTING FUNCTION is_memberR---\n")
    test1=test("[1, 3, 5, 7], 4 => False", f([1, 3, 5, 7], 4),False)
    if test1 == False:
        print("     **even number of items in list**\n")#challenges
    test2=test("[23, 24, 25, 26, 27], 5 => False", f([23, 24, 25, 26, 27], 5),False)
    if test2 == False:
        print("     **odd number of items in list**\n")#challenges
    test3=test("[0, 1, 4, 5, 6, 8], 4 => True",f([0, 1, 4, 5, 6, 8], 4),True)
    test4=test("[0, 1, 2, 3, 4, 5, 6], 3 => True",f( [0, 1, 2, 3, 4, 5, 6], 3),True)
    test5=test("[1, 3], 1 => True",f([1, 3], 1),True)
    test6=test("[2, 10], 10 => True",f([2, 10], 10),True)
    test7=test("[99, 100], 101 => False",f([99, 100], 101),False)
    if test7== False:
        print("     **short list**\n")#challenges
    test8=test("[42], 42 => True",f([42], 42),True)
    test9=test("[43], 44 => False",f([43], 44),False)
    if test9==False:
        print("     **one item list**\n")#challenges
    test10=test("[],99 => False",f([], 99),False)
    if test10==False:
        print("     **empty list**\n")#challenges
    while  (test1 and test2 and test7 and test9 and test10 and test6 and test3 and test8 and test4 and test5) is True:
        return True

    else:
        return False

    
