def compute_sum(n):
    sum = 0
    for i in range(1,n+1,1):
        sum += i
    return sum

def compute_sum_rec(n,i = 0): #initialize our iterator at 0
    i += 1 #increment i +1 to approach our base case
    if i == n: #base case
        return n#the last number to add
    return i + compute_sum_rec(n, i)#add the current number to the next

print(compute_sum_rec(4) ) # = 10