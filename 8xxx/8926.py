n = int(input())

res = ""

for i in str(n):
    if int(i) % 2 != 0:
        res += str(int(i) - 1)
    else:
        res += str(int(i) + 1)

print(int(res))
