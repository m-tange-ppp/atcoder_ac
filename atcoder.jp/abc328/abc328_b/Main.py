import sys
def II(): return int(sys.stdin.readline().rstrip())
def LI(): return list(map(int,sys.stdin.readline().rstrip().split()))
def MI(): return map(int,sys.stdin.readline().rstrip().split())
def SI(): return sys.stdin.readline().rstrip()
def LS(): return list(sys.stdin.readline().rstrip().split())

N = II()
D = [0]  + LI()
ans = 0
for i in range(1, N + 1):
    s = set()
    for n in str(i):
        s.add(int(n))
    if len(s) != 1:
        continue
    c = 0
    for num in s:
        c = num
    if c <= D[i]:
        ans += 1
    if 10 * c + c <= D[i]:
        ans += 1
print(ans)