# Implement the function fib(n), which returns the nth number in the Fibonacci sequence, using only O(1) space.

# Approach 1: Dynamic Programming -- O(n) Time & O(n) Space
# By storing the values we compute in between calls, we can avoid recomputation of already computed values
def fib(n):
    # Take the first two Fibonacci numbers, 0 and 1
    fibList = [0, 1]

    while len(fibList) < n + 1:
        fibList.append(0)
        
    if n <= 1:
        return n

    else:
        if fibList[n-1] == 0:
            fibList[n-1] = fib(n-1)
        if fibList[n-2] == 0:
            fibList[n-2] = fib(n-2)
        fibList[n] = fibList[n-2] + fibList[n-1]
        return fibList[n]

print('9th Fibonacci Number:', fib(9))

# Second Approach: Memoization -- O(n) Time & O(1) Space
# We can further improve the space needed from the O(n) dynamic programming approach, to only needing O(1) space,
# by only storing the previous 2 numbers, since they are all we need to solve for the proceeding fibonacci number.
def fibonacci(n):
    a = 0
    b = 1
    if n == 0:
        return a
    if n == 1:
        return b
    else:
        for i in range(2, n+1):
            c = a + b
            a = b
            b = c
        return b

print('9th Fibonacci Number:', fibonacci(9))