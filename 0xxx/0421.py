I,k = map(int,input().split())

count = 0

while True:
    if I > 1:
        I = I / k
        if I > 1:
            count = count + 1
    else:
        break
      
print(count)
