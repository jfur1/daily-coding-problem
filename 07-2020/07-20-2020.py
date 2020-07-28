# Good morning! Here's your coding interview problem for today.

# This problem was asked by Uber.

# Write a program that determines the smallest number of perfect squares that sum up to N.

# Here are a few examples:

# Given N = 4, return 1 (4)
# Given N = 17, return 2 (16 + 1)
# Given N = 18, return 2 (9 + 9)

def getMinSquares(n):

    # Base Cases
    if n <= 3:
        return n
    
    # getMinSquares rest of the table  
    # using recursive formula 
    res = n # Maximum squares required  
            # is n (1 * 1 + 1 * 1 + ..) 
  
    # Go through all smaller numbers to revursively find minimum
    for x in range(1, n+1):
        temp = x* x
        if temp > n:
            break
        else:
            res = min(res, 1 + getMinSquares(n-temp))

    return res

print(getMinSquares(4))
print(getMinSquares(17))