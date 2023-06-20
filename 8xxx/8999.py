n = str(input())

maximum = 0

for i in range(0, len(n)):
    if maximum < ord(n[i]):
        maximum = ord(n[i])
        
print(chr(maximum), n.count(str(chr(maximum))))
