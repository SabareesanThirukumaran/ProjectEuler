def primeFactors(n):
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
    n = 1
    triNum = (n * (n+1)) / 2
    while not primeFactors(triNum):
        n += 1
        triNum = (n * (n+1)) / 2
    print(triNum)
    
triangles()
    
