import sys
def i(): return int(sys.stdin.readline().rstrip())
def li(): return list(map(int,sys.stdin.readline().rstrip().split()))
def mi(): return map(int,sys.stdin.readline().rstrip().split())
def s(): return sys.stdin.readline().rstrip()
def ls(): return list(sys.stdin.readline().rstrip().split())
def input(): return sys.stdin.readline().rstrip()

S = s()
l = len(S)
ans = set()
f_big = False
f_small = False

for i in range(l):
    ans.add(S[i])
    if S[i].isupper():
        f_big = True
    if S[i].islower():
        f_small = True

if len(ans) == l and f_small and f_big:
    print("Yes")
else:
    print("No")