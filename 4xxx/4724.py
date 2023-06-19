n = str(input())

st1 = ""
st2 = ""

for i in range(0, len(n)):
    if i%2 == 0:
        st1 += n[i]
    else:
        st2 += n[i]

print(n[2])
print(n[-2])
print(n[:5])
print(n[:-2])
print(st1)
print(st2)
print(n[::-1])
print((n[::-1])[::2])
print(len(n))
