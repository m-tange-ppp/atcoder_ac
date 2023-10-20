import sys
def II(): return int(sys.stdin.readline().rstrip())
def LI(): return list(map(int,sys.stdin.readline().rstrip().split()))
def MI(): return map(int,sys.stdin.readline().rstrip().split())
def SI(): return sys.stdin.readline().rstrip()
def LS(): return list(sys.stdin.readline().rstrip().split())

S = SI()
T = SI()
list_S = [[S[0], 1]]
list_T = [[T[0], 1]]
for i in range(1, len(S)):
    a = S[i]
    if list_S[-1][0] == a:
        list_S[-1][1] += 1
    else:
        list_S.append([a, 1])
for i in range(1, len(T)):
    a = T[i]
    if list_T[-1][0] == a:
        list_T[-1][1] += 1
    else:
        list_T.append([a, 1])

flag = True
if len(list_S) != len(list_T):
    flag = False
else:
    for i in range(len(list_S)):
        s = list_S[i]
        t = list_T[i]
        if not (s[0] == t[0] and (s[1] == t[1] or 1 < s[1] < t[1])):
            flag = False
            break
        else:
            continue
        break

print("Yes" if flag else "No")
