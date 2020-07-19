# Implement the function fib(n), which returns the nth number in the Fibonacci sequence, using only O(1) space.
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

print(fib(9))