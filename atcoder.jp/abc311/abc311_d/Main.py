import sys
from collections import deque
def I(): return int(sys.stdin.readline().rstrip())
def LI(): return list(map(int,sys.stdin.readline().rstrip().split()))
def MI(): return map(int,sys.stdin.readline().rstrip().split())
def S(): return sys.stdin.readline().rstrip()
def LS(): return list(sys.stdin.readline().rstrip().split())
def input(): return sys.stdin.readline().rstrip()

H, W = map(int, input().split())
grids = [S() for _ in range(H)]

Q = deque()
Q.append([1, 1])

dist = [[-1]*W for _ in range(H)]
dist[1][1] = 0

dirs = [(0, 1), (0, -1), (1, 0), (-1, 0)]

stop = set() 

while Q:
    y, x = Q.popleft()
    for dy, dx in dirs:
        y2 = y + dy
        x2 = x + dx
        while grids[y2][x2] == ".":
            dist[y2][x2] = 0
            y2 = y2 + dy
            x2 = x2 + dx
        if not (y2 - dy, x2 - dx) in stop:
            Q.append((y2 - dy, x2 - dx))
            stop.add((y2 - dy, x2 - dx))

ans = 0
for h in dist:
    for w in h:
        if w == 0:
            ans += 1

print(ans)
