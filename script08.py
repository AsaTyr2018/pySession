def prime_generator():
    num = 2
    primes = []
    while True:
        is_prime = True
        for p in primes:
            if num % p == 0:
                is_prime = False
                break
        if is_prime:
            primes.append(num)
            yield num
        num += 1

"""
|
|
|
"""

def take(n, iterable):
    result = []
    for _, value in zip(range(n), iterable):
        result.append(value)
    return result
