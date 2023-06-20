n = str(input())
lener = len(n)

if len(n) % 2 != 0:
    print("no")
    exit(0)

pol = lener / 2
for i in range(0, int(pol)):
    if n[int(i - pol)] == n[i]:
        pass
    else:
        print("no")
        exit(0)

print('yes')
