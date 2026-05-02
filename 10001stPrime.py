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

# To calculate primes -->
# Start from the first prime number (2) until the root of the current possible prime. Check if any of those numbers can divide evenly into the current number and if it does, it isnt a prime
# So we can stop checking and move to the next