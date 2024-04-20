s = list(input())
nums = list(int(input()) for _ in range(len(s)-1))

for i in range(len(nums)):
    if i != len(nums)-1:
        s.remove(s[nums[i]])
        print(''.join(s))
    else:
        if nums[i] >= len(s):
            s.remove(s[-1])
            print(''.join(s))