from itertools import permutations

n = int(input())

s = str(abs(n))
i = list(map("".join, permutations(s)))
i = [int(x) for x in i if int(x)>99]

if n>0:
    print(min(i))
else:
    print(-max(i))
  
