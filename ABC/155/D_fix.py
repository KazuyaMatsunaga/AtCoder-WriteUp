import itertools
import numpy

N, K = map(int, input().split())
A = list(map(int, input().split()))

count_negative = 0
count_zero = 0
count_positive = 0

for i in A:
    if i < 0:
        count_negative += 1
    elif i == 0:
        count_zero += 1
    else:
        count_positive += 1

count_seki_negative = count_negative * count_positive
count_seki_zero = count_zero * \
    (count_negative + count_positive) + (count_zero * (count_zero - 1)) // 2
count_seki_positive = (count_positive * (count_positive - 1)
                       ) // 2 + (count_negative * (count_negative - 1)) // 2

A = numpy.array(A, dtype=int)
ms = numpy.msort(numpy.abs(A[A < 0]))
ps = numpy.msort(A[A > 0])

print(A)
print(ms)
print(ps)
