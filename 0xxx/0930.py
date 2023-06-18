phone = str(input())

res1 = ""
count = 0
arr = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9",]
ii = 0

while True:
    if phone[0] == "0" or phone[0] == "1" or phone[0] == "2" or phone[0] == "3" or phone[0] == "4" or phone[0] == "5" or phone[0] == "6" or phone[0] == "7" or phone[0] == "8" or phone[0] == "9":
        res1 += phone[0]

    phone = phone[1::]

    if phone == "":
        break

for i in res1:
    for j in arr:
        if i == j:
            arr.pop(ii)
        ii += 1
    ii = 0

print(len(arr))

for k in arr:
    print(k, end=" ")
