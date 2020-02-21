N = int(input())
A = list(map(int, input().split()))

state_plus = False
state_minus = False
state_flat = True
count = 0

for i in range(N-1):
    # print(str(A[i]) + ',' + str(A[i + 1]))
    if state_flat:
        if A[i + 1] > A[i]:
            state_flat = False
            state_plus = True
        elif A[i + 1] < A[i]:
            state_flat = False
            state_minus = True
    elif state_plus:
        if A[i] > A[i + 1]:
            state_plus = False
            state_flat = True
            count += 1
    elif state_minus:
        if A[i] < A[i + 1]:
            state_minus = False
            state_flat = True
            count += 1
    # print(count)

print(count + 1)
