n = int(input())

chels = 0

while True:
    if (chels + 1)**3 >= n:
        break
    else:
        chels = chels + 1
        
print(chels ** 3)
