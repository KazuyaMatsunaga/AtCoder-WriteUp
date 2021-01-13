import numpy as np

N = int(input())
A = [int(i) for i in input().split()]
B = [int(i) for i in input().split()]

ans = np.dot(A, B)

if ans == 0:
    print("Yes")
else:
    print("No")
