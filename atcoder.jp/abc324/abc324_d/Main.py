import sys
def II(): return int(sys.stdin.readline().rstrip())
def LI(): return list(map(int,sys.stdin.readline().rstrip().split()))
def MI(): return map(int,sys.stdin.readline().rstrip().split())
def SI(): return sys.stdin.readline().rstrip()
def LS(): return list(sys.stdin.readline().rstrip().split())

from collections import defaultdict
N = II()
S = SI()
sd = defaultdict(int)
for s in S:
    sd[s] += 1
sq_list = []
i = 10 ** ((N - sd["0"] - 1) // 2)
ans = 0
if S == "0":
    ans = 1
else:
    while i ** 2 < 10 ** N:
        d = defaultdict(int)
        n = str(i ** 2)
        for c in n:
            d[c] += 1
        d["0"] += (len(S) - len(n))
        if sd == d:
            ans += 1
        i += 1
print(ans)