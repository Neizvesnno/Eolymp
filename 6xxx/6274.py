m, n = map(int,input().split())

pir = 0 
count = 1

while True:
    if count <= m and m > n:
        pir = pir + 1
        m = m - count
        count = count + 1
    else:
        break

print(pir)
