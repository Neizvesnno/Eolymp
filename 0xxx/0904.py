n = input()

v = [int(s) for s in input().split()]
ne = []
for kol in v:
    if kol < 0:
        ne.append(kol)
    if kol >= 0:
        kol = kol + 2
        ne.append(kol)
print(*ne)
