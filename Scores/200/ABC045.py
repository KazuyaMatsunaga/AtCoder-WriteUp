S = [input() for i in range(3)]

flag = True
num_who = 0

while flag:
    if num_who == 0:
        if S[num_who].startswith('a'):
            S[num_who] = S[num_who][1:]
        elif S[num_who].startswith('b'):
            S[num_who] = S[num_who][1:]
            num_who = 1
        elif S[num_who].startswith('c'):
            S[num_who] = S[num_who][1:]
            num_who = 2
        else:
            print("A")
            flag = False
    elif num_who == 1:
        if S[num_who].startswith('a'):
            S[num_who] = S[num_who][1:]
            num_who = 0
        elif S[num_who].startswith('b'):
            S[num_who] = S[num_who][1:]
        elif S[num_who].startswith('c'):
            S[num_who] = S[num_who][1:]
            num_who = 2
        else:
            print("B")
            flag = False
    elif num_who == 2:
        if S[num_who].startswith('a'):
            S[num_who] = S[num_who][1:]
            num_who = 0
        elif S[num_who].startswith('b'):
            S[num_who] = S[num_who][1:]
            num_who = 1
        elif S[num_who].startswith('c'):
            S[num_who] = S[num_who][1:]
        else:
            print("C")
            flag = False
