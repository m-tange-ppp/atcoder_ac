import sys
from collections import deque
def I(): return int(sys.stdin.readline().rstrip())
def LI(): return list(map(int,sys.stdin.readline().rstrip().split()))
def MI(): return map(int,sys.stdin.readline().rstrip().split())
def S(): return sys.stdin.readline().rstrip()
def LS(): return list(sys.stdin.readline().rstrip().split())
def input(): return sys.stdin.readline().rstrip()

n,m = MI()
grids = []
for _ in range(n):
    grids.append(S())

def count_pattern(grids, pattern):
    row = len(grids)
    col = len(grids[0])
    ans = []

    for r in range(row - 8):
        for c in range(col - 8):
            match = True

            for i in range(9):
                for j in range(9):
                    if pattern[i][j] != '?' and pattern[i][j] != grids[r + i][c + j]:
                        match = False
                        break

                if not match:
                    break

            if match:
                print(f"{r + 1} {c + 1}")

pattern = [
    list("###.?????"),
    list("###.?????"),
    list("###.?????"),
    list("....?????"),
    list("?????????"),
    list("?????...."),
    list("?????.###"),
    list("?????.###"),
    list("?????.###")
    ]

count_pattern(grids, pattern)