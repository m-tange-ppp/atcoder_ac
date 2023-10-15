import sys
def I(): return int(sys.stdin.readline().rstrip())
def LI(): return list(map(int,sys.stdin.readline().rstrip().split()))
def MI(): return map(int,sys.stdin.readline().rstrip().split())
def S(): return sys.stdin.readline().rstrip()
def LS(): return list(sys.stdin.readline().rstrip().split())
def input(): return sys.stdin.readline().rstrip()

from collections import deque
N, M = MI()
par_list = LI()
kakei = [[] for _ in range(N)]
for i in range(len(par_list)):
    p = par_list[i] - 1
    kakei[p].append(i + 1)

count = [-1]*N

for _ in range(M):
    x, y = MI()
    x -= 1
    count[x] = max(y, count[x])

stack = deque([(0, -1)])
ans = 0

while stack:
    node, d = stack.popleft()
    d = max(d, count[node])
    if d >= 0:
        ans += 1
    d -= 1
    for c in kakei[node]:
        stack.append([c, d])

print(ans)