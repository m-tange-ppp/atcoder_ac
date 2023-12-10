import sys
def II(): return int(sys.stdin.readline().rstrip())
def LI(): return list(map(int,sys.stdin.readline().rstrip().split()))
def MI(): return map(int,sys.stdin.readline().rstrip().split())
def SI(): return sys.stdin.readline().rstrip()
def LS(): return list(sys.stdin.readline().rstrip().split())

from collections import deque
N = II()
G = [[] for _ in range(N + 1)]
for i in range(1, N + 1):
    G[i] = LI()[1:]
#print(G)
Q = deque()
Q.append(1)
ans = []
read = [0] * (N + 1)
while Q:
    now = Q.pop()
    if now < 0:
        now = -now
        if read[now] == 0:
            ans.append(now)
            read[now] = 1
    else:
        for n in G[now]:
            if read[n] == 1:
                continue
            Q.append(-n)
            Q.append(n)
print(*ans)