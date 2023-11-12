a = int(input(), 2)
b = int(input(), 2)
c = a + b
str1 = ""

while True:
    if c % 2 != 0:
        str1 += '1'
    else:
        str1 += '0'
    c = c//2

    if c == 0:
        break

str1 = str1[::-1]

print(str1)
