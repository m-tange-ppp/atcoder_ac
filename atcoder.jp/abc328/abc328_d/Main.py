import sys
def II(): return int(sys.stdin.readline().rstrip())
def LI(): return list(map(int,sys.stdin.readline().rstrip().split()))
def MI(): return map(int,sys.stdin.readline().rstrip().split())
def SI(): return sys.stdin.readline().rstrip()
def LS(): return list(sys.stdin.readline().rstrip().split())

S = SI()
L = len(S)
l = 0
r = 2
while r < len(S):
    if r - l == 2 and S[l] == "A" and S[l + 1] == "B" and S[r] == "C":
        S = S[:l] + S[r + 1:]
        l = max(0, l - 2)
        r = l + 2
    else:
        l += 1
        r += 1
print(S)
    