str1 = str(input())
str2 = str(input())

lener = len(str1 + str2)
zap_lener = lener

arr = []

while zap_lener != 0:
    arr.append("")
    zap_lener -= 1

asaria = 1

while True:
    if asaria % 2 != 0:
        arr[asaria - 1] = str1[0]
        str1 = str1[1::]
    elif asaria % 2 == 0:
        arr[asaria - 1] = str2[0]
        str2 = str2[1::]

    asaria += 1

    if asaria - 1 == lener:
        break

res = ''
for i in arr:
    res += i

print(res)
