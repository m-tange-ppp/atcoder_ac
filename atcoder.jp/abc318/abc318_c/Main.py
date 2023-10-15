import sys
def i(): return int(sys.stdin.readline().rstrip())
def li(): return list(map(int,sys.stdin.readline().rstrip().split()))
def mi(): return map(int,sys.stdin.readline().rstrip().split())
def s(): return sys.stdin.readline().rstrip()
def ls(): return list(sys.stdin.readline().rstrip().split())
def input(): return sys.stdin.readline().rstrip()

N, D, P = mi()
F = li()

F.sort(reverse=True)
flag = True
ans = sum(F)

for j in range(0, N, D):
    days = sum(F[j:j + D])
    if days > P:
        ans -= days - P
    else:
        break

print(ans)
    