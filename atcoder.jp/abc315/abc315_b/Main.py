import sys
def I(): return int(sys.stdin.readline().rstrip())
def LI(): return list(map(int,sys.stdin.readline().rstrip().split()))
def MI(): return map(int,sys.stdin.readline().rstrip().split())
def S(): return sys.stdin.readline().rstrip()
def LS(): return list(sys.stdin.readline().rstrip().split())
def input(): return sys.stdin.readline().rstrip()

m = I()
d = LI()
sum_days = [d[0]]
for i in range(len(d) - 1):
    sum_days.append(sum_days[i] + d[i + 1])

mid = (sum_days[-1] + 1) // 2
for n, sum in enumerate(sum_days):
    if mid - sum <= 0:
        last_m = n + 1
        break

if last_m == 1:
    last_d = mid
else:
    last_d = mid - sum_days[last_m - 2]

print(f"{last_m} {last_d}")