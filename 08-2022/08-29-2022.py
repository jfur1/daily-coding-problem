# Good morning! Here's your coding interview problem for today.

# This problem was asked by Facebook.

# A builder is looking to build a row of N houses that can be of K different colors. He has a goal of minimizing cost while ensuring that no two neighboring houses are of the same color.

# Given an N by K matrix where the nth row and kth column represents the cost to build the nth house with kth color, return the minimum cost which achieves this goal.
# -----------------------------

# Function to find the minimum cost of
# coloring the houses such that no two
# adjacent houses has the same color
def minCost(costs, N):
   
    # Corner Case
    if (N == 0):
        return 0
 
    # Auxiliary 2D dp array
    dp = [[0 for i in range(3)] for j in range(3)]
 
    # Base Case
    dp[0][0] = costs[0][0]
    dp[0][1] = costs[0][1]
    dp[0][2] = costs[0][2]
 
    for i in range(1, N, 1):
       
        # If current house is colored
        # with red the take min cost of
        # previous houses colored with
        # (blue and green)
        dp[i][0] = min(dp[i - 1][1], dp[i - 1][2]) + costs[i][0]
 
        # If current house is colored
        # with blue the take min cost of
        # previous houses colored with
        # (red and green)
        dp[i][1] = min(dp[i - 1][0], dp[i - 1][2]) + costs[i][1]
 
        # If current house is colored
        # with green the take min cost of
        # previous houses colored with
        # (red and blue)
        dp[i][2] = min(dp[i - 1][0], dp[i - 1][1]) + costs[i][2]
 
    # Print the min cost of the
    # last painted house
    print(min(dp[N - 1][0], min(dp[N - 1][1],dp[N - 1][2])))
 
# Driver Code
if __name__ == '__main__':
    costs = [[14, 2, 11],
             [11, 14, 5],
             [14, 3, 10]]
    N = len(costs)
     
    # Function Call
    minCost(costs, N)

# Input: N = 3, cost[][3] = {{14, 2, 11}, {11, 14, 5}, {14, 3, 10}}
# Output: 10
# Explanation: 
# Paint house 0 as blue. Cost = 2. Paint house 1 as green. Cost = 5. Paint house 2 as blue. Cost = 3.
# Therefore, the total cost = 2 + 5 + 3 = 10.

