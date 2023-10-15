import sys
def I(): return int(sys.stdin.readline().rstrip())
def LI(): return list(map(int,sys.stdin.readline().rstrip().split()))
def MI(): return map(int,sys.stdin.readline().rstrip().split())
def S(): return sys.stdin.readline().rstrip()
def LS(): return list(sys.stdin.readline().rstrip().split())
def input(): return sys.stdin.readline().rstrip()

N = I()
Ss = set()
for _ in range(N):
    s1 = S()
    if len(s1) == 1 or s1 == s1[::-1]:
        s2 = s1 + "0"
    else:
        s2 = s1[::-1]
    Ss.add(s1)
    Ss.add(s2)

print(len(Ss) // 2)