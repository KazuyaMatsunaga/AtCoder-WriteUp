x, y = map(int, input().split())

l1 = [1, 3, 5, 7, 8, 10, 12]
l2 = [4, 6, 9, 11]
l3 = [2]

if x in l1:
    if y in l1:
        print("Yes")
    else:
        print("No")
elif x in l2:
    if y in l2:
        print("Yes")
    else:
        print("No")
else:
    print("No")
