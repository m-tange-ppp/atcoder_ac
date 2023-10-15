import sys
def i(): return int(sys.stdin.readline().rstrip())
def li(): return list(map(int,sys.stdin.readline().rstrip().split()))
def mi(): return map(int,sys.stdin.readline().rstrip().split())
def s(): return sys.stdin.readline().rstrip()
def ls(): return list(sys.stdin.readline().rstrip().split())
def input(): return sys.stdin.readline().rstrip()

N, K = mi()
S_list = [[0] * 26 for _ in range(N)]

for i in range(N):
    S = s()
    for j in range(len(S)):
        S_list[i][ord(S[j]) - ord('a')] = 1

ans = 0
for i in range(2 ** N):
    c_list = [0] * 26
    for j in range(N):
        if i & (1 << j):
            for k in range(26):
                c_list[k] += S_list[j][k]
    n = 0
    for c in c_list:
        if c == K:n += 1
    if n > ans:ans = n

print(ans)