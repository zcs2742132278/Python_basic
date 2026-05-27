'''
给你一个数组 nums 和一个值 val，你需要 原地 移除所有数值等于 val 的元素。元素的顺序可能发生改变。然后返回 nums 中与 val 不同的元素的数量。

假设 nums 中不等于 val 的元素数量为 k，要通过此题，您需要执行以下操作：

更改 nums 数组，使 nums 的前 k 个元素包含不等于 val 的元素。nums 的其余元素和 nums 的大小并不重要。
返回 k。
'''


# def removeElement(nums, val):
#     k = 0
#     for i in range(len(nums)):
#         if nums[i] != val:
#             nums[k] = nums[i]
#             k += 1
#     return k
def removeElement(nums,val):
    k=0
    i=0
    while i < len(nums):
        if nums[i] != val:
            nums[k] = nums[i]
            k +=1
        i += 1
    return k

nums1 = [1, 3, 5, 9, 10, 10, 22, 10, 6]
k = removeElement(nums1, 10)
# :k 取k的从0到k-1
print(nums1[:k])  # [1, 3, 5, 9, 22, 6]
print(k)          # 6