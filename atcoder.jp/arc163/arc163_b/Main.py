import sys

input = sys.stdin.readline

N, M = map(int, input().split())
A = list(map(int, input().split()))
x, y, *z = A

z.sort()

ans = 10 ** 18
for i in range(N-2-M+1):
    zx = z[i]
    zy = z[i+M-1]
    v = max(x - zx, 0) + max(zy - y, 0)
    ans = min(ans, v)
print(ans)