import sys

n = int(input())

arr = []

if n <= 0:
    print(0)
    sys.exit(0)

while True:
    arr.append(int(input()))

    n -= 1

    if not n:
        break

str1 = ""
arr1 = []

for i in arr:
    while True:
        if i % 2 != 0:
            str1 += '1'
        else:
            str1 += '0'
        i = i//2

        if i == 0:
            break
    str1 = str1[::-1]
    arr1.append(str1)
    str1 = ""

count = 0

for i in arr1:
    i = str(i)
    if len(str(i)) >= 2:
        if int(str(i[::-1])[1]) % 2 != 0:
            count += 1

print(count)
