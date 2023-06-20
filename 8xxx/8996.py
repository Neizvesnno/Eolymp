n = str(input())

res = "" + str(n[0])
n = n[1::]
booleta = False
zap_letter = ""

while True:

    zap_letter = n[0]
    
    for i in res:
        if i == zap_letter:
            booleta = True
            break
    
    if not booleta:
        res += str(n[0])

    n = n[1::]
    booleta = False

    if not n:
        break

print(res)
