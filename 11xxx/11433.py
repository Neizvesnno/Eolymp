import math

n = int(input())
res = 0
reglam = 0

for go in range(1, n + 1):
    reglam += math.sin(go)
    res += 1/reglam

print("%.6f" % res)
