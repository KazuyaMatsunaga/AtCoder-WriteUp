A, B = map(int, input().split())

sum_A = 0
sum_B = 0

flag = True

while(flag):
    l_A = A % 10
    sum_A += l_A
    ans_A = A // 10
    if ans_A == 0:
        flag = False
    A = ans_A

flag = True

while(flag):
    l_B = B % 10
    sum_B += l_B
    ans_B = B // 10
    if ans_B == 0:
        flag = False
    B = ans_B

if sum_A >= sum_B:
    print(sum_A)
else:
    print(sum_B)
