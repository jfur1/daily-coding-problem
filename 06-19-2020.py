# Given a string of parentheses, find the balanced string that can be produced from it
# using the minimum number of insertions and deletions. If there are multiple solutions, return any of them.

# For example, given "(()", you could return "(())". Given "))()(", you could return "()()()()".
# Author: John Furlong
# Description: Problems like this are similar to checking for permuations. The simplest appraoch would be
# to keep track of the offset in symmetry of the string. 
def balancedString(str):
    count = 0
    res = 0
    for i in range(len(str)):
        if(str[i] == ')'):
            count += 1
        else:
            count -= 1
        # Count must be >= -1 because of symmetry
        if(count == -1):
            count += 1
            res += 1
    nPairs = int(len(str)+(res+count)/2)

    for i in range(0, nPairs-2):
        print('()', end ='')
    print('()')
    print('Minimum # of operations to construct:', count+res)
    return #count + res

balancedString("))()(")
