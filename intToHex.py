'''
number / 16
take whole number = First Hex
number - (whole number * 16) = 2ndHex
hexList [01233456789ABCDEF]
return string of hexList[First Hex] + hexList[2ndHex]
'''

def intToHex(number):
    hexList = ['0','1','2','3','4','5','6','7','8','9','A','B','C','D','E','F']
    num1 = 0
    num2 = 0
    hexString = ""
    if number <= 256:
        num1 = int(number/16)
        print (num1)
        num2 = number-(num1*16)
        print (num2)
        hexString += hexList[num1]
        hexString += hexList[num2]
    return hexString

print (intToHex(1))
