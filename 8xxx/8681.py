n = int(input())
res = 1
while True:
    if n > 0:
        a = n % 10
        if a != 0 :
           res = a * res
        n = n//10
    else:
        break

print(res)
