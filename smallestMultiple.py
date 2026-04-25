# LCM formula --> abs(a*b) / gcd(a,b)
# GCD formula --> gcd(a,b) = while b > 0: a = b, b = a%b

def gcd(a,b):
    while b > 0:
        temp = a
        a = b
        b = temp % b
    return a

def lcm(a,b):
    return abs(a*b) // gcd(a,b)

result = 1
for i in range(1,21):
    result = lcm(result, i)

print(result)