N = int(input())

p = 1

for i in range(N):
    i += 1
    p *= i
    p %= 10**9 + 7

print(p)
