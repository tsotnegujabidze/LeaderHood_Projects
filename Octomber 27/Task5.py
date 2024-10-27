# Create a program that checks if a given string is a palindrome (reads the same forward and backward). The function should ignore spaces, punctuation, and capitalization.

def palindrome(word):
    no_to_spaces = word.lower().replace(" ", "")
    return no_to_spaces == no_to_spaces[::-1]

print(palindrome("A man a plan a canal Panama")) # True

print(palindrome("Hello")) # False