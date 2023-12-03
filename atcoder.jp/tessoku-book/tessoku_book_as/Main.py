import sys
def II(): return int(sys.stdin.readline().rstrip())
def LI(): return list(map(int,sys.stdin.readline().rstrip().split()))
def MI(): return map(int,sys.stdin.readline().rstrip().split())
def SI(): return sys.stdin.readline().rstrip()
def LS(): return list(sys.stdin.readline().rstrip().split())

inp = LS()
N, C = int(inp[0]), inp[1]
A = SI()

count = 0
for c in A:
    if c == "R":
        count = (count + 1) % 3
    elif c == "B":
        count = (count + 2) % 3
    else:
        pass

if count == 0 and C == "W" or count == 1 and C == "R" or count == 2 and C == "B":
    print("Yes")
else:
    print("No")