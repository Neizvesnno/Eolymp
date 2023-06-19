s = str(input())
i, j = map(int, input().split())

print(s[:(i - 1)] + (s[(i - 1):j])[::-1] + s[j:])
