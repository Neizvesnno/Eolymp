n = str(input())

count = 0

if n[0] == '-':
    n = n[1::]

while True:
    count += 1
    print(f'{n[0]}{count}', end="")
    n = n[1::]
    if not n:
        break
      
