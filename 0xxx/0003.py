n = int(input())
ste = 0.5
a = int((n ** (1 / 3)) + ste)
b = int(((n / a) ** ste) + ste)
c = int(n / (a * b))
sl = a * (b + 1) + b * (a + 1)
sl2 = (a + 1) * (b + 1)
v = sl * (c + 1) + sl2 * c
res = n - a * b * c
if res != 0:
    if n > 4:
        d = int(res ** ste)
        e = int(res ** ste)
        op = (d, e)
        while d * e < res:
            op = (d, e)
            if d < e:
                d += 1
            else:
                e += 1
        d, e = op
        v += d * (e + 1) + e * (d + 1) + (d + 1) * (e + 1)
        res -= d * e
        if res != 0:
            v += 3 * (res - 1) + 5
    else:
        v += 8
print(int(v))
