primes = []
current = 2
while len(primes) != 10001:
    is_prime = True
    for i in range(2, int(current**0.5) + 1):
        if current % i == 0:
            is_prime = False
            break
    
    if is_prime:
        primes.append(current)
    current += 1

print(primes[-1])