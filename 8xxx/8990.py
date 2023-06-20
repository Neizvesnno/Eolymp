n = str(input())

pp = ""

for i in range(0, len(n)):
    if n[i] == "a" or n[i] == "e" or n[i] == "i" or n[i] == "o" or n[i] == "u" or n[i] == "y":
        pp += str(n[i])*2
    else:
        pp += str(n[i])

print(pp)
