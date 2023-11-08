import sys
def II(): return int(sys.stdin.readline().rstrip())
def LI(): return list(map(int,sys.stdin.readline().rstrip().split()))
def MI(): return map(int,sys.stdin.readline().rstrip().split())
def SI(): return sys.stdin.readline().rstrip()
def LS(): return list(sys.stdin.readline().rstrip().split())

sys.setrecursionlimit(10**7)
N, M = MI()
A = LI()
B = LI()
G = [[] for _ in range(N)]
for i in range(M):
    a, b = A[i] - 1, B[i] - 1
    G[a].append(b)
    G[b].append(a)

color = [0] * N

def dfs(v, c):
    color[v] = c
    for i in range(len(G[v])):
        if color[G[v][i]] == c:
            return False
        if color[G[v][i]] == 0 and not dfs(G[v][i], -c):
            return False
    return True

for i in range(N):
    if color[i] == 0:
        if not dfs(i, 1):
            print("No")
            sys.exit()
print("Yes")