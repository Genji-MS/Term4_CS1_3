#!python

import string
# Hint: Use these string constants to encode/decode hexadecimal digits and more
# string.digits is '0123456789'
# string.hexdigits is '0123456789abcdefABCDEF'
# string.ascii_lowercase is 'abcdefghijklmnopqrstuvwxyz'
# string.ascii_uppercase is 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
# string.ascii_letters is ascii_lowercase + ascii_uppercase
# string.printable is digits + ascii_letters + punctuation + whitespace


def decode(digits, base):
    """Decode given digits in given base to number in base 10.
    digits: str -- string representation of number (in given base)
    base: int -- base of given number
    return: int -- integer representation of number (in base 10)"""
    # Handle up to base 36 [0-9a-z]
    assert 2 <= base <= 36, 'base is out of range: {}'.format(base) 
    # √ : Decode digits from binary (base 2)
    if base == 2:
        digList = [char for char in digits][::-1]#convert to array of char and reverse
        sumList = [(int(digit) * 2 **i) for digit,i in zip(digList,range(len(digList)))]#make list of binary into ints
        return sum(sumList)#add each item of list
    # √: Decode digits from hexadecimal (base 16)
    elif base == 16:
        digList = [char for char in digits][::-1]
        sumList = [ (digList.index(digit) * 16 **i ) for digit,i in zip(digList,range(len(digList)))]
        return int(digits,16)
    # √: Decode digits from any base (2 up to 36)
    else:
        digList = [char for char in digits][::-1]#convert to array of char and reverse
        sumList = [(int(digit) * base **i) for digit,i in zip(digList,range(len(digList)))]#make list of binary into ints
        return sum(sumList)#add each item of list


def encode(number, base):
    """Encode given number in base 10 to digits in given base.
    number: int -- integer representation of number (in base 10)
    base: int -- base to convert to
    return: str -- string representation of number (in given base)"""
    # Handle up to base 36 [0-9a-z]
    assert 2 <= base <= 36, 'base is out of range: {}'.format(base)
    # Handle unsigned numbers only for now
    assert number >= 0, 'number is negative: {}'.format(number)
    # √: Encode number in binary (base 2)
    # return "{0:b}".format(number)
    if base == 2:
        binaryList=[]
        while number:
            if number%2 == 1:
                number -=1
                binaryList.append('1')
            else:
                binaryList.append('0')
            number /= 2
            number = int(number)
        return ''.join(reversed(binaryList))
    # √: Encode number in hexadecimal (base 16)
    # return hex(number)[2:]
    elif base == 16:
        hexList = []
        while number:
            number, remainder = divmod(number, 16)
            hexList.append(string.hexdigits[remainder])
        return ''.join(reversed(hexList))
    # √: Encode number in any base (2 up to 36)
    elif base >= 2 and base <= 36:
        decoded = []
        while number:
            number, remainder = divmod(number, base)
            decoded.append(string.printable[remainder])
        return ''.join(reversed(decoded))
    else:
        return 0


def convert(digits, base1, base2):
    """Convert given digits in base1 to digits in base2.
    digits: str -- string representation of number (in base1)
    base1: int -- base of given number
    base2: int -- base to convert to
    return: str -- string representation of number (in base2)"""
    # Handle up to base 36 [0-9a-z]
    assert 2 <= base1 <= 36, 'base1 is out of range: {}'.format(base1)
    assert 2 <= base2 <= 36, 'base2 is out of range: {}'.format(base2)
    # √: Convert digits from base 2 to base 16 (and vice versa)
    if base1 == 2 and base2 == 16:
        convert = decode(digits,2)
        return encode(convert,16)
    elif base1 == 16 and base2 == 2:
        convert = decode(digits,16)
        return encode(convert,2)
    # √: Convert digits from base 2 to base 10 (and vice versa)
    elif base1 == 2 and base2 == 10:
        return f'{decode(digits,2)}'
    elif base1 == 10 and base2 == 2:
        return encode(int(digits),2)
    # √: Convert digits from base 10 to base 16 (and vice versa)
    elif base1 == 10 and base2 == 16:
        return encode(int(digits),16)
    elif base1 == 16 and base2 == 10:
        return f'{decode(digits,16)}'
    # √: Convert digits from any base to any base (2 up to 36)
    elif base1 >= 2 and base1 <= 36 and base2 >=2 and base2 <= 36:
        convert = decode(digits,base1)
        return encode(convert,base2)


def main():
    """Read command-line arguments and convert given digits between bases."""
    import sys
    args = sys.argv[1:]  # Ignore script file name
    if len(args) == 3:
        digits = args[0]
        base1 = int(args[1])
        base2 = int(args[2])
        # Convert given digits between bases
        result = convert(digits, base1, base2)
        print('{} in base {} is {} in base {}'.format(digits, base1, result, base2))
    else:
        print('Usage: {} digits base1 base2'.format(sys.argv[0]))
        print('Converts digits from base1 to base2')


if __name__ == '__main__':
    print(encode(79,16) )

#79 / 16 = 
# 4 r 15
# 4   f