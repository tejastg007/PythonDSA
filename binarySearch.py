nums = [2, 3, 6, 7, 10, 12]
key = 122

left = 0
right = len(nums)-1

while left <= right:
    mid = (left+right)//2
    if nums[mid] == key:
        print(mid)
        exit()
    elif key > nums[mid]:
        left = mid+1
    else:
        right = mid-1
