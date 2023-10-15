import sys
def I(): return int(sys.stdin.readline().rstrip())
def LI(): return list(map(int,sys.stdin.readline().rstrip().split()))
def MI(): return map(int,sys.stdin.readline().rstrip().split())
def S(): return sys.stdin.readline().rstrip()
def LS(): return list(sys.stdin.readline().rstrip().split())
def input(): return sys.stdin.readline().rstrip()

n, d = MI()
sches = []
for _ in range(n):
    sches.append(S())

hima = []
for i in range(d):
    f = True
    for s in sches:
        if s[i] != "o":
            f = False
            break
    if f:
        if i != 0 and hima[i - 1] != 0 :
            hima.append(hima[i - 1] + 1)
        else:
            hima.append(1)
    else:
        hima.append(0)

print(max(hima))