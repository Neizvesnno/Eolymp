n, k, m = map(int, input().split())

while True:

    if n - k <= 0:
        break

    n -= k
    k += m

if n == 0:
    print(k)
else:
    print(n)
