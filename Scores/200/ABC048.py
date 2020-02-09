a, b, x = map(int, input().split())

if (a - 1) < 0:
    count_a = 0
else:
    count_a = (a - 1) // x + 1

count_b = b // x + 1

print(count_b - count_a)
