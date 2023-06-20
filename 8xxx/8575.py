n = int(input())

a = n // 500
n = n - 500 * a
b = n // 200
n = n - 200 * b
c = n // 100
n = n - 100 * c
d = n // 50
n = n - 50 * d
e = n // 20
n = n - 20 * e
f = n // 10
n = n - 10 * f
g = n // 5
n = n - 5 * g
k = n // 2
n = n - 2 * k
v = n // 1
n = n - 1 * v

print(a + b + c + d + e + f + g + k + v)
