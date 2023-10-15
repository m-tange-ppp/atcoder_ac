import sys
def II(): return int(sys.stdin.readline().rstrip())
def LI(): return list(map(int,sys.stdin.readline().rstrip().split()))
def MI(): return map(int,sys.stdin.readline().rstrip().split())
def SI(): return sys.stdin.readline().rstrip()
def LS(): return list(sys.stdin.readline().rstrip().split())

N, K = MI()
ans = 0
for i in range(1, N + 1):
    min_i = min(K - i + 1, N + 1)
    for j in range(1, min_i):
        if K - i - j > 0 and K - i - j <= N:
            ans += 1
print(ans)