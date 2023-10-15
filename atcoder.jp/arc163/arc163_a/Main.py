import sys

input = sys.stdin.readline

T = int(input())
ans = []

for _ in range(T):
    N = int(input())
    S = input().strip()
    f = False
    for i in range(1, len(S)):
        s1 = S[:i]
        s2 = S[i:]
        if s1 < s2:
            f = True
            break
        else:
            continue
    ans.append("Yes" if f == True else "No")

for a in ans:
    print(a)