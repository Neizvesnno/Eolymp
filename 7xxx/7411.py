n = input()

op = 0

if n[1] == '+':
    op = 1
else:
    op = -1


if n[4] == 'x':
    x = int(n[0]) + op * int(n[2])
    print(x)
    exit(0)
    
if n[0] == 'x':
    a = int(n[2])
    a1 = op
    x1 = 1
else:
    a = int(n[0])
    a1 = 1
    x1 = op

b = int(n[4])

res = (b - a1 * a) * x1

print(res)
