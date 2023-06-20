A = int(input())
B = int(input())
C = int(input())
if A == B and B == C:
    print("3")
elif A == B and B != C or A == C and A != B or A != B and B == C:
    print("2")
elif A < B+C and B < A+C and C < A+B:
    print("1")
else: 
    print("0")
    
