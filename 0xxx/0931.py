n = int(input())

dob = 1
suma = 0
for num in str(n):
    dob *= int(num)
    suma += int(num)

print("%.3f" % (dob/suma))
