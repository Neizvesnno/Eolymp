a, m = map(int,input().split())

pir = 0
s = 0

while True:
    if s + a * 2 == m:
        pir += 1
        break
    else:
        pir += 1
        s += a
        a += 1

print(pir)
