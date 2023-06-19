num = input().strip()

product = 1
found = False

for digit in num:
    if digit.isdigit() and int(digit) % 2 == 0:
        product *= int(digit)
        found = True

if found:
    print(product)
else:
    print(-1)
  
