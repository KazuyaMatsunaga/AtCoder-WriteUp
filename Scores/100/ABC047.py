a, b, c = map(int, input().split())

candies = []
candies.append(a)
candies.append(b)
candies.append(c)

max_candy = max(candies)

candies.remove(max_candy)

if sum(candies) == max_candy:
    print("Yes")
else:
    print("No")
