import sys
def II(): return int(sys.stdin.readline().rstrip())
def LI(): return list(map(int,sys.stdin.readline().rstrip().split()))
def MI(): return map(int,sys.stdin.readline().rstrip().split())
def SI(): return sys.stdin.readline().rstrip()
def LS(): return list(sys.stdin.readline().rstrip().split())

from collections import deque

N, M = MI()
E = [[] for _ in range(N)]
for _ in range(M):
    a, b = MI()
    a -= 1
    b -= 1
    E[a].append(b)
    E[b].append(a)

Q = deque()
Q.append(0)
visited = [-1] * N
visited[0] = 0
while Q:
    now = Q.pop()
    for n in E[now]:
        if visited[n] == -1:
            visited[n] = 0
            Q.append(n)
print("The graph is connected." if sum(visited) == 0 else "The graph is not connected.")