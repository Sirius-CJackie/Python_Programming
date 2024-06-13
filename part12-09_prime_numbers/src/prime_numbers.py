# Write your solution here
def prime_numbers():
    num = 2
    primes = []
    while True:
        for prime in primes:
            if num % prime == 0:
                break
        else:
            primes.append(num)
            yield num
        num += 1