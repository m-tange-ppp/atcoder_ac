import sys
def II(): return int(sys.stdin.readline().rstrip())
def LI(): return list(map(int,sys.stdin.readline().rstrip().split()))
def MI(): return map(int,sys.stdin.readline().rstrip().split())
def SI(): return sys.stdin.readline().rstrip()
def LS(): return list(sys.stdin.readline().rstrip().split())

from collections import deque

N, M = MI()
E = [[] for _ in range(N + 1)]
for _ in range(M):
    a, b = MI()
    E[a].append(b)
    E[b].append(a)

Q = deque()
Q.append(1)
visited = [10 ** 6] * (N + 1)
visited[1] = 0
while Q:
    now = Q.popleft()
    for n in E[now]:
        if visited[n] > visited[now] + 1:
            visited[n] = visited[now] + 1
            Q.append(n)
for i in range(1, N + 1):
    if visited[i] == 10 ** 6:
        visited[i] = -1
    print(visited[i])