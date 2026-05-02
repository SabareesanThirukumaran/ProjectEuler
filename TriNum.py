def primeFactors(n):
    # To see number of divisors : multiply the (exponents + 1) of each prime factor of a number.
    # To calculate prime factors of a number, keep a running counter of divisors (i.e 2, 3, 4, 5) and keep dividing by the divisor until the remaining number becomes 1
    divisor = 2
    remaining = n
    primes = {}
    while remaining != 1:
        if remaining % divisor == 0:
            remaining //= divisor
            if divisor not in primes.keys():
                primes[divisor] = 1
            else:
                primes[divisor] += 1
        else:
            divisor += 1
            
    product = 1
    for value in primes.values():
        product *= (value + 1)  
        
    return product > 500
            
def triangles():
    # Triangle number formula is n(n+1)/2
    n = 1
    triNum = (n * (n+1)) / 2
    while not primeFactors(triNum):
        n += 1
        triNum = (n * (n+1)) / 2
    print(triNum)
    
triangles()
    
