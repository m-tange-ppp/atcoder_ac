import sys
def II(): return int(sys.stdin.readline().rstrip())
def LI(): return list(map(int,sys.stdin.readline().rstrip().split()))
def MI(): return map(int,sys.stdin.readline().rstrip().split())
def SI(): return sys.stdin.readline().rstrip()
def LS(): return list(sys.stdin.readline().rstrip().split())

N, Q = MI()
C = LI()
set_list = [{c} for c in C]
ans = []
for _ in range(Q):
    a, b = MI()
    a, b = a - 1, b - 1
    if len(set_list[a]) >= len(set_list[b]):
        set_list[a] |= set_list[b]
        set_list[a], set_list[b] = set(), set_list[a]
    else:
        set_list[b] |= set_list[a]
        set_list[a] = set()
    ans.append(len(set_list[b]))
print(*ans, sep="\n")