s = input()
a, b = map(int, input().split())

print (b - a + 2)
for i in range(a, b):
    print(s[i:b])
  
