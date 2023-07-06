n = int(input())

arr_truelor = []
enderation_bool = False

while True:

    str_zap = str(input())

    if len(str_zap) >= 3:
        for i in range(0, len(str_zap) - 2):
            if str_zap[i] + str_zap[i + 1] + str_zap[i + 2] == "BSM":
                enderation_bool = True
                break

    if enderation_bool:
        arr_truelor.append("YES")
    else:
        arr_truelor.append("NO")

    n -= 1
    enderation_bool = False

    if not n:
        break

for i in arr_truelor:
    print(i)
  
