q = list(map(int, input().split()))

w = q[0] + q[1]
e = 0

while True:

    if not w >= q[2]:
        break

    e += 1
    w -= q[2]
    w += 1

print(e)
