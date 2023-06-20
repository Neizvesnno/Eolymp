n = int(input())
res = n

while True:
    if res % 2 == 0 or res % 3 == 0 or res % 5 == 0 or res == n:
        res = res - 1
    else:
        break

print(res)
