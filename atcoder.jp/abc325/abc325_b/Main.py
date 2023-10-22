import sys
def II(): return int(sys.stdin.readline().rstrip())
def LI(): return list(map(int,sys.stdin.readline().rstrip().split()))
def MI(): return map(int,sys.stdin.readline().rstrip().split())
def SI(): return sys.stdin.readline().rstrip()
def LS(): return list(sys.stdin.readline().rstrip().split())

N = II()
kyoten = []
for _ in range(N):
    W, X = MI()
    kyoten.append([W, (X + 9) % 24])
ans = 0
for i in range(24):
    sum_w = 0
    for k in kyoten:
        w, x = k[0], k[1]
        if x <= 15 and x <= i <= x + 8:
            sum_w += w
        elif x >= 16 and (x <= i or 0 <= i <= (x + 8) % 24):
            sum_w += w
    if ans < sum_w:
        ans = sum_w
print(ans)