n = int(input()) - 1
arr = list(map(int, input().split()))

if len(arr) == 2:
    print(0)
else:
    counter = 0
    cc = 1
    while True:
        zap_el = arr[cc]

        if arr[cc - 1] < zap_el and arr[cc + 1] < zap_el:
            counter += 1

        cc += 1

        if cc == n:
            break

    print(counter)
  
