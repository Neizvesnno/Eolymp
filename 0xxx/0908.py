n = int(input())
arr = list(map(int, input().split()))[:n:]

count = 0
res = 0

for i in arr:
    if int(i) % 6 == 0 and int(i) > 0:
        res += int(i)
        count += 1

print(count, res)
