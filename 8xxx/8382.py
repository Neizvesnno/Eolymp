n = str(input())

op_sum = 0
pch_1 = False
pch_2 = False
pch_3 = False
pch_4 = False

for i in n:
    if not pch_1:
        for j in range(65, 91):
            if ord(i) == j:
                op_sum += 1
                pch_1 = True
                break
    if not pch_2:
        for j in range(97, 123):
            if ord(i) == j:
                op_sum += 1
                pch_2 = True
                break
    if not pch_3:
        for j in range(48, 58):
            if ord(i) == j:
                op_sum += 1
                pch_3 = True
                break
    if not pch_4:
        for j in range(33, 44):
            if ord(i) == j:
                op_sum += 1
                pch_4 = True
                break

if len(n) >= 8:
    op_sum += 1

print(op_sum)
