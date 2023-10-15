n = input()
nums = list(map(int, input().split()))
c = 0
f = False

while True:
    for i in range(len(nums)):
        if nums[i] % 2 != 0:
            f = True
            break
        else:
            nums[i] = nums[i] / 2
    if f:
        break
    c += 1

print(c)