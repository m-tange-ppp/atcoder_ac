import sys
def II(): return int(sys.stdin.readline().rstrip())
def LI(): return list(map(int,sys.stdin.readline().rstrip().split()))
def MI(): return map(int,sys.stdin.readline().rstrip().split())
def SI(): return sys.stdin.readline().rstrip()
def LS(): return list(sys.stdin.readline().rstrip().split())

from collections import deque
N, M = MI()
G = [[] for _ in range(N + 1)]
for _ in range(M):
    A, B = MI()
    G[A].append(B)
ans = []
for i in range(1, N + 1):
    visited = [0] * (N + 1)
    Q = deque()
    Q.append(i)
    visited[i] = 1
    while Q:
        now = Q.pop()
        for next in G[now]:
            if visited[next] == 0:
                visited[next] = 1
                Q.append(next)
    if sum(visited) == N:
        ans.append(i)
if len(ans) == 1:
    print(ans[0])
else:
    print(-1)