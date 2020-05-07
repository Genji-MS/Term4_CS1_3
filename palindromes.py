#!python

import string
# Hint: Use these string constants to ignore capitalization and/or punctuation
# string.ascii_lowercase is 'abcdefghijklmnopqrstuvwxyz'
# string.ascii_uppercase is 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
# string.ascii_letters is ascii_lowercase + ascii_uppercase


def is_palindrome(text):
    """A string of characters is a palindrome if it reads the same forwards and
    backwards, ignoring punctuation, whitespace, and letter casing."""
    # implement is_palindrome_iterative and is_palindrome_recursive below, then
    # change this to call your implementation to verify it passes all tests
    assert isinstance(text, str), 'input is not a string: {}'.format(text)
    return is_palindrome_recursive(text)
    # return is_palindrome_recursive(text)


def is_palindrome_iterative(text):
    # √: implement the is_palindrome function iteratively here
    #set variables to the left and right index extremes of the word
    left = 0
    right = len(text)-1
    #If these values cross each other, we will have passed the middle of the word and can confirm it is palindrome
    while left < right:
        #2nd loop to format our character at the left/right index. If it's not a letter, check the next index
        lChar = text[left].lower()
        while lChar == " " or lChar in string.punctuation != False or lChar in string.ascii_lowercase == False:
            left +=1
            lChar = text[left].lower()
        #as above for the right character
        rChar = text[right].lower()
        while rChar == " " or rChar in string.punctuation != False or rChar in string.ascii_lowercase == False:
            right -=1
            rChar = text[right].lower()
        #We've determined that both values are actual letters. I converted them into numbers, but it's not needed in hindsight
        lChar = string.ascii_lowercase.index(lChar)
        rChar = string.ascii_lowercase.index(rChar)
        #Compare if our letters are the same, if its not, then our word is not a pallindrome
        if lChar != rChar:
            return False
        #advance each index
        left +=1
        right -=1
    #we've exited the loop, we can safely say our palindrome is true
    return True
    # once implemented, change is_palindrome to call is_palindrome_iterative
    # to verify that your iterative implementation passes all tests


def is_palindrome_recursive(text, left=None, right=None):
    # √: implement the is_palindrome function recursively here
    #If variables have not been passed into the function, initialize them
    if left == None:
        left = 0
    if right == None:
        right = len(text)-1
    #Base case to exit our loop as true
    if left >= right:
        return True
    #We will only 'check' the variables if we have two letters and not punctuation. 
    check = True
    #format each character to lowercase(if possible) 
    lChar = text[left].lower()
    if lChar not in string.ascii_lowercase:
        #This is punctuation or a space, increment to the next index value
        left +=1
        check = False
    rChar = text[right].lower()
    if rChar not in string.ascii_lowercase:
        right -=1
        check = False

    #check if we have a pallindrome by comparing characters
    if check:
        #if characters don't match, it's our exit case to determine not a pallindrome
        if lChar != rChar:
            return False
        #increment our left/right variables
        left +=1
        right -=1
    #itterate
    return is_palindrome_recursive(text, left, right)
    # once implemented, change is_palindrome to call is_palindrome_recursive
    # to verify that your iterative implementation passes all tests


def main():
    import sys
    args = sys.argv[1:]  # Ignore script file name
    if len(args) > 0:
        for arg in args:
            is_pal = is_palindrome(arg)
            result = 'PASS' if is_pal else 'FAIL'
            is_str = 'is' if is_pal else 'is not'
            print('{}: {} {} a palindrome'.format(result, repr(arg), is_str))
    else:
        print('Usage: {} string1 string2 ... stringN'.format(sys.argv[0]))
        print('  checks if each argument given is a palindrome')


if __name__ == '__main__':
    main()