import operator as op
from functools import reduce 

def ncr(n, r):
    r = min(r, n-r)
    if r == 0: return 1
    numer = reduce(op.mul, range(n, n-r, -1))
    denom = reduce(op.mul, range(1, r+1))
    return numer//denom

Rang = int(input())
for t in range(Rang):
  n, k = map(int,input().split())
  print(ncr(n, k))
