import sys
def II(): return int(sys.stdin.readline().rstrip())
def LI(): return list(map(int,sys.stdin.readline().rstrip().split()))
def MI(): return map(int,sys.stdin.readline().rstrip().split())
def SI(): return sys.stdin.readline().rstrip()
def LS(): return list(sys.stdin.readline().rstrip().split())

from itertools import combinations
N = II()
A = LI()
combs = list(combinations([i for i in range(N)], 3))
for comb in combs:
    s = 0
    for i in comb:
        s += A[i]
    if s == 1000:
        break
else:
    print("No")
    sys.exit()
print("Yes")