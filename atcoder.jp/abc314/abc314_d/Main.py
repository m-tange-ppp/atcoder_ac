import sys
def I(): return int(sys.stdin.readline().rstrip())
def LI(): return list(map(int,sys.stdin.readline().rstrip().split()))
def MI(): return map(int,sys.stdin.readline().rstrip().split())
def S(): return sys.stdin.readline().rstrip()
def LS(): return list(sys.stdin.readline().rstrip().split())
def input(): return sys.stdin.readline().rstrip()

n = I()
s = list(input())
q = I()
reqlist = []
count = 0
for _ in range(q):
    i = LS()
    t = int(i[0])
    x = int(i[1])
    c = i[2]
    reqlist.append((t, x, c, count))
    count += 1

last_non_one_index = 10**9 + 1
for req in reqlist:
    if req[0] != 1:
        last_non_one_index = req[3]

for req in reqlist:
    t = req[0]
    x = req[1]
    c = req[2]
    count = req[3]
    if count == last_non_one_index:
        if t == 2:
            s = [ch.lower() for ch in s]
        else :
            s = [ch.upper() for ch in s]
    else:
        if t == 1:
            s[x - 1] = c
print("".join(s))