n = input()

res = 0

for kol in n:
    if kol != "-":
        res += int(kol)

print(res)
