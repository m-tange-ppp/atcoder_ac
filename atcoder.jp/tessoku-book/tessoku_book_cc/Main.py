import sys
def II(): return int(sys.stdin.readline().rstrip())
def LI(): return list(map(int,sys.stdin.readline().rstrip().split()))
def MI(): return map(int,sys.stdin.readline().rstrip().split())
def SI(): return sys.stdin.readline().rstrip()
def LS(): return list(sys.stdin.readline().rstrip().split())

N = SI()
keta = len(N) - 1
c = keta
ans = 0
while c >= 0:
    if N[keta - c] == "1":
        ans += 2 ** c
    c -= 1
print(ans)