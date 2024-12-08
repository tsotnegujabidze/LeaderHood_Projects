# 9) Identify Non-Prime Numbers Within a Range

# Create a function that accepts two integers, start and end, and returns a list of all non-prime numbers within the range [start, end] (inclusive). A non-prime number is defined as any integer greater than 1 that is not a prime number.



def not_primes(start, end):
    not_primes = []

    for i in range(start, end + 1):
        if i <= 1:
            not_primes.append(i)
        else:
            is_prime = True
            for som in range(2, int(i**0.5) + 1):
                if i % som == 0:
                    is_prime = False
                    break
            if not is_prime:
                not_primes.append(i)

    return not_primes
        


print(not_primes(10, 20)) # [10, 12, 14, 15, 16, 18, 20]
print(not_primes(1, 10)) # [1, 4, 6, 8, 9, 10]
print(not_primes(20, 30)) # [20, 21, 22, 24, 25, 26, 27, 28, 30]
print(not_primes(24, 25)) # [24, 25]
print(not_primes(1, 1)) # [1]