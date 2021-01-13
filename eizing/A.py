L, R, d = map(int, input().split())

long = R - L

count = 0

for i in range(long + 1):
    value = i + L
    if value % d == 0:
        count += 1

print(count)
