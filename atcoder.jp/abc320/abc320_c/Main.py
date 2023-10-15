import sys
def II(): return int(sys.stdin.readline().rstrip())
def LI(): return list(map(int,sys.stdin.readline().rstrip().split()))
def MI(): return map(int,sys.stdin.readline().rstrip().split())
def SI(): return sys.stdin.readline().rstrip()
def LS(): return list(sys.stdin.readline().rstrip().split())

from itertools import permutations
M = II()
S_list = [SI() for _ in range(3)]

ans = 10 ** 9 
nums = [str(i) for i in range(10)]
f = ["0", "1", "2"]

for num in nums:
    if not (num in S_list[0] and num in S_list[1] and num in S_list[2]):
        continue
    flags = [list(T) for T in list(permutations(f))]

    for i in range(len(flags)):
        t = 0
        while flags[i]:
            for flag in flags[i]:
                if S_list[int(flag)][t % M] == num:
                    flags[i].remove(flag)
                    break
            t += 1
        if ans > t:
            ans = t

if ans == 10 ** 9:
    ans = 0

print(ans - 1)
