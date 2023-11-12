n = int(input())
arr = list(map(int, input().split()))

lenner = len(arr)
summer = sum(arr)

sk = summer/lenner

lenner2 = 0
summer2 = 0

for i in arr:
    if i > sk:
        summer2 += i
        lenner2 += 1

print(summer2, lenner2)
