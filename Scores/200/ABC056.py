W, a, b = map(int, input().split())

d = 0

if a > (b + W):
    d = a - (b + W)
else:
    d = b - (a + W)

if d < 0:
    print(0)
else:
    print(d)
