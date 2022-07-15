import string

def alphabet(n):
    lookup = dict()
    letters = string.ascii_letters
    for i in range(n):
        lookup[i] = letters[i]
    return lookup

# Build a dictionary to lookup the first n lowercase letters of the alphabet. The return value of alphabet() should be a dictionary where the keys are numbers 0-25

# Hint: string.ascii_letters = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
# We have already imported the string library for you.returns a string constant containing the entire lowercase alphabet (26 letters).

# Note: there are no performance gains to be gained from this kind of approach in the real world...it is just intended for practice working with the dictionary data structure :)

# Test cases:
lowercase = alphabet(26)
print(lowercase[9]) # j

both_cases = alphabet(52)
print(both_cases[51]) # Z