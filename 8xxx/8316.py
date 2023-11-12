n = str(input())

arr = [i for i in n]
arr.sort()
string = ''


for i in arr:
    string += i

print(string)
print(string[::-1])
