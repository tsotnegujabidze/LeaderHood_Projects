# 6) Find Intersection of Two Lists

# Write a function to find the common elements between two lists.

def find_intersection(list1, list2):
    new = []
    for i in list1:
        if i in list2:
            new.append(i)
    return new

print(find_intersection([1, 2, 3], [2, 3, 4]))
print(find_intersection([1, 1, 2], [1, 3]))
print(find_intersection([], [1, 2]))