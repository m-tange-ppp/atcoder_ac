import sys
def II(): return int(sys.stdin.readline().rstrip())
def LI(): return list(map(int,sys.stdin.readline().rstrip().split()))
def MI(): return map(int,sys.stdin.readline().rstrip().split())
def SI(): return sys.stdin.readline().rstrip()
def LS(): return list(sys.stdin.readline().rstrip().split())

N = II()
S = SI()
f = False
for i in range(N - 1):
    if S[i] == "a" and S[i + 1] == "b":
        f = True
        break
    elif S[i] == "b" and S[i + 1] == "a":
        f = True
        break
print("Yes" if f else "No")
