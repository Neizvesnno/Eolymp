a, b, c = map(int, input().split())
x, y, z = map(int, input().split())

print(min(x//a, y//b, z//c))
