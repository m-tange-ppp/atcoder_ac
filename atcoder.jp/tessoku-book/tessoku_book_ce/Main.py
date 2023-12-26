import sys
def II(): return int(sys.stdin.readline().rstrip())
def LI(): return list(map(int,sys.stdin.readline().rstrip().split()))
def MI(): return map(int,sys.stdin.readline().rstrip().split())
def SI(): return sys.stdin.readline().rstrip()
def LS(): return list(sys.stdin.readline().rstrip().split())

N = II()
A = LI()
Q = II()
csum = [A[0]]
for i in range(1, N):
    csum.append(csum[-1] + A[i])
for _ in range(Q):
    L, R = MI()
    L -= 1
    R -= 1
    num = R - L + 1
    hits = csum[R] - csum[L] + A[L]
    if hits > num - hits:
        print("win")
    elif hits < num - hits:
        print("lose")
    else:
        print("draw")