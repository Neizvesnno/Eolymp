s = str(input())

res = 0

for i in s:
    if i.isupper():
        res += 1

print(res)
