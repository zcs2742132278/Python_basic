'''
给你一个有序数组 nums ，请你 原地 删除重复出现的元素，使得出现次数超过两次的元素只出现两次 ，返回删除后数组的新长度。

不要使用额外的数组空间，你必须在 原地 修改输入数组 并在使用 O(1) 额外空间的条件下完成。
'''

# 有序数组
def removeDuplicates(nums):
    if len(nums) <= 2:
        return len(nums)
    k = 2  # 前两个元素一定保留
    for i in range(2, len(nums)):
        if nums[i] != nums[k - 2]:  # 和往前数第2个不同，说明还没出现两次
            nums[k] = nums[i]
            k += 1
    return k


nums = [1, 1, 1, 2, 2, 2, 2, 3, 3, 3, 3]
k = removeDuplicates(nums)
print(nums[:k])  # [1, 1, 2, 2, 3, 3]
print(k)         # 6