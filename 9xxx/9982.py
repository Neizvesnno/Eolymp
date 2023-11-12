n = int(input())
count = 0

for i in range(0, n):
    for j in range(0, n):
        if j + 1 != n:
            print(count, end="")
        else:
            print(count)
    count += 1
  
