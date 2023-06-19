n = int(input())

count = 0
res = 0

while True:
    if count <= n:
        count += 1
        if n % count == 0:
            res += 1
    else:
        break

print(res)
