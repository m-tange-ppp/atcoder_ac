import sys
def I(): return int(sys.stdin.readline().rstrip())
def LI(): return list(map(int,sys.stdin.readline().rstrip().split()))
def MI(): return map(int,sys.stdin.readline().rstrip().split())
def S(): return sys.stdin.readline().rstrip()
def LS(): return list(sys.stdin.readline().rstrip().split())
def input(): return sys.stdin.readline().rstrip()

n,m = MI()
s = S()
clist = LI()
slist = [[] for _ in range(m)]
indexlist = [[] for _ in range(m)]

for index, c in enumerate(clist):
    slist[c - 1].append(s[index])
    indexlist[c - 1].append(index)

newlist = []
for s in slist:
    newlist.append(s[len(s) - 1:] + s[:len(s) - 1])
newlist = [item for sublist in newlist for item in sublist]
indexlist = [item for sublist in indexlist for item in sublist]
ans = list(zip(newlist, indexlist))
ans.sort(key=lambda x:x[1])
print("".join(str(s) for s, _ in ans))
