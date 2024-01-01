import sys
def II(): return int(sys.stdin.readline().rstrip())
def LI(): return list(map(int,sys.stdin.readline().rstrip().split()))
def MI(): return map(int,sys.stdin.readline().rstrip().split())
def SI(): return sys.stdin.readline().rstrip()
def LS(): return list(sys.stdin.readline().rstrip().split())

N, K = MI()
A = LI()
csum = [0] * N
csum[0] = A[0]
for i in range(1, N):
    csum[i] = csum[i - 1] + A[i]
ans = 0
if csum[0] <= K:
    ans += 1
if N > 1:
    for i in range(1, N):
        if csum[i] <= K:
            ans += 1
        for j in range(i - 1, -1, -1):
            if csum[i] - csum[j] <= K:
                ans += 1
            else:
                break
print(ans)