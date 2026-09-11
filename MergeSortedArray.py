# https://leetcode.com/problems/merge-sorted-array/description/?envType=problem-list-v2&envId=array

def merge(nums1, m, nums2, n):

    ptr1 = 0
    ptr2 = 0
    ans = []
    while ptr1 < m and ptr2 < n:
        if nums2[ptr2] < nums1[ptr1]:
            ans.append(nums2[ptr2])
            ptr2 = ptr2+1

        else:
            ans.append(nums1[ptr1])
            ptr1 = ptr1+1

    while ptr1 < m:
        ans.append(nums1[ptr1])
        ptr1 = ptr1+1

    while ptr2 < n:
        ans.append(nums2[ptr2])
        ptr2 = ptr2+1

    nums1 = ans
    print(nums1)


nums1 = [1, 2, 3, 0, 0, 0]
nums2 = [2, 5, 6]

merge(nums1, 3, nums2, len(nums2))
