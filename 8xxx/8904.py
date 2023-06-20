n = int(input())
count = 1
res = 0
dis = 0

while True:
    if dis >= n:
        break
    else:
        res = 2 ** count
        count = count + 1
        dis = 2 ** count

print(res)
