m = int(input())

count = 0

for figures in range(100, 1000):
    if (int(str(figures)[0]) + int(str(figures)[1]) + int(str(figures)[2])) == m\
            and (int(str(figures)[0]) % 2 != 0 and int(str(figures)[1]) % 2 != 0 and int(str(figures)[2]) % 2 != 0):
        count += figures

print(count)
