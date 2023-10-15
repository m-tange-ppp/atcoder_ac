nums = list(map(int, input().split()))
flag = True

for i in range(len(nums)):
    if i != 0 and nums[i - 1] > nums[i]:
        print("No")
        flag = False
        break
    if nums[i] < 100 or 675 < nums[i]:
        print("No")
        flag = False
        break
    if nums[i] % 25 != 0:
        print("No")
        flag = False
        break

if flag:
    print("Yes")