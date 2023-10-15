import sys
def II(): return int(sys.stdin.readline().rstrip())
def LI(): return list(map(int,sys.stdin.readline().rstrip().split()))
def MI(): return map(int,sys.stdin.readline().rstrip().split())
def SI(): return sys.stdin.readline().rstrip()
def LS(): return list(sys.stdin.readline().rstrip().split())

H, W = MI()
if H == 1:
    print(W)
elif W == 1:
    print(H)
else:
    print(-(-H // 2 ) * -(-W // 2 ))