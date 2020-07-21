# Describe an algorithm to compute the longest increasing subsequence of an array of numbers in O(n log n) time.

# Approach 1: Recursion

# Global Var to store max
global maximum

# Utility function
def LIS_Utility(arr, n):
    
    # Get access to maximum
    global maximum

    # Base Case
    if n == 1: return 1

    maxEnd = 1

    # Recursively get all LIS
    for i in range(1, n):
        res = LIS_Utility(arr, i)
        if arr[i-1] < arr[n-1] and res+1 > maxEnd:
            maxEnd = res + 1
    
    # Compare maxEnd with overall maximum
    maximum = max(maximum, maxEnd)

    return maxEnd

def LIS(arr):

    # Get access to global var
    global maximum

    n = len(arr)
    maximum = 1

    LIS_Utility(arr, n)

    return maximum

arr = [9, 23, 8, 34, 22, 49, 42, 66]
print("Length of the Longest Increasing Subsequence in the array: ", arr)
print(LIS(arr))