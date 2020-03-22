S = input()

s1 = S[0]
index_f = (len(S)-1)/2
s2 = S[int(index_f)-1]

index_o = (len(S)+3)/2
s3 = S[int(index_o) - 1]
index_l = len(S) - 1
s4 = S[int(index_l)]

ans = 'No'

s_f = S[0:int(index_f)]
s_l = S[int(index_o) - 1:]

# print(s1)
# print(s2)
# print(s3)
# print(s4)
# print(s_f)
# print(s_l)

if (s_f == s_l) and (s1 == s2) and (s3 == s4):
    ans = 'Yes'

print(ans)
