import sys
def II(): return int(sys.stdin.readline().rstrip())
def LI(): return list(map(int,sys.stdin.readline().rstrip().split()))
def MI(): return map(int,sys.stdin.readline().rstrip().split())
def SI(): return sys.stdin.readline().rstrip()
def LS(): return list(sys.stdin.readline().rstrip().split())

INPUT = LS()
N = int(INPUT[0])
T = INPUT[1]
ans = []

for i in range(N):
    S = SI()
    if S == T:
        ans.append(i)
    elif len(S) - len(T) == -1:
        if len(S) != 1:
            count_s = 0
            count_t = 0
            miss = 0
            while miss < 2 and count_s < len(S) and count_t < len(T):
                while count_t < len(T) and S[count_s] != T[count_t] and miss < 2 :
                    count_t += 1
                    miss += 1
                count_s += 1
                count_t += 1
            if miss < 2:
                ans.append(i)
        else:
            if S in T:
                ans.append(i)
    elif len(S) - len(T) == 1:
        if len(T) != 1:
            count_s = 0
            count_t = 0
            miss = 0
            while miss < 2 and count_t < len(T) and count_s < len(S):
                while count_s < len(S) and S[count_s] != T[count_t] and miss < 2 :
                    count_s += 1
                    miss += 1
                count_s += 1
                count_t += 1
            if miss < 2:
                ans.append(i)
        else:
            if T in S:
                ans.append(i)
    elif len(S) - len(T) == 0:
        count = 0
        for j in range(len(S)):
            if S[j] != T[j]:
                count += 1
        if count == 1:
            ans.append(i)
            
print(len(ans))
print(*[i + 1 for i in ans])