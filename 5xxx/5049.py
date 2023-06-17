import re

s = str(input())

print(re.sub(r"\s+", " ", s))
