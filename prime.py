N = int(input())

flag = True
ans = ""

if N == 1:
    ans = "YES"
else:
    for i in range(2, N):
        if N % i == 0:
            ans = "NO"
            break

print(ans)
