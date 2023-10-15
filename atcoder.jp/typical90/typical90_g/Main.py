import bisect

N = int(input())
classes = list(map(int, input().split()))
classes.sort()
result = []
Q = int(input())
for _ in range(Q):
    st = int(input())
    i = bisect.bisect_left(classes, st)
    min_diff = 10 ** 10
    if i < N:
        min_diff = min(min_diff, abs(classes[i] - st))
    if i > 0:
        min_diff = min(min_diff, abs(classes[i - 1] - st))
    result.append(min_diff)
for a in result:
    print(a)