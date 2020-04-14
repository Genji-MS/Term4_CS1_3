def ReverseString(string):
    print(string)
    reversedString = ""
    for r in range(len(string)-1,-1,-1):
        reversedString += string[r]
    return reversedString

def CheckPalandrome(string):
    passed = True
    halfLength = len(string)//2
    for s,e in zip(range(0,halfLength,1),range(len(string)-1,halfLength-1,-1)):
        if string[s] != string[e]:
            passed = False
            break
    return passed

def CheckPalandromeRec(string, left = 0, right = -1):
    if right == -1:
        right = len(string)-1
    if left >= right:
        return True
    if string[left] != string[right]:
        return False
    else:
        left +=1
        right -=1
    return CheckPalandromeRec(string, left, right)

if __name__ == '__main__':
    print(ReverseString("a b c d e f e g a g b b") )
    print(CheckPalandromeRec("racecar"))
    print(CheckPalandromeRec("Lizapeizel"))
    print(CheckPalandromeRec("WooooW"))