'''
给你一个 非严格递增排列 的数组 nums ，请你 原地 删除重复出现的元素，使每个元素 只出现一次 ，返回删除后数组的新长度。元素的 相对顺序 应该保持 一致 。然后返回 nums 中唯一元素的个数。

考虑 nums 的唯一元素的数量为 k。去重后，返回唯一元素的数量 k。

nums 的前 k 个元素应包含 排序后 的唯一数字。下标 k - 1 之后的剩余元素可以忽略。
'''


def removeDuplicates(nums):
    if not nums:
        return 0
    k = 1  # 第一个元素一定保留
    for i in range(1, len(nums)):
        if nums[i] != nums[i - 1]:  # 和上一个保留的不同，就是新元素
            nums[k] = nums[i]
            k += 1
    return k




nums = [1, 1, 3, 3, 4, 5, 12, 23, 45, 45]
k = removeDuplicates(nums)
print(nums[:k])  # [1, 3, 4, 5, 12, 23, 45]
print(k)         # 7

for i in (1,3):
    print('22')