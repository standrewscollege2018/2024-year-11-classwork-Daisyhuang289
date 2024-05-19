def sieve_of_eratosthenes(limit):
    primes = []
    is_prime = [True] * (limit + 1)
    is_prime[0] = is_prime[1] = False
    
    for num in range(2, int(limit**0.5) + 1):
        if is_prime[num]:
            primes.append(num)
            for multiple in range(num*num, limit + 1, num):
                is_prime[multiple] = False
                
    for num in range(int(limit**0.5) + 1, limit + 1):
        if is_prime[num]:
            primes.append(num)
    
    return primes

limit = 2000000
primes = sieve_of_eratosthenes(limit)
print(sum(primes))
