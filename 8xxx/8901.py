n = input()
len1 = len(n)
count = 1

if int(n) < 0:
    len1 = len1 - 1

while True:
    if len1 > 0:
        len1 = len1 - 1
        count = count * 10
    else:
        break

if int(n) < 0:
    count = 0 - count

print(count)
