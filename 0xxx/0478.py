a,b,c = map(int,input().split())

cubes = a * b * c
total = cubes * 6
original = 2 * (a * b + a * c + b * c)
s = total - original

print (cubes, s)
