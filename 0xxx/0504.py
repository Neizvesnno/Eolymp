n = int(input())

arr = []
count = 0
zap_zap_ch = 0
arr2 = []

while True:
    if not n:
        break

    arr.append(str(input()))

    n -= 1

for zap_st in arr:
    zap_str = zap_st

    for q in zap_st:
        arr2.append(q)

    while True:
        if zap_zap_ch == len(zap_str):
            break
        if arr2[zap_zap_ch] == "B":
            arr2[zap_zap_ch] = "N"
            if zap_zap_ch == 0:
                pass
            elif zap_zap_ch == 1:
                arr2[zap_zap_ch - 1] = "N"
            elif zap_zap_ch == 2:
                arr2[zap_zap_ch - 1] = "N"
                arr2[zap_zap_ch - 2] = "N"
            else:
                arr2[zap_zap_ch - 1] = "N"
                if arr2[zap_zap_ch - 2] != "S":
                    arr2[zap_zap_ch - 2] = "N"

        zap_zap_ch += 1

    zap_zap_ch = 0

    while True:
        if zap_zap_ch == len(zap_str):
            break

        if arr2[zap_zap_ch] == "S":
            arr2[zap_zap_ch] = "N"
            if zap_zap_ch == 0 and zap_zap_ch + 1 != len(arr2) and arr2[zap_zap_ch + 1] != "S":
                arr2[zap_zap_ch + 1] = "N"
            elif (zap_zap_ch + 1) == len(zap_str):
                arr2[zap_zap_ch - 1] = "N"
            else:
                if zap_zap_ch != 0:
                    arr2[zap_zap_ch - 1] = "N"
                if zap_zap_ch + 1 != len(arr2) and arr2[zap_zap_ch + 1] != "S":
                    arr2[zap_zap_ch + 1] = "N"

        zap_zap_ch += 1

    cputer = 0

    for i in arr2:
        if i == "D":
            arr2[cputer] = "N"
        cputer += 1

    for i in arr2:
        if i == "-":
            count += 1

    print(count)

    count = 0
    arr2 = []
    zap_zap_ch = 0
  
