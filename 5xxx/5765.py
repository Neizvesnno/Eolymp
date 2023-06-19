n, k = map(int, input().split())
n -= k

if n == 0:
  print (1, 1)
else:
    q = n // k
    if n % k != 0:
        q += 1
    print(q + 1, n + 1)
  
