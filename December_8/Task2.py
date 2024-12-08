# 1) Sum of Positive Numbers with Flooring

# Create a function that takes a list of numbers, including fractions, and returns the sum of all positive numbers, floored to the nearest integer.

# assert problem_2_sum_of_positive([1, -4, 7, 12]) == 20
# assert problem_2_sum_of_positive([-1.5, 2.7, -3.3, 4.8]) == 6  # floor(2.7) + floor(4.8) = 6
# assert problem_2_sum_of_positive([]) == 0
# assert problem_2_sum_of_positive([-1, -2, -3]) == 0

def function(numbers):
    total = 0
    for i in numbers:
        if i > 0:
            total += int(i)
    return total

print(function([1, -4, 7, 12]))
print(function([-1.5, 2.7, -3.3, 4.8]))
print(function([]))
print(function([-1, -2, -3]))