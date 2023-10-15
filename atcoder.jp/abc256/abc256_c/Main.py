import sys
def II(): return int(sys.stdin.readline().rstrip())
def LI(): return list(map(int,sys.stdin.readline().rstrip().split()))
def MI(): return map(int,sys.stdin.readline().rstrip().split())
def SI(): return sys.stdin.readline().rstrip()
def LS(): return list(sys.stdin.readline().rstrip().split())

h1, h2, h3, w1, w2, w3 = MI()
grid = [[] for _ in range(3)]

for i in range(1, h1 - 1):
    for j in range(1, h1 - i):
        grid[0].append([i, j, h1 - i - j])
for i in range(1, h2 - 1):
    for j in range(1, h2 - i):
        grid[1].append([i, j, h2 - i - j])
for i in range(1, h3 - 1):
    for j in range(1, h3 - i):
        grid[2].append([i, j, h3 - i - j])

ans = 0
for a in grid[0]:
    for b in grid[1]:
        for c in grid[2]:
            if a[0] + b[0] + c[0] == w1 and a[1] + b[1] + c[1] == w2 and a[2] + b[2] + c[2] == w3:
                ans += 1

print(ans)
