import sys
def II(): return int(sys.stdin.readline().rstrip())
def LI(): return list(map(int,sys.stdin.readline().rstrip().split()))
def MI(): return map(int,sys.stdin.readline().rstrip().split())
def SI(): return sys.stdin.readline().rstrip()
def LS(): return list(sys.stdin.readline().rstrip().split())

from collections import deque

N = II()


kukan = [0] * (2 * 10 ** 5 + 1)
ans = []

for _ in range(N):
    L, R = MI()
    kukan[L] += 1
    kukan[R] -= 1

l = 0
r = 2 * 10 ** 5 + 1
ind_l = 0
ind_r = 0
ans = []
for i in range(len(kukan) - 1):
    kukan[i + 1] += kukan[i]
    if kukan[i] == 0 and kukan[i + 1] > 0:
        l = kukan[i + 1]
        ind_l = i + 1
    elif kukan[i] != 0 and kukan[i + 1] == 0:
        r = kukan[i + 1]
        ind_r = i + 1
        ans.append([ind_l, ind_r])
for s in ans:
    print(*s)    