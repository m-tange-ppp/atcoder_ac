from platform import mac_ver
import sys
def II(): return int(sys.stdin.readline().rstrip())
def LI(): return list(map(int,sys.stdin.readline().rstrip().split()))
def MI(): return map(int,sys.stdin.readline().rstrip().split())
def SI(): return sys.stdin.readline().rstrip()
def LS(): return list(sys.stdin.readline().rstrip().split())

from collections import deque
N = II()
A = [0] + LI()
P = [0, 0] + LI()
G = [[] for _ in range(N + 1)]
for i in range(2, N + 1):
    G[P[i]].append(i)

ind = []
deep = [0] * (N + 1)
Q = deque()
Q.append(1)
deep[1] = 0
ind.append((0, 1))
while Q:
    now = Q.pop()
    for next in G[now]:
        deep[next] = deep[now] + 1
        Q.append(next)
        ind.append((deep[next], next))
ind.sort(reverse=True, key=lambda x:x[0])
#print(ind)
max_deep = ind[0][0]
adds = 0
for i in range(len(ind)):
    if ind[i][0] != max_deep:
        if adds > 0:
            print("+")
            sys.exit()
        elif adds < 0:
            print("-")
            sys.exit()
        else:
            max_deep = ind[i][0]
    adds += A[ind[i][1]]
if A[1] > 0:
    print("+")
elif A[1] < 0:
    print("-")
else:
    print(0)