# Write a function that takes a maximum bound and returns all primes up to and including the maximum bound.

def prime(max):
    primes = []
    for num in range(2, max + 1):
        is_prime = True
        for i in range(2, int(num**0.5) + 1):
            if num % i == 0:
                is_prime = False
                break
        if is_prime:
            primes.append(num)
    return primes

print(prime(11)) # 11 => [2, 3, 5, 7, 11]
