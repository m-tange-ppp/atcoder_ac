import sys
def i(): return int(sys.stdin.readline().rstrip())
def li(): return list(map(int,sys.stdin.readline().rstrip().split()))
def mi(): return map(int,sys.stdin.readline().rstrip().split())
def s(): return sys.stdin.readline().rstrip()
def ls(): return list(sys.stdin.readline().rstrip().split())
def input(): return sys.stdin.readline().rstrip()

N = i()
grid = [[0] * 1001 for _ in range(1001)]
minlx = 1001
minly = 1001
maxrx = 0
maxry = 0
ans = [0] * (N + 1)

for _ in range(N):
    lx, ly, rx, ry = mi()
    grid[lx][ly] += 1
    grid[rx][ry] += 1
    grid[lx][ry] -= 1
    grid[rx][ly] -= 1

for i in range(1001):
    for j in range(1000):
        grid[i][j + 1] += grid[i][j]

for i in range(1000):
    for j in range(1001):
        grid[i + 1][j] += grid[i][j]
        ans[grid[i][j]] += 1

for a in ans[1:]:
    print(a)