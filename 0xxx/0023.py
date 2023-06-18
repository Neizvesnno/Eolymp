def fun(n, k):
    if n == 1: return k
    if k == 1: return -1
    if k == 2: return 2 if n % 2 == 0 else -1
    if n == 2: return k * (k - 1) 
    return k * (k - 1)**(n - 1) - fun(n - 1, k)

n,k = map(int,input().split())
print(fun(n,k))
