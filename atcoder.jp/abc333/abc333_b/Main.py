import sys
def II(): return int(sys.stdin.readline().rstrip())
def LI(): return list(map(int,sys.stdin.readline().rstrip().split()))
def MI(): return map(int,sys.stdin.readline().rstrip().split())
def SI(): return sys.stdin.readline().rstrip()
def LS(): return list(sys.stdin.readline().rstrip().split())

S = SI()
T = SI()
ABC = ["A", "B", "C", "D", "E"]
s = []
t = []
for i in range(2):
    s.append(ABC.index(S[i]))
    t.append(ABC.index(T[i]))
ds = abs(s[0] - s[1])
dt = abs(t[0] - t[1])
s = {ds, dt}
if s == {1} or s == {4} or s == {1, 4} or s == {2} or s == {3} or s == {2, 3}:
    print("Yes")
    sys.exit()
else:
    print("No")