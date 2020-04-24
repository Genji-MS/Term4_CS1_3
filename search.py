#!python

def linear_search(array, item):
    """return the first index of item in array or None if item is not found"""
    # implement linear_search_iterative and linear_search_recursive below, then
    # change this to call your implementation to verify it passes all tests
    return linear_search_recursive(array, item)
    # return linear_search_recursive(array, item)


def linear_search_iterative(array, item):
    # loop over all array values until item is found
    for index, value in enumerate(array):
        if value == item:
            return index  # found
    return None  # not found


def linear_search_recursive(array, item, index=0):
    # √: implement linear search recursively here
    if index == len(array):
        return None
    elif array[index] == item:
        return index
    index += 1
    return linear_search_recursive(array, item, index)
    # once implemented, change linear_search to call linear_search_recursive
    # to verify that your recursive implementation passes all tests


def binary_search(array, item):
    """return the index of item in sorted array or None if item is not found"""
    # implement binary_search_iterative and binary_search_recursive below, then
    # change this to call your implementation to verify it passes all tests
    return binary_search_recursive(array, item)
    # return binary_search_recursive(array, item)


def binary_search_iterative(array, item):
    # √: implement binary search iteratively here
    left = 0
    right = len(array)  #do not -1 the index cause it'll cause issues to search right side of array
    while left < right:
        index = (left+right)//2
        #print (f' left:{left} right:{right} index:{index}')
        search = array[index]
        if search == item:
            return index
        if item < search and right != index:  #checking this to prevent loops
            right = index
        elif item > search and left != index:  #checking this to prevent loops
            left = index
        else:
            return None
    return None
    # once implemented, change binary_search to call binary_search_iterative
    # to verify that your iterative implementation passes all tests


def binary_search_recursive(array, item, left=None, right=None):
    # √: implement binary search recursively here
    if left == None:
        left = 0
    if right == None:
        right = len(array)

    index = (left + right)//2
    search = array[index]

    if left >= right:
        return None
    if search == item:
        return index
    if item<search and right != index:
        right = index
        return binary_search_recursive(array, item, left, right)
    elif item>search and left != index:
        left = index
        return binary_search_recursive(array,item,left,right)
    else:
        return None
    # once implemented, change binary_search to call binary_search_recursive
    # to verify that your recursive implementation passes all tests

if __name__ == "__main__":
    names = ['Alex', 'Brian', 'Julia', 'Kojin', 'Nabil', 'Nick', 'Winnie']
    print (binary_search(names, 'Winnie'))