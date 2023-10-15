n, a, b = map(int, input().split())
count = 0

for i in range(1, n + 1, 1):
    si = str(i)
    keta = len(si)
    sum = 0
    for j in range(keta):
        sum += int(si[j])
    if a<= sum <= b:
        count += i

print(count)