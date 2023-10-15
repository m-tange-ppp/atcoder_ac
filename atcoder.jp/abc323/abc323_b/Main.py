import sys
def II(): return int(sys.stdin.readline().rstrip())
def LI(): return list(map(int,sys.stdin.readline().rstrip().split()))
def MI(): return map(int,sys.stdin.readline().rstrip().split())
def SI(): return sys.stdin.readline().rstrip()
def LS(): return list(sys.stdin.readline().rstrip().split())

N = II()
wins = []
for i in range(N):
    S = SI()
    count = 0
    for c in S:
        if c == "o":
            count += 1
    wins.append([i, count])
wins.sort(key=lambda x:x[1], reverse=True)
print(*[x[0] + 1 for x in wins])