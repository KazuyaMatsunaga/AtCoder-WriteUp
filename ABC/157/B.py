A = [list(map(int, input().split())) for i in range(3)]
N = int(input())
B = [int(input()) for i in range(N)]

for i in range(N):
    for j in range(3):
        if B[i] in A[j]:
            index_v = A[j].index(B[i])
            A[j][index_v] = 0

if (A[0][0] == 0 and A[0][1] == 0 and A[0][2] == 0) or (A[1][0] == 0 and A[1][1] == 0 and A[1][2] == 0) or (A[2][0] == 0 and A[2][1] == 0 and A[2][2] == 0) or (A[0][0] == 0 and A[1][0] == 0 and A[2][0] == 0) or (A[0][1] == 0 and A[1][1] == 0 and A[2][1] == 0) or (A[0][2] == 0 and A[1][2] == 0 and A[2][2] == 0) or (A[0][0] == 0 and A[1][1] == 0 and A[2][2] == 0) or (A[0][2] == 0 and A[1][1] == 0 and A[2][0] == 0):
    print('Yes')
else:
    print('No')
