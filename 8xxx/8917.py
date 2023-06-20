n = int(input())

count = 1

while True:
    if n > 2 ** count:
        print(2 ** count, end=" ")
        count += 1
    else:
        break
        
