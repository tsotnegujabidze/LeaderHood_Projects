# 8) Longest Consecutive Sequence

# Given an unsorted array of integers, find the length of the longest consecutive elements sequence.

def longest_consecutive(nums):
    sortted = set(nums)
    max_lenght = 0
    for i in sortted:
        if i - 1 not in sortted:
            something = i
            new_lenght = 1

            while something + 1 in sortted:
                something += 1
                new_lenght += 1
            
            max_lenght = max(max_lenght, new_lenght)
    return max_lenght

print(longest_consecutive([100, 4, 200, 1, 3, 2])) # 4

print(longest_consecutive([0, 0])) # 1

print(longest_consecutive([9, 1, 4, 7, 3, 2, 8, 5, 6])) # 9

