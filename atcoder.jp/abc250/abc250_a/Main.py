import sys
def i(): return int(sys.stdin.readline().rstrip())
def li(): return list(map(int,sys.stdin.readline().rstrip().split()))
def mi(): return map(int,sys.stdin.readline().rstrip().split())
def s(): return sys.stdin.readline().rstrip()
def ls(): return list(sys.stdin.readline().rstrip().split())
def input(): return sys.stdin.readline().rstrip()

H, W = mi()
R, C = mi()
R, C = R - 1, C - 1
ans = 0
for i in range(H):
    for j in range(W):
        if abs(R - i) + abs(C - j) == 1:
            ans += 1
print(ans)