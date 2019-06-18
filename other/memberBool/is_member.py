"""
list membership.
finding the targeted number in a list and the result is returned.
name: Saud Aljandal
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
                    if item < alist[mid_number]:
                            last = mid_number-1
                    else:
                            first = mid_number+1
    return result
