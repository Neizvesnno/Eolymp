n = str(input())
a, b = map(int, input().split())

n = n[:a] + n[(b + 1):]
                   
print(n)
