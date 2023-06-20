s = input()

len_s = len(s)
len_p = len(s[0::2])

print(s[1] + s[3] + s[9])
print(s[0] + s[1] + s[-1])
print(s[-5:-1] + s[-1])
print(s[0:len_s - 4])
print(s[0::2])
print(len_p)
print(s[::-2])
