import sys
def II(): return int(sys.stdin.readline().rstrip())
def LI(): return list(map(int,sys.stdin.readline().rstrip().split()))
def MI(): return map(int,sys.stdin.readline().rstrip().split())
def SI(): return sys.stdin.readline().rstrip()
def LS(): return list(sys.stdin.readline().rstrip().split())

N,M,L = MI()
A = LI()
B = LI()
NG = set()
for _ in range(L):
    c,d = MI()
    NG.add((c-1,d-1))
A_ind = [[i,a] for i,a in enumerate(A)]
B_ind = [[i,a] for i,a in enumerate(B)]
A_ind.sort(key=lambda x:x[1], reverse=True)
B_ind.sort(key=lambda x:x[1], reverse=True)
ans = 0
for a in A_ind:
    for b in B_ind:
        if not (a[0],b[0]) in NG:
            ans = max(ans, a[1] + b[1])
            break
print(ans)