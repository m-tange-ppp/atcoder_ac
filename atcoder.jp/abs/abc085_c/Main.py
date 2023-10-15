n, a = map(int, input().split())
f = False

for i in range(n + 1):
    for j in range(n - i + 1):
        if 10000 * i + 5000 * j + 1000 * (n - i - j) == a:
            print(f"{i} {j} {n - i - j}")
            f = True
            break
        if f:
            break
    if f:
        break

if not f:
    print("-1 -1 -1")