a, b = map(int, input().split())

def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

def nsk(a, b):
    return a * b // gcd(a, b)

print(nsk(a, b))
