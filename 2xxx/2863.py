n = int(input())

count = 0
while True:
    if count <= n:
        count += 1
        if n % count == 0 and count % 2 != 0:
            print(count)
    else:
        break
      
