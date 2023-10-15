import sys
def I(): return int(sys.stdin.readline().rstrip())
def LI(): return list(map(int,sys.stdin.readline().rstrip().split()))
def MI(): return map(int,sys.stdin.readline().rstrip().split())
def S(): return sys.stdin.readline().rstrip()
def LS(): return list(sys.stdin.readline().rstrip().split())
def input(): return sys.stdin.readline().rstrip()

n = I()
s_list = [[] for _ in range(n)]
max_s = 0
max_f = -1
for _ in range(n):
    f,s = MI()
    s_list[f - 1].append(s)
    if s > max_s:
        max_s = s
        max_f = f - 1

s1, s2 = 0, 0
for i in range(n):
    if i == max_f and len(s_list[i]) > 1:
        sorted_list = sorted(s_list[i], reverse=True)
        s1 = sorted_list[1] // 2
    elif i != max_f:
        for s in s_list[i]:
            if s > s2:
                s2 = s
second = max(s1, s2)

print(max_s + second)