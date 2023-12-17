import sys
def II(): return int(sys.stdin.readline().rstrip())
def LI(): return list(map(int,sys.stdin.readline().rstrip().split()))
def MI(): return map(int,sys.stdin.readline().rstrip().split())
def SI(): return sys.stdin.readline().rstrip()
def LS(): return list(sys.stdin.readline().rstrip().split())

from collections import deque
N = II()
G = [[] for _ in range(N + 1)]
for _ in range(N - 1):
    u, v = MI()
    G[u].append(v)
    G[v].append(u)
Q = deque()
visited = [-1] * (N + 1)
spe = set()
Q.append(1)
visited[1] = 0
kouho = []
count = 0
if len(G[1]) == 1:
    print(1)
    sys.exit()
while Q:
    now = Q.pop()
    if now in spe:
        kouho.append(count)
        count = 0
    if now != 1:
        count += 1
    for next in G[now]:
        if now == 1:
            spe.add(next)
        if visited[next] == -1:
            Q.append(next)
            visited[next] = 0
kouho.append(count)
kouho.sort()
ans = sum(kouho[:-1]) + 1
print(ans)