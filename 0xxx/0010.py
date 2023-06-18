N = int(input())

count = 0
rab = 0
st = N

while True:
    if count <= 0.5:
        count = count + 1/st
        rab += 1
        st = st - 1
    else:
        break

print(N - rab + 1)
