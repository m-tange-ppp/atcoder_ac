import sys
def II(): return int(sys.stdin.readline().rstrip())
def LI(): return list(map(int,sys.stdin.readline().rstrip().split()))
def MI(): return map(int,sys.stdin.readline().rstrip().split())
def SI(): return sys.stdin.readline().rstrip()
def LS(): return list(sys.stdin.readline().rstrip().split())

import sys
sys.setrecursionlimit(10**7) 

N, M = MI()
edges = [[] for _ in range(N)]
people = [[0, 0] for _ in range(N)]
visited = [-1] * N

for _ in range(M):
    A, B, X, Y = MI()
    edges[A - 1].append([B - 1, X, Y])
    edges[B - 1].append([A - 1, -X, -Y])

def dfs(a):
    for e in edges[a]:
        next, x, y = e[0], e[1], e[2]
        if visited[next] == -1:
            people[next][0] = people[a][0] + x
            people[next][1] = people[a][1] + y
            visited[next] = 0
            dfs(next)
    return

visited[0] = 0
dfs(0)

for i in range(N):
    if visited[i] == -1:
        print("undecidable")
    else:
        print(*people[i])