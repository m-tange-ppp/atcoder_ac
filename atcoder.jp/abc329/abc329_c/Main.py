import sys
def II(): return int(sys.stdin.readline().rstrip())
def LI(): return list(map(int,sys.stdin.readline().rstrip().split()))
def MI(): return map(int,sys.stdin.readline().rstrip().split())
def SI(): return sys.stdin.readline().rstrip()
def LS(): return list(sys.stdin.readline().rstrip().split())

from collections import defaultdict
N = II()
S = SI()
l = 0
r = 0
dic = defaultdict(int)
while r < N:
    if r < N - 1 and S[r] == S[r + 1]:
        r += 1
    elif r == N - 1:
        dic[S[l]] = max(r - l + 1, dic[S[l]])
        r += 1
    else:
        dic[S[l]] = max(r - l + 1, dic[S[l]])
        r += 1
        l = r
ans = 0
for a in dic.values():
    ans += a
print(ans)