N, M = map(int, input().split())

s_l = []
c_l = []

for i in range(M):
    s, c = input().split()
    s_l.append(int(s))
    c_l.append(int(c))

v_l = [-1] * N
seki = 10 ** (N - 1)

sum = 0

for i in range(M):
    if v_l[s_l[i]] > c_l[i]:
        v_l[s_l[i]] > c_l[i]


if ((v_l[0] == 0) and (not N == 1)):
    print(-1)
else:
    for i in range(N):
        sum += v_l[i] * seki
        seki //= 10
    print(sum)
