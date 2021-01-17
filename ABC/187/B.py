N = int(input())

A = [tuple(map(int, input().split())) for i in range(N)]

count = 0

for i in range(N):
    for j in range(i):
        if -1 <= ((A[i][1] - A[j][1]) / (A[i][0] - A[j][0])) and ((A[i][1] - A[j][1]) / (A[i][0] - A[j][0])) <= 1:
            count += 1

print(count)
