import sys
def II(): return int(sys.stdin.readline().rstrip())
def LI(): return list(map(int,sys.stdin.readline().rstrip().split()))
def MI(): return map(int,sys.stdin.readline().rstrip().split())
def SI(): return sys.stdin.readline().rstrip()
def LS(): return list(sys.stdin.readline().rstrip().split())

N, M = MI()
S = SI()
T = SI()

def settou():
    if S == T[:N]:
        return True
    return False

def setsubi():
    if S == T[M - N:]:
        return True
    return False

ans = 0
if settou() and setsubi():
    ans = 0
elif settou() and not setsubi():
    ans = 1
elif not settou() and setsubi():
    ans = 2
else:
    ans = 3

print(ans)