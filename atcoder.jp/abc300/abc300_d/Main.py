from bisect import bisect_left, bisect_right
#from itertools import permutations, combinations
#from collections import defaultdict, deque
#from math import gcd,lcm
#from heapq import heapify, heappush, heappop
import math
import sys
sys.setrecursionlimit(10**6)
def ii(): return int(sys.stdin.readline().rstrip())
def mi(d=0): return map(lambda x:int(x)-d ,sys.stdin.readline().rstrip().split())
def li(d=0): return list(int(x)-d for x in sys.stdin.readline().rstrip().split())
def si(): return sys.stdin.readline().rstrip()
inf=float('inf'); MOD=998244353 #10**9+7

N = ii()

def prime(n):
    is_prime = [True] * (n + 1)
    is_prime[0], is_prime[1] = False, False
    for i in range(2, int(math.sqrt(n)) + 1):
        if is_prime[i]:
            for j in range(2 * i, n + 1, i):
                is_prime[j] = False
    return is_prime

hurui = prime(int(math.sqrt(N)) + 1)
prime_list = []
for i in range(int(math.sqrt(N)) + 1):
    if hurui[i]:
        prime_list.append(i)
# print(*prime_list)

ans = 0

L = len(prime_list)
for i in range(L):
    a = prime_list[i]
    aa = a ** 2
    r = bisect_right(prime_list, int(math.sqrt(N // a ** 2))) - 1
    if r - i <= 1:
        break
    while r - i > 1:
        cc = prime_list[r] ** 2
        for j in range(i + 1, r):
            if aa * prime_list[j] * cc <= N:
                ans += 1
            else:
                break
        r -= 1
print(ans)