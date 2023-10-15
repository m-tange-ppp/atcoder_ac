import sys
def I(): return int(sys.stdin.readline().rstrip())
def LI(): return list(map(int,sys.stdin.readline().rstrip().split()))
def MI(): return map(int,sys.stdin.readline().rstrip().split())
def S(): return sys.stdin.readline().rstrip()
def LS(): return list(sys.stdin.readline().rstrip().split())

N = I()
S_set = set()
max_T = 0
ans = 0

for i in range(N):
    s, t = sys.stdin.readline().rstrip().split()
    T = int(t)
    if not s in S_set:
        S_set.add(s)
        if T > max_T:
            max_T = T
            ans = i + 1

print(ans)
