'''
给定一个整数数组 nums，将数组中的元素向右轮转 k 个位置，其中 k 是非负数。

示例 1:

输入: nums = [1,2,3,4,5,6,7], k = 3
输出: [5,6,7,1,2,3,4]
解释:
向右轮转 1 步: [7,1,2,3,4,5,6]
向右轮转 2 步: [6,7,1,2,3,4,5]
向右轮转 3 步: [5,6,7,1,2,3,4]
示例 2:

输入：nums = [-1,-100,3,99], k = 2
输出：[3,99,-1,-100]
解释:
向右轮转 1 步: [99,-1,-100,3]
向右轮转 2 步: [3,99,-1,-100]
'''
# 自己想的  力扣给的结果为错
def cyclic(nums,k):
    # 引入一个新数组
    nums1 = []
    # 先遍历 数组 后k 位
    for i in range(len(nums)-k,len(nums)):
        nums1.append(nums[i])
    # 再遍历 数组 前几位
    for i in range(0,len(nums)-k):
        nums1.append(nums[i])
    nums[:] = nums1
    return nums

nums = [1,2,3,4,5,6,7]
k = 3
print(cyclic(nums, k))

# 方法二
def cyclic2(nums,k):
    k = k % len(nums)   #处理 k 比数组长的情况
    nums[:] = nums[-k:] + nums[:-k]
    return nums


nums2 = [1,2,3,4,5,6,7]
print(cyclic2(nums2, 11))
print(k % len(nums))
print(nums2[:])
print(nums2[-3:])
print(nums2[:-3])