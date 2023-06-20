n = int(input()) 

suma = 0 
x1 = 10 ** (n-1) 
x2 = x1 - (x1 / 10 * 2) 
suma = x1 + x2 

while True: 
    x2 = x2 - x2 / 10 
    if x2.is_integer(): 
        suma += x2 
    else: 
        break 

print(int(suma))
