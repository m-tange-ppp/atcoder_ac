n = int(input())
for _ in range(n):
    num = int(input())
    go = [i for i in range(1, num + 1)]
    order = list(map(int, input().split()))
    tuples = list(zip(go, order))
    tuples = sorted(tuples, key=lambda x: x[1])
    count = 1
    a = tuples[0][0]
    for i in range(num):
        if a < tuples[i][0]:
            a = tuples[i][0]
            count += 1
    print(count)