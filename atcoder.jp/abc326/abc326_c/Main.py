import sys
def II(): return int(sys.stdin.readline().rstrip())
def LI(): return list(map(int,sys.stdin.readline().rstrip().split()))
def MI(): return map(int,sys.stdin.readline().rstrip().split())
def SI(): return sys.stdin.readline().rstrip()
def LS(): return list(sys.stdin.readline().rstrip().split())

import bisect
N, M = MI()
A = LI()
A.sort()
nums = list(set(A))
ans = 0
for n in nums:
    l = bisect.bisect_left(A, n)
    r = bisect.bisect_right(A, n + M - 1)
    if r - l > ans:
        ans = r - l
print(ans)