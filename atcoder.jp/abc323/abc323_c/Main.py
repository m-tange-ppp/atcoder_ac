import sys
def II(): return int(sys.stdin.readline().rstrip())
def LI(): return list(map(int,sys.stdin.readline().rstrip().split()))
def MI(): return map(int,sys.stdin.readline().rstrip().split())
def SI(): return sys.stdin.readline().rstrip()
def LS(): return list(sys.stdin.readline().rstrip().split())

N, M = MI()
A = LI()
sorted_A = []
for i in range(M):
    sorted_A.append([i, A[i]])
sorted_A.sort(reverse=True, key=lambda x:x[1])
S = []
solved = []

for i in range(N):
    s = SI()
    solved.append(s)
    point = i + 1
    for i in range(M):
        if s[i] == "o":
            point += A[i]
    S.append(point)

max_now = max(S)
for i in range(N):
    now = S[i]
    s = solved[i]
    ind = 0
    count = 0
    if max_now != now:
        while now < max_now:
            pro = sorted_A[ind]
            ind += 1
            if s[pro[0]] != "o":
                now += pro[1]
                count += 1
    print(count)