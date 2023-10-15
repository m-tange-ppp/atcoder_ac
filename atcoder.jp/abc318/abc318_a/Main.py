import sys
def i(): return int(sys.stdin.readline().rstrip())
def li(): return list(map(int,sys.stdin.readline().rstrip().split()))
def mi(): return map(int,sys.stdin.readline().rstrip().split())
def s(): return sys.stdin.readline().rstrip()
def ls(): return list(sys.stdin.readline().rstrip().split())
def input(): return sys.stdin.readline().rstrip()

N, M, P = mi()
nokori = N - M
ans = 0
if nokori >= 0:
    ans += 1
while nokori >= 0:
    nokori -= P
    if nokori >= 0:
        ans += 1
print(ans)