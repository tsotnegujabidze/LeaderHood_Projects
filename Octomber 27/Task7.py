# Create a program that receives an integer n and returns the first n numbers in the Fibonacci sequence. The sequence starts with 0 and 1, and each subsequent number is the sum of the previous two.

def something(num):
    if num <= 0:
        return []
    elif num == 1:
        return [0]
    else:
        seq = [0, 1]
        for i in range(2, num):
            seq.append(seq[i - 1] + seq[i - 2])
        return seq

print(something(5)) # 5 --> [0, 1, 1, 2, 3]

print(something(7)) # 7 --> [0, 1, 1, 2, 3, 5, 8]