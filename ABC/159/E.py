H, W, K = map(int, input().split())

s_l = []
S = []
sum = 0

for i in range(H):
    s = input()
    for j in s:
        s_l.append(int(j))
        if int(j) == 1:
            sum += 1
    S.append(s_l)
    s_l = []

print(sum)
print(S)

if sum <= K:
    ans = 0
else:


print(sum//K)
