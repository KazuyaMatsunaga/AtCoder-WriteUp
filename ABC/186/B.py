H, W = map(int, input().split())

A = [list(map(int, input().split())) for i in range(H)]

min = A[0][0]

ans = 0

for i in A:
    for j in i:
        if min > j:
            min = j

for i in A:
    for j in i:
        if min != j:
            count = j - min
            ans += count

print(ans)
