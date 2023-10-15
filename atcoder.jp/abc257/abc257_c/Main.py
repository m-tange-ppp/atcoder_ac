import sys
def II(): return int(sys.stdin.readline().rstrip())
def LI(): return list(map(int,sys.stdin.readline().rstrip().split()))
def MI(): return map(int,sys.stdin.readline().rstrip().split())
def SI(): return sys.stdin.readline().rstrip()
def LS(): return list(sys.stdin.readline().rstrip().split())

import bisect
N = II()
S = SI()
W = LI()

children = []
adult = []
for i in range(N):
    if S[i] == "0":
        children.append(W[i])
    else:
        adult.append(W[i])
children.sort()
adult.sort()
W.append(0)
W.append(max(W) + 1)


ans = 0
len_a = len(adult)
for w in W:
    c = bisect.bisect_left(children, w)
    a = bisect.bisect_left(adult, w)
    if ans < c + len_a - a:
        ans = c + len_a - a

print(ans)