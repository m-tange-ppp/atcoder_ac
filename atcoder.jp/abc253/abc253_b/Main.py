import sys
def II(): return int(sys.stdin.readline().rstrip())
def LI(): return list(map(int,sys.stdin.readline().rstrip().split()))
def MI(): return map(int,sys.stdin.readline().rstrip().split())
def SI(): return sys.stdin.readline().rstrip()
def LS(): return list(sys.stdin.readline().rstrip().split())

H, W = MI()
S = [SI() for _ in range(H)]
koma = []
for i in range(H):
    for j in range(W):
        if S[i][j] == "o":
            koma.append((i, j))
print(abs(koma[0][0] - koma[1][0]) + abs(koma[0][1] - koma[1][1]))