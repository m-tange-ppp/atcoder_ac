import sys
def II(): return int(sys.stdin.readline().rstrip())
def LI(): return list(map(int,sys.stdin.readline().rstrip().split()))
def MI(): return map(int,sys.stdin.readline().rstrip().split())
def SI(): return sys.stdin.readline().rstrip()
def LS(): return list(sys.stdin.readline().rstrip().split())

S = SI()
l = len(S)
bubun = []
for i in range(l):
    for j in range(i, l):
        bubun.append(S[i:j + 1])
ans = 0
for b in bubun:
    if b == b[::-1] and len(b) > ans:
        ans = len(b)
print(ans)