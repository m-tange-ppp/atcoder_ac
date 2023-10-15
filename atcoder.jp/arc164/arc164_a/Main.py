import sys
def I(): return int(sys.stdin.readline().rstrip())
def LI(): return list(map(int,sys.stdin.readline().rstrip().split()))
def MI(): return map(int,sys.stdin.readline().rstrip().split())
def S(): return sys.stdin.readline().rstrip()
def LS(): return list(sys.stdin.readline().rstrip().split())
def input(): return sys.stdin.readline().rstrip()

T = I()

def dec_to_ter(N):
    shou = N
    keta = []
    while shou > 0:
        keta.append(shou % 3)
        shou //= 3
    keta.reverse()
    return keta

for _ in range(T):
    N, K = MI()
    t = dec_to_ter(N)
    L = sum(t)
    print("Yes" if K % 2 == L % 2 and L <= K <= N else "No")