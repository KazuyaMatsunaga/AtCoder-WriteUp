A, B, C = map(int, input().split())

if (A == B and B != C) or (A == C and A != B) or (B == C and C != A):
    print('Yes')
else:
    print('No')
