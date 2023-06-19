import math

a, b, c = map(int, input().split())

d = math.floor(math.sqrt(a*a + b*b + c*c))

print(d)
