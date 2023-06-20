n = input()

len_n = len(n)
count = 0
kol = 0

for i in range(0, len_n):
    if int(n[i]) % 2 == 0:
        count += int(n[i])
        kol = 1

if kol == 0:
    print(-1)
else:
    print(count)
  
