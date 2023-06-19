a, b = map(int, input().split())


def evklid(k, v):
    if k % v == 0:
        return v
    else:
        return evklid(v, k % v)


print(evklid(a, b))
