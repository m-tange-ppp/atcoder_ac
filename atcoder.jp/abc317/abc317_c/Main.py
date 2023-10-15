import sys
def i(): return int(sys.stdin.readline().rstrip())
def li(): return list(map(int,sys.stdin.readline().rstrip().split()))
def mi(): return map(int,sys.stdin.readline().rstrip().split())
def s(): return sys.stdin.readline().rstrip()
def ls(): return list(sys.stdin.readline().rstrip().split())
def input(): return sys.stdin.readline().rstrip()

from collections import deque

N, M = mi()
E = [[0] * N for _ in range(N)]
for _ in range(M):
    A, B, C = mi()
    E[A - 1][B - 1] = C
    E[B - 1][A - 1] = C

ans = 0
used = [False] * N

def dfs(v, s):
    global ans
    used[v] = True
    if s > ans: ans = s
    for i in range(N):
        if not used[i] and E[v][i]:
            dfs(i, s + E[v][i])
    used[v] = False #Falseに戻して他の経路で使えるように

for i in range(N):
    dfs(i, 0)
print(ans)