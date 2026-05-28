'''
给定一个大小为 n 的数组 nums ，返回其中的多数元素。多数元素是指在数组中出现次数 大于 ⌊ n/2 ⌋ 的元素。

你可以假设数组是非空的，并且给定的数组总是存在多数元素
'''


def num_most(nums):
    # 遍历数组，维护一个候选元素 candidate 和计数器 count
    candidate = None
    count = 0
    for num in nums:
        # count == 0 时，把当前元素设为候选
        if count == 0:
            candidate = num
        # 当前元素等于候选时  count + 1，否则 count - 1  三元表达式
        count += 1 if num == candidate else -1

    num1 = nums.count(candidate)
    return candidate, num1


# 三元表达式 ： 变量 = 值1 if 条件 else 值2
# [2,1,3,2,3,22,2,2,3,2,2]
nums1 = input()  # 终端输入
print(num_most(nums1))


def method_new(nums):
    count = 0
    houxuan = None
    for num in nums:
        if count == 0:
            houxuan = num
        if houxuan == num:
            count += 1
        else:
            count -= 1
    return houxuan, nums.count(houxuan)

nums2 = [2,1,3,2,3,22,2,2,3,2,2]
print(method_new(nums1))
