import sys
def II(): return int(sys.stdin.readline().rstrip())
def LI(): return list(map(int,sys.stdin.readline().rstrip().split()))
def MI(): return map(int,sys.stdin.readline().rstrip().split())
def SI(): return sys.stdin.readline().rstrip()
def LS(): return list(sys.stdin.readline().rstrip().split())

from collections import defaultdict

N, K = MI()
A = LI()

ans = 0
l = 0
r = 0
count = defaultdict(int)
while r < N:
    count[A[r]] += 1
    r += 1
    ans += 1
    if len(count) > K:
        count[A[l]] -= 1
        if count[A[l]] == 0:
            count.pop(A[l])
        l += 1
        ans -= 1

print(ans)