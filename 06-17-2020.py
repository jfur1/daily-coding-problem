# You have N stones in a row, and would like to create from them a pyramid. 
# This pyramid should be constructed such that the height of each stone increases by one until reaching the tallest stone, 
# after which the heights decrease by one. In addition, the start and end stones of the pyramid should each be one stone high.

# You can change the height of any stone by paying a cost of 1 unit to lower its height by 1, as many times as necessary.
# Given this information, determine the lowest cost method to produce this pyramid.

# For example, given the stones [1, 1, 3, 3, 2, 1], the optimal solution is to pay 2 to create [0, 1, 2, 3, 2, 1].

# Author: John Furlong

# Dyanmic Programming Appraoach -- help from GeeksforGeeks
#   Scan left to right, and determine the maximum possible height for each position.
#   * If H(i) is the height of a stone at position i, 
#       then maxHeight(i) = min(H(i), i, maxHeight(i-1))
#   * Max height cannot exceed H(i) since we can only decrease the number of stones
#   * Max height cannot exceed i, since the pyramid must start at height 1
#   * Max height cannot exceed max possible height of the stone before it, as stones must increase when moving left
#   
# Similarly, calculate the max height when moving from the right to left.
# By finding the peak of the pyramid, we can use that index to find the minimum cost of constructing the pyramid


def constructPyramid(stones):
    N = len(stones)

    # Used to store max height at each position
    left = [0] * N
    right = [0] * N

    # The max height at the start is 1
    left[0] = min(stones[0], 1)

    # For each position, calculate the max height
    for i in range(1, N):
        left[i] = min(stones[i],
                    min(left[i-1] + 1, i + 1))
    
    # Max height at the right side of pyramid is 1
    right[N-1] = min(stones[N-1], 1)

    # For each position, calculate the max height
    for i in range(N-2, -1, -1):
        right[i] = min(stones[i],
                    min(right[i+1] + 1, N - i))

    # Find the minimum pyramid between left and right
    pyramid = [0] * N
    for i in range(N):
        pyramid[i] = min(right[i], left[i])

    # Find the max height of the pyramid
    max_idx = 0
    for i in range(N):
        if pyramid[i] > pyramid[max_idx]:
            max_idx = i

    cost = 0
    height = pyramid[max_idx]

    # Calculate the cost to construct the left half
    for x in range(max_idx, -1, -1):
        cost += stones[x] - height
        if height > 0:
            height -= 1

    # Calculate the cost of constructing the right half
    height = pyramid[max_idx] - 1 
    for x in range(max_idx + 1, N):
        cost += pyramid[x] - height
        if height > 0:
            height -= 1

    print('Minimum cost to construct the pyramid:',cost)
    return cost
    
stones = [1, 1, 3, 3, 2, 1]
constructPyramid(stones)