N, K = map(int, input().split())

ways = 1

ways *= K

ways *= pow(K - 1, N - 1)

print(ways)
