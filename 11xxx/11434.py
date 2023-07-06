n = int(input())

if not n:
    print(0)
    exit(0)

res = 1

for go in range(1, n + 1):
    res *= (1 + 1/go)

print("%.6f" % res)
