import string

def reverse_int(number):
    stack = []
    while number:
        number, remainder = divmod(number, 10)
        stack.append(string.printable[remainder])
    revInt= ''.join(stack)
    return int(revInt)

print (reverse_int(3479))
