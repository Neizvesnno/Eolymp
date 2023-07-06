n = int(input())

if n < 8 or n > 30:
    print("Impossible")
    exit(0)

pb = 0
arr1 = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
arr = [6, 2, 5, 5, 4, 5, 6, 3, 7, 6]
koloritm = 0
zap_1 = 0
zap_2 = 0
zap_3 = 0
zap_4 = 0
return1 = False
prbn = 10

for first in range(0, 3):
    pb += arr[first]
    zap_1 = first
    if first == 2:
        prbn = 4
    for second in range(0, prbn):
        pb += arr[second]
        zap_2 = second
        for third in range(0, 6):
            pb += arr[third]
            zap_3 = third
            for forty in range(0, 10):
                return1 = False
                pb += arr[forty]
                zap_4 = forty
                if pb == n and not return1:
                    break
                return1 = True
                pb -= arr[forty]
            if pb == n and not return1:
                break
            pb -= arr[third]
        if pb == n and not return1:
            break
        pb -= arr[second]
    if pb == n and not return1:
        break
    pb -= arr[first]
    if str(f"{zap_1}{zap_2}:{zap_3}{zap_4}") == "23:59" and pb != n:
        koloritm += 1

if koloritm == 0:
    print(f'{zap_1}{zap_2}:{zap_3}{zap_4}')
else:
    print("Impossible")
