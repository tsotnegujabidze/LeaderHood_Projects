# 1) Sum of Positive Numbers

#Challenge:
# Create a function that takes a list of numbers and returns the sum of all positive numbers.

def sum_of_positive_numbers(numbers):
    sum = 0
    for num in numbers:
        if num > 0:
            sum += num
    return sum

print(sum_of_positive_numbers([1, -4, 7, 12]))

print(sum_of_positive_numbers([-1, -2, -3, -4]))

print(sum_of_positive_numbers([]))