num = input().strip()

for i in range(len(num) // 2):
    if num[i] != num[len(num) - i - 1]:
        print("No")
        break
else:
    print("Yes")
