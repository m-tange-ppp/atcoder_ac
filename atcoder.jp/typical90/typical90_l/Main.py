import sys
from collections import deque

input = sys.stdin.readline

class UnionFind:
    def __init__(self, N):
        self.par = [-1] * N
        self.siz = [1] * N

    def root(self, x):
        if self.par[x] == -1:
            return x
        else:
            self.par[x] = self.root(self.par[x])
            return self.par[x]

    def issame(self, x, y):
        return self.root(x) == self.root(y)

    def unite(self, x, y):
        rx = self.root(x)
        ry = self.root(y)
        if rx == ry:
            return False
        else:
            if self.siz[rx] < self.siz[ry]:
                rx, ry = ry, rx
            self.par[ry] = rx
            self.siz[rx] += self.siz[ry]
            return True

    def get_size(self, x):
        return self.siz[self.root(x)]

H, W = map(int, input().split())
N = int(input())
uf = UnionFind(H * W)
dir = [W, -W, 1, -1]
wall = [0] * (H * W)
ans = []

for _ in range(N):
    q = list(map(int, input().split()))
    if q[0] == 1:
        point = (q[1] - 1) * W + (q[2] - 1)
        wall[point] = 1
        for d in dir:
            point2 = point + d
            if not (0 <= point2 <= H * W - 1):
                continue
            if (d == 1 and (point + 1) % W == 0) or(d == -1 and point % W == 0):
                continue
            if wall[point2] == 1:
                uf.unite(point, point2)
    else:
        start = (q[1] - 1) * W + (q[2] - 1)
        end = (q[3] - 1) * W + (q[4] - 1)
        ans.append("Yes" if wall[start] == 1 and wall[end] == 1 and uf.issame(start, end) else "No")

for a in ans:
    print(a)