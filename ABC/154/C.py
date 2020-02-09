import collections

N = int(input())
A = list(map(int, input().split()))

count = collections.Counter(A)

s = "YES"

for v in count.values():
    if v >= 2:
        s = "NO"
        break

print(s)
