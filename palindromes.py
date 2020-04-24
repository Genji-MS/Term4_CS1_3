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
    left = 0
    right = len(text)-1
    while left < right:
        lChar = text[left].lower()
        while lChar == " " or lChar in string.punctuation != False or lChar in string.ascii_lowercase == False:
            left +=1
            lChar = text[left].lower()
        rChar = text[right].lower()
        while rChar == " " or rChar in string.punctuation != False or rChar in string.ascii_lowercase == False:
            right -=1
            rChar = text[right].lower()
        #print (f' l:{lChar} r:{rChar}')
        lChar = string.ascii_lowercase.index(lChar)
        rChar = string.ascii_lowercase.index(rChar)
        if lChar != rChar:
            return False
        left +=1
        right -=1
    return True
    # once implemented, change is_palindrome to call is_palindrome_iterative
    # to verify that your iterative implementation passes all tests


def is_palindrome_recursive(text, left=None, right=None):
    # √: implement the is_palindrome function recursively here
    if left == None:
        left = 0
    if right == None:
        right = len(text)-1
    if left >= right:
        return True
    
    check = True
    lChar = text[left].lower()
    if lChar not in string.ascii_lowercase:
        left +=1
        check = False
    rChar = text[right].lower()
    if rChar not in string.ascii_lowercase:
        right -=1
        check = False

    #print (f'Left: {lChar} Right:{rChar} check:{check}')
    if check:
        if lChar != rChar:
            return False
        left +=1
        right -=1
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