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
    A, B, C = MI()
    G[A].append([B, C])
    G[B].append([A, C])
Q = deque()
dist = [10 ** 10] * (N + 1)
Q.append([1, 0])
dist[1] = 0
while Q:
    now = Q.popleft()
    for next in G[now[0]]:
        if dist[now[0]] + next[1] < dist[next[0]]:
            dist[next[0]] = dist[now[0]] + next[1]
            Q.append(next)
for i in range(1, N + 1):
    if dist[i] == 10 ** 10:
        print(-1)
    else:
        print(dist[i])