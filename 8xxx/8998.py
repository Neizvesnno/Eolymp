n = str(input())

mn = 255
k = 0

for i in range(len(n)):
    if mn > ord(n[i]):
        mn = ord(n[i])

for i in range(len(n)):
    if chr(mn) == n[i]:
        k += 1

print(chr(mn), k)
