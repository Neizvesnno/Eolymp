a, b = map(int, input().split())
arr = list(map(int, input().split()))

if b == 0:
    print(a)
elif a == 0:
    print(0)
else:
    lenner = len(arr)
    summer = sum(arr)

    pk = summer - lenner + 1

    if (a - pk) > 0:
        print(a - pk)
    else:
        print(0)
      
