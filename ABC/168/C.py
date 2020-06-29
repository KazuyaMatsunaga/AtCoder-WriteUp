import math

A, B, H, M = map(int, input().split())

H_kakudo = H / 12.0 * 360.0
M_kakudo = M / 60.0 * 360.0

print(H_kakudo)
print(M_kakudo)

kakudo = abs(M_kakudo - H_kakudo)

if kakudo > 180.0:
    kakudo = 360.0 - kakudo

print(kakudo)

ans = math.sqrt(A*A + B*B - 2 * A * B * math.cos(math.radians(kakudo)))

print(ans)
