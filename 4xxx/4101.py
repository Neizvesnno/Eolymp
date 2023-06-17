n = int(input())
count = 0
prb = 100
k1 = 0
k2 = 0
k3 = 0
lis1 = []
while True:
    if 100 <= prb <= 999:
        k1 = prb % 10
        k2 = prb // 10 % 10
        k3 = prb // 100 % 10
        res = k1 + k2 + k3
        if res == n:
            ch = (k3 * 100 + k2 * 10 + k1)
            count = count + 1
            lis1.append(ch)

    else:
        break
    prb = prb + 1

print(count)

lis1 = sorted(lis1)

for i in range(len(lis1)):
    result = lis1[i]
    print(result)
