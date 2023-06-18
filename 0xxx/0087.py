commands = str(input())

cord = [0]
s = 0

for i in commands:
    if str(i) == "R":
        s += 1
        cord.append(s)

    elif str(i) == "L":
        s -= 1
        cord.append(s)

booleta = False
cord.sort()
arr = [cord[0]]
arr = arr[1::]
new_zap = None
kk = 1

while True:
    new_zap = cord[0]

    for i in arr:
        if new_zap == i:
            booleta = True
            break

    if not booleta:
        arr.append(new_zap)

    booleta = False
    cord = cord[1::]
    kk += 1

    if not cord:
        break

print(len(arr))
