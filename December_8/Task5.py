# 5) Check if Two Strings are Anagrams

# Write a function to check if two strings are anagrams (contain the same characters in the same frequency).


def checking(num1, num2):
    num1 = num1.replace(' ', '').lower()
    num2 = num2.replace(' ', '').lower()
    return sorted(num1) == sorted(num2)

print(checking('listen', 'silent')) # True
print(checking("hello", "world")) # False
print(checking("triangle", "integral")) # True


