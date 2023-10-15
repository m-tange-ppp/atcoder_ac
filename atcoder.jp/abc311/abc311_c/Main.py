import sys
def I(): return int(sys.stdin.readline().rstrip())
def LI(): return list(map(int,sys.stdin.readline().rstrip().split()))
def MI(): return map(int,sys.stdin.readline().rstrip().split())
def S(): return sys.stdin.readline().rstrip()
def LS(): return list(sys.stdin.readline().rstrip().split())
def input(): return sys.stdin.readline().rstrip()

n = I()
ends = [x - 1 for x in LI()]

visited = []
vis_set = set()
visited.append(0)
vis_set.add(0)

for _ in range(n):
    st = ends[visited[len(visited) - 1]]
    if st in vis_set:
        break
    visited.append(st)
    vis_set.add(st)

ind = visited.index(st)
loop = [x + 1 for x in visited[ind:]]
print(len(loop))
print(*loop)