# Good morning! Here's your coding interview problem for today.

# Given a real number n, find the square root of n. For example, given n = 9, return 3.
# Citation: Geeksforgeeks
# # Returns floor of square root of x 
def floorSqrt(x): 
  
    # Base cases 
    if (x == 0 or x == 1): 
        return x 
  
    # Staring from 1, try all numbers until 
    # i*i is greater than or equal to x. 
    i = 1; result = 1
    while (result <= x): 
      
        i += 1
        result = i * i 
      
    return i - 1
  
# Driver Code 
x = 11
print(floorSqrt(x))