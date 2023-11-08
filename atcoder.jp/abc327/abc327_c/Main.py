import sys
def II(): return int(sys.stdin.readline().rstrip())
def LI(): return list(map(int,sys.stdin.readline().rstrip().split()))
def MI(): return map(int,sys.stdin.readline().rstrip().split())
def SI(): return sys.stdin.readline().rstrip()
def LS(): return list(sys.stdin.readline().rstrip().split())

A = [LI() for _ in range(9)]
nums = {1, 2, 3, 4, 5, 6, 7, 8, 9}
f = True
for i in range(9):
    r = set()
    for j in range(9):
        r.add(A[i][j])
    if r != nums:
        f = False
        break
else:
    for j in range(9):
        c = set()
        for i in range(9):
            c.add(A[i][j])
        if c != nums:
            f = False
            break
    else:
        for i in range(0, 7, 3):
            for j in range(0, 7, 3):
                s = set()
                for k in range(i, i + 3):
                    for l in range(j, j + 3):
                        s.add(A[k][l])
                if s != nums:
                    f = False
                    break
            else:
                continue
            break
print("Yes" if f else "No")