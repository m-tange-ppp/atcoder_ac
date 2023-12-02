import sys
def II(): return int(sys.stdin.readline().rstrip())
def LI(): return list(map(int,sys.stdin.readline().rstrip().split()))
def MI(): return map(int,sys.stdin.readline().rstrip().split())
def SI(): return sys.stdin.readline().rstrip()
def LS(): return list(sys.stdin.readline().rstrip().split())

N,K = MI()
M = [LI() for _ in range(N)]
M.sort(key=lambda x:x[0])
tairyoku = [m[0] for m in M]
ans = 0
for l in tairyoku:
    r = l+K
    taimember = []
    for m in M:
        if l <= m[0] <= r:
            taimember.append(m)
    taimember.sort(key=lambda x:x[1])
    kiryoku = [m[1] for m in taimember]
    for l in kiryoku:
        r = l+K
        member = []
        for m in taimember:
            if l <= m[1] <= r:
                member.append(m)
        if ans <= len(member):
            ans = len(member)
print(ans)