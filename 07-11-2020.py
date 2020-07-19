# You're given a string consisting solely of (, ), and *. * can represent either a (, ), or an empty string. 
# Determine whether the parentheses are balanced.

# For example, (()* and (*) are balanced. )*( is not balanced.

def balanced(str):
    low = high = 0
    for c in str:
        low += 1 if c == '(' else -1
        high += 1 if c != ')' else -1
        if high < 0: break
        low = max(low, 0)
    return low == 0

string = ")*("
string2 = "(()*"
string3 = "(*)"
print(string, ':', balanced(string))
print(string2, ':', balanced(string2))
print(string3, ':', balanced(string3))

# Time Complexity: O(n) where n is the length of the string
# Space Complexity: O(1), the space used by the high and low pointers.