import sys
def II(): return int(sys.stdin.readline().rstrip())
def LI(): return list(map(int,sys.stdin.readline().rstrip().split()))
def MI(): return map(int,sys.stdin.readline().rstrip().split())
def SI(): return sys.stdin.readline().rstrip()
def LS(): return list(sys.stdin.readline().rstrip().split())

sys.setrecursionlimit(10**7) 

H, W = MI()
masu = [SI() for _ in range(H)]
target = [[1] * W for _ in range(H)]
vec = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]

def search(i, j):
    for v in vec:
        h, w = v[0], v[1]
        if 0 <= h + i < H and 0 <= w + j < W:
            if target[h + i][w + j] == 1 and masu[h + i][w + j] == "#":
                target[h + i][w + j] = 0
                search(h + i, w + j)
    return

ans = 0

for i in range(H):
    for j in range(W):
        if target[i][j] == 1:
            target[i][j] = 0
            if masu[i][j] == "#":
                ans += 1
                search(i, j)

print(ans)