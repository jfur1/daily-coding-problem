# Create a basic sentence checker that takes in a stream of characters and determines whether they form valid sentences.
# If a sentence is valid, the program should print it out.

# We can consider a sentence valid if it conforms to the following rules:

# The sentence must start with a capital letter, followed by a lowercase letter or a space.
# All other characters must be lowercase letters, separators (,,;,:) or terminal marks (.,?,!,‽).
# There must be a single space between each word.
# The sentence must end with a terminal mark immediately following a word.

def sentenceChecker(sentence):
    seperators = [',' , ':', ';']
    terminals = ['.' , '?', '!']

    # Base Case: Is first letter capitalized?
    if ord(sentence[0]) < 64 or ord(sentence[0]) > 90:
        print("First character must be capital letter!")
        return False

    i = 0
    wordLen = 1
    terminalIdx = 1
    while i < len(sentence)-1:
        i += 1
        # Terminal 
        if sentence[i] in terminals:
            # Was the previous character invalid?
            if sentence[i-1] == ' ' or sentence[i-1] in seperators or sentence[i-1] in terminals:
                print('Invalid character preceeding terminal')
                return False
            else:
                wordLen = 0
                terminalIdx = i
                continue

        # No double spaces
        elif sentence[i] == ' ':
            if sentence[i-1] == ' ' or sentence[i+1] == ' ':
                print('No double spaces!')
                return False
            else:
                wordLen = 0
                continue
        
        # Seperator
        elif sentence[i] in seperators:
            if ord(sentence[i-1]) >= 97 and ord(sentence[i-1]) <= 122:
                continue
            else:
                print('Invalid seperator')
                return False

        # lowercase letters
        elif ord(sentence[i]) >= 97 and ord(sentence[i]) <= 122 :
            if wordLen == 1 and ord(sentence[i-1]) >= 65 and ord(sentence[i-1]) <= 90:
                wordLen += 1
                continue
            elif wordLen >= 1 and ord(sentence[i-1]) >= 97 and ord(sentence[i-1]) <= 122 and i > terminalIdx:
                wordLen += 1
                continue
            elif wordLen == 0 and sentence[i-1] == ' ':
                wordLen += 1
                continue
            else:
                print('Invalid lowercase: ', sentence[i], i)
                return False

        wordLen += 1
    # Make sure that the sentence(s) end with terminal
    if sentence[len(sentence)-1] not in terminals:
        print('Sentence must end with a terminal character!')
        return False
    else:   
        print('Valid Sentence:', sentence)
        return True
        
print('Test 1:')
sentenceChecker("Hello, my name is john.")
print('Test 2:')
sentenceChecker("Hello, my name is john .")
print('Test 3:')
sentenceChecker(" Hello, my name is john.")
print('Test 4:')
sentenceChecker("Hello,my name is john.")
print('Test 5:')
sentenceChecker("Hello, my name is john")