N = int(input())
T = list(map(int, input().split()))
M = int(input())
P = [list(map(int, input().split())) for i in range(M)]

sum = 0

for i in range(len(P)):
    t = T[P[i][0] - 1]
    T[P[i][0] - 1] = P[i][1]
    for j in T:
        sum += j
    print(sum)
    sum = 0
    T[P[i][0] - 1] = t
