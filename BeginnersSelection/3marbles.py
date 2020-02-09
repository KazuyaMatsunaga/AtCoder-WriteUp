def marble_count(list):
    count = 0
    for l in list:
        if l == 1:
            count += 1
    return count

list = map(int,input())

print(marble_count(list))
