N = int(input())

flag = True
count = 0
money = 0

while(flag):
    money += 1000
    count += 1
    if money >= N:
        flag = False

print(count * 1000 - N)
