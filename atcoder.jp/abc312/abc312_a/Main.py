import sys
from collections import deque
def I(): return int(sys.stdin.readline().rstrip())
def LI(): return list(map(int,sys.stdin.readline().rstrip().split()))
def MI(): return map(int,sys.stdin.readline().rstrip().split())
def S(): return sys.stdin.readline().rstrip()
def LS(): return list(sys.stdin.readline().rstrip().split())
def input(): return sys.stdin.readline().rstrip()

s = S()
my_set = {"ACE", "BDF", "CEG", "DFA", "EGB", "FAC", "GBD"}
print("Yes" if s in my_set else "No")