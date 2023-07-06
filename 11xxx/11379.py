a, b, c = map(int, input().split())

res = 0

if a*3 >= b:
    while c > 2:
    
        c -= 3
        res += b

for i in range(0, c):
    res += a

print(res)
