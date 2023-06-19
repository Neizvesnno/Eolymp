a = int(input())

res = 0
for b in range(100):
    c = a - b
    if 0 <= c <= 99:
        res += 1

print(res)
