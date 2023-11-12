n = int(input())
arr = list(map(int, input().split()))

maxer = max(arr)
counter = 0

for i in arr:
    if i == maxer:
        counter += 1

print(counter)
