import sys
def i(): return int(sys.stdin.readline().rstrip())
def li(): return list(map(int,sys.stdin.readline().rstrip().split()))
def mi(): return map(int,sys.stdin.readline().rstrip().split())
def s(): return sys.stdin.readline().rstrip()
def ls(): return list(sys.stdin.readline().rstrip().split())
def input(): return sys.stdin.readline().rstrip()

N, A, B = mi()
tiles = [["."]*(B * N) for _ in range(A * N)]
vflag = 0
hflag = 0
for i in range(A * N):
    if i % A == 0:
        vflag += 1
    for j in range(B * N):
        if j % B == 0:
            hflag += 1
        if (vflag + hflag) % 2 == 1:
            tiles[i][j] = "#"
    hflag = 0
    print("".join(tiles[i]))