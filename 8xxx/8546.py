n = int(input())
sum = 0
for S in range(1, n + 1):
    sum += 1 / (S * (S + 1))

print("%.7f"%sum)
