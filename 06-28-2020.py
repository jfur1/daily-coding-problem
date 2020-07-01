# Author: John Furlong
# Help from GeeksforGeeks
# Given a string and a set of characters, return the shortest substring containing all the characters in the set.

# For example, given the string "figehaeci" and the set of characters {a, e, i}, you should return "aeci".

# If there is no substring containing all the characters in the set, return null.

def shortestSubstring(word, chars):
    len1 = len(word)
    len2 = len(chars)

    # Check if the word lentgth is less than the set of characters
    if len1 < len2:
        print("No such window exists.")
        return 

    hash_pat = [0] * 256
    hash_str = [0] * 256

    # Store the occurence of characters from the set
    for i in range(0, len2):
        hash_pat[ord(chars[i])] += 1

    start, start_idx, min_len = 0, -1, float('inf')

    # Begin traversal of the word
    count = 0
    for j in range(0, len1):

        # Count the occurence of characters from the word
        hash_str[ord(word[j])] += 1

        # Of the string's character match with the character form the set, then increment
        if (hash_pat[ord(word[j])] != 0 and 
            hash_str[ord(word[j])] <= hash_pat[ord(word[j])]):
            count += 1

        # If all the characters are matched
        if count == len2:

            # Try and minimize the window (Check if any character is occurring
            # more number of times than its occurrence pattern, if yes then remove
            # it from strating and also remove the useless characters)
            while(hash_str[ord(word[start])] > hash_pat[ord(word[start])] 
                    or hash_pat[ord(word[start])] == 0):

                if (hash_str[ord(word[start])] > hash_pat[ord(word[start])]):
                    hash_str[ord(word[start])] -= 1
                    start += 1

            # Update the window size
            len_window = j - start + 1
            if min_len > len_window:
                min_len = len_window
                start_idx = start
    
    # If no window is found
    if start_idx == -1:
        print("No such window exists")
        return
    
    # Return the substring starting from the start_idx and length min_len
    return word[start_idx : start_idx + min_len]

word = "figehaeci"
#chars = ['a', 'e', 'i']
chars = 'aei'

print(shortestSubstring(word, chars))