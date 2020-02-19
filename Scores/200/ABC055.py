N = int(input())

p = 1

for i in range(N):
    i += 1
    p *= i


print(p % (pow(10, 9) + 7))
