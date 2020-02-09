N = int(input())

A = list(map(int, input().split()))

count = 0
i = 0
j = 0

while i == 0:
    for a in A:
        if a % 2 == 1:
            i = 1
            break
        else:
            a = a / 2
            A[j] = a
            j += 1
    j = 0
    if i == 0:
        count += 1

print(count)
