# 3) Find the Missing Number

# Create a function to find the missing number in a list of integers from 1 to n.

def find_missing_number(numbers):
    if len(numbers) == 1 or len(numbers) == 0:
        return []
    n = len(numbers) + 1
    expected_sum = (n * (n + 1)) // 2
    actual_sum = sum(numbers)
    return expected_sum - actual_sum


print(find_missing_number([1, 2, 4, 5])) # 3

print(find_missing_number([3, 5, 6, 1, 2])) # 4

print(find_missing_number([2])) # []