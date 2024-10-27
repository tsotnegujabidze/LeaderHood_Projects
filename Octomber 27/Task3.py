# Create a program that receives a list and removes duplicate elements while maintaining the original order.

def remove_dublicate(list):
    list2 = []
    for i in list:
        if i not in list2:
            list2.append(i)
    return list2

print(remove_dublicate([1, 2, 2, 3, 4, 4, 5])) # [1, 2, 3, 4, 5]

print(remove_dublicate(['a', 'b', 'a', 'c'])) # ['a', 'b', 'c']

