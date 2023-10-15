import sys
def II(): return int(sys.stdin.readline().rstrip())
def LI(): return list(map(int,sys.stdin.readline().rstrip().split()))
def MI(): return map(int,sys.stdin.readline().rstrip().split())
def SI(): return sys.stdin.readline().rstrip()
def LS(): return list(sys.stdin.readline().rstrip().split())

from collections import defaultdict

Q = II()
S = defaultdict(int)
max_x = -1
min_x = 10 ** 9 + 1
def query(q):
    num = q[0]
    global max_x
    global min_x
    if num == 1:
        x = q[1]
        S[x] += 1
        if x > max_x:
            max_x = x
        if x < min_x:
            min_x = x
    elif num == 2:
        x = q[1]
        c = q[2]
        S[x] -= min(c, S[x])
        if S[x] == 0:
            S.pop(x)
            if x == max_x or x ==min_x:
                max_x = -1
                min_x = 10 ** 9 + 1
                for k in S.keys():
                    if k > max_x:
                        max_x = k
                    if k < min_x:
                        min_x = k
    else:
        print(max_x - min_x)
for _ in range(Q):
    query(LI())
