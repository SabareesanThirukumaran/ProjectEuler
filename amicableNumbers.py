# This method calculates each amicable pair by calculating sum of divisors by looping through all numbers untilt he half of that nuumber

def sumOfDivisors(number):
    divisors = (1,)
    for i in range(2, (number//2)+1):
        if number % i == 0:
            divisors += (i, number//i)
    return sum(set(divisors))
    
amicablePairs = ()
for i in range(2, 10000):
    if i == sumOfDivisors(sumOfDivisors(i)) and i != sumOfDivisors(i):
        amicablePairs += (sorted((i, sumOfDivisors(i))),)

final = []
i = 0
while i < len(amicablePairs):
    if i % 2 == 0:
        final.append(amicablePairs[i])
    i += 1

total = 0
for pair in final:
    total += pair[0] + pair[1]
print(total)

# The more efficient method is find the proof of the formula that the sum of divisors is equal to the formula
# prime^(power+1) - 1 / prime - 1
# S if given a number, perform prime factorization (i.e divide by 2, 3, 4, 5 until the number is reduced to 1) then apply the formula for each prime and exponent
# Multiply out the results of each prime to get sum of divisors
# Proof on https://mathschallenge.net/index.php?section=faq&ref=number/sum_of_divisors