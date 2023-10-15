import sys
def I(): return int(sys.stdin.readline().rstrip())
def LI(): return list(map(int,sys.stdin.readline().rstrip().split()))
def MI(): return map(int,sys.stdin.readline().rstrip().split())
def S(): return sys.stdin.readline().rstrip()
def LS(): return list(sys.stdin.readline().rstrip().split())
def input(): return sys.stdin.readline().rstrip()

n = I()
s = S()

abc = set()
for i in range(n):
    abc.add(s[i])
    if len(abc) == 3:
        print(i+1)
        break