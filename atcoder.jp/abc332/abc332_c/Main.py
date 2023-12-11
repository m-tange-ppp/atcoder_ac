import sys
def II(): return int(sys.stdin.readline().rstrip())
def LI(): return list(map(int,sys.stdin.readline().rstrip().split()))
def MI(): return map(int,sys.stdin.readline().rstrip().split())
def SI(): return sys.stdin.readline().rstrip()
def LS(): return list(sys.stdin.readline().rstrip().split())

N, M = MI()
S = SI()
muji = M
rogo = 0
R = 0
for i in range(N):
    if S[i] == "0":
        muji = M
        rogo = R
    elif S[i] == "1":
        if muji > 0:
            muji -= 1
        elif rogo > 0:
            rogo -= 1
        else:
            R += 1
    else:
        if rogo > 0:
            rogo -= 1
        else:
            R += 1
print(R)