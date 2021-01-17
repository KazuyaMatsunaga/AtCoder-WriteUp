N, M, T = map(int, input().split())

remain = N
prev = 0

ans = "Yes"

for _ in range(M):
    a, b = map(int, input().split())
    remain -= a - prev
    if remain <= 0:
        ans = "No"
    remain += b - a
    remain = min(N, remain)
    prev = b

remain -= (T - prev)
if remain <= 0:
    ans = "No"

print(ans)
