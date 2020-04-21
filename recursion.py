#!python

def factorial(n):
    """factorial(n) returns the product of the integers 1 through n for n >= 0,
    otherwise raises ValueError for n < 0 or non-integer n"""
    # check if n is negative or not an integer (invalid input)
    if not isinstance(n, int) or n < 0:
        raise ValueError('factorial is undefined for n = {}'.format(n))
    # implement factorial_iterative and factorial_recursive below, then
    # change this to call your implementation to verify it passes all tests
    #return factorial_iterative(n)
    return factorial_recursive(n)


def factorial_iterative(n):
    # √: implement the factorial function iteratively here
    sum = 1
    for i in range(1,n+1,1):
        sum *= i
    return sum
    # once implemented, change factorial (above) to call factorial_iterative
    # to verify that your iterative implementation passes all tests


def factorial_recursive(n, i = 0):
    i += 1 #increment i +1 to approach our base case
    if i >= n: #base case including 0
        return i #the last number to add (while we could use n, this will cause an error where n = 0 returns 0 NOT 1)
    return i * factorial_recursive(n, i)

    


def main():
    import sys
    args = sys.argv[1:]  # Ignore script file name
    if len(args) == 1:
        num = int(args[0])
        result = factorial(num)
        print('factorial({}) => {}'.format(num, result))
    else:
        print('Usage: {} number'.format(sys.argv[0]))


if __name__ == '__main__':
    main()