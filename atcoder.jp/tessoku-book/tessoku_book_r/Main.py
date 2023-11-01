import sys
def II(): return int(sys.stdin.readline().rstrip())
def LI(): return list(map(int,sys.stdin.readline().rstrip().split()))
def MI(): return map(int,sys.stdin.readline().rstrip().split())
def SI(): return sys.stdin.readline().rstrip()
def LS(): return list(sys.stdin.readline().rstrip().split())

N, S = MI()
A = LI()
A.sort()
sums = set()
sums.add(0)
i = 0
while i < N:
    for s in list(sums):
        sums.add( s + A[i])
    i += 1
print("Yes" if S in sums else "No")