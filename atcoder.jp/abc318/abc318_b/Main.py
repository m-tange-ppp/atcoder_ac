import sys
def i(): return int(sys.stdin.readline().rstrip())
def li(): return list(map(int,sys.stdin.readline().rstrip().split()))
def mi(): return map(int,sys.stdin.readline().rstrip().split())
def s(): return sys.stdin.readline().rstrip()
def ls(): return list(sys.stdin.readline().rstrip().split())
def input(): return sys.stdin.readline().rstrip()

N = i()
grid = [[0] * 102 for _ in range(102)]

for _ in range(N):
    A, B, C, D = mi()
    grid[A][C] += 1
    grid[B][D] += 1
    grid[A][D] -= 1
    grid[B][C] -= 1

for k in range(101):
    for j in range(100):
        grid[k][j + 1] += grid[k][j]

for k in range(101):
    for j in range(100):
        grid[k + 1][j] += grid[k][j]

ans = 0
for k in range(101):
    for j in range(101):
        if grid[k][j] != 0:
            ans += 1

print(ans)