#from bisect import bisect_left, bisect_right
#from itertools import permutations, combinations
from collections import defaultdict, deque
#from math import gcd
# from heapq import heapify, heappush, heappop
import sys
sys.setrecursionlimit(10**6)
def ii(): return int(sys.stdin.readline().rstrip())
def mi(d=0): return map(lambda x:int(x)-d ,sys.stdin.readline().rstrip().split())
def li(d=0): return list(int(x)-d for x in sys.stdin.readline().rstrip().split())
def si(): return sys.stdin.readline().rstrip()
INF=float('inf'); MOD=998244353 #10**9+7

N, K = mi()
P = li()

if K == 1:
    print(0)
    sys.exit()

ans = INF
v_i_list = [[v, i] for i, v in enumerate(P)]
v_i_list.sort(key=lambda x:x[0])

def segmin(x, y):
    return min(x, y)
ide_ele_min = INF

def segmax(x, y):
    return max(x, y)
ide_ele_max = 0

class SegTree:
    """
    init(init_val, ide_ele): 配列init_valで初期化 O(N)
    update(k, x): k番目の値をxに更新 O(N)
    query(l, r): 区間[l, r)をsegfuncしたものを返す O(logN)
    """
    def __init__(self, init_val, segfunc, ide_ele):
        """
        init_val: 配列の初期値
        segfunc: 区間にしたい操作
        ide_ele: 単位元
        n: 要素数
        num: n以上の最小の2のべき乗
        tree: セグメント木(1-index)
        """
        n = len(init_val)
        self.segfunc = segfunc
        self.ide_ele = ide_ele
        self.num = 1 << (n - 1).bit_length()
        self.tree = [ide_ele] * 2 * self.num
        # 配列の値を葉にセット
        for i in range(n):
            self.tree[self.num + i] = init_val[i]
        # 構築していく
        for i in range(self.num - 1, 0, -1):
            self.tree[i] = self.segfunc(self.tree[2 * i], self.tree[2 * i + 1])

    def update(self, k, x):
        """
        k番目の値をxに更新
        k: index(0-index)
        x: update value
        """
        k += self.num
        self.tree[k] = x
        while k > 1:
            self.tree[k >> 1] = self.segfunc(self.tree[k], self.tree[k ^ 1])
            k >>= 1

    def query(self, l, r):
        """
        [l, r)のsegfuncしたものを得る
        l: index(0-index)
        r: index(0-index)
        """
        res = self.ide_ele

        l += self.num
        r += self.num
        while l < r:
            if l & 1:
                res = self.segfunc(res, self.tree[l])
                l += 1
            if r & 1:
                res = self.segfunc(res, self.tree[r - 1])
            l >>= 1
            r >>= 1
        return res

minseg = SegTree([0] * K, segmin, ide_ele_min)
maxseg = SegTree([0] * K, segmax, ide_ele_max)
for i in range(K):
    minseg.update(i, v_i_list[i][1])
    maxseg.update(i, v_i_list[i][1])
l = minseg.query(0, K)
r = maxseg.query(0, K)
ans = r - l
for i in range(K, N):
    minseg.update(i % K, v_i_list[i][1])
    maxseg.update(i % K, v_i_list[i][1])
    if v_i_list[i][1] < l:
        l = v_i_list[i][1]
    elif v_i_list[i][1] > r:
        r = v_i_list[i][1]
    elif v_i_list[i - K][1] == l:
        l = minseg.query(0, K)
    elif v_i_list[i - K][1] == r:
        r = maxseg.query(0, K)
    if r - l < ans:
        ans = r - l
print(ans)