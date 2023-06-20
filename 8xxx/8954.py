n = int(input())

arr = []

while True:

    if n != 0:
        n -= 1
    else:
        break

    m = int(input())

    arr.append(m)

while True:

    print(arr[-1], end=" ")

    arr = arr[:(len(arr) - 1)]

    if not arr:
        break
      
