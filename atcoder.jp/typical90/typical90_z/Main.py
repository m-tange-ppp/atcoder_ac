import sys
def i(): return int(sys.stdin.readline().rstrip())
def li(): return list(map(int,sys.stdin.readline().rstrip().split()))
def mi(): return map(int,sys.stdin.readline().rstrip().split())
def s(): return sys.stdin.readline().rstrip()
def ls(): return list(sys.stdin.readline().rstrip().split())
def input(): return sys.stdin.readline().rstrip()

from collections import deque
N = i()
edges = [[] for _ in range(N)]
for _ in range(N - 1):
    A, B = mi()
    A, B = A - 1, B - 1
    edges[A].append(B)
    edges[B].append(A)

visited = [-1] * N
Q = deque()
Q.append(0)
visited[0] = 0
while Q:
    n = Q.popleft()
    for next in edges[n]:
        if visited[next] == -1:
            visited[next] = abs(visited[n] - 1)
            Q.append(next)

if sum(visited) >= N / 2:
    ans = [i + 1 for i, v in enumerate(visited) if v == 1]
else:
    ans = [i + 1 for i, v in enumerate(visited) if v == 0]
print(*ans[:int(N / 2)])