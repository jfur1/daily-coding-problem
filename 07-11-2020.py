# You're given a string consisting solely of (, ), and *. * can represent either a (, ), or an empty string. 
# Determine whether the parentheses are balanced.

# For example, (()* and (*) are balanced. )*( is not balanced.

def balanced(str):
    low = high = 0
    for i in range(0, len(str)):
        if str[i] == ')':
            high -= 1
            if low > 0:
                low -= 1
        elif str[i] == '(':
            high += 1
            low += 1
        elif str[i] == '*':
            if low > 0:
                low -= 1
            high += 1
    if low == 0: return True 
    else: return False

string = "((*"
print(balanced(string))
