"""
给你两个按 非递减顺序 排列的整数数组 nums1 和 nums2，另有两个整数 m 和 n ，分别表示 nums1 和 nums2 中的元素数目。

请你 合并 nums2 到 nums1 中，使合并后的数组同样按 非递减顺序 排列。

注意：最终，合并后数组不应由函数返回，而是存储在数组 nums1 中。为了应对这种情况，nums1 的初始长度为 m + n，其中前 m 个元素表示应合并的元素，后 n 个元素为 0 ，应忽略。nums2 的长度为 n 。
"""
from sklearn.externals.array_api_compat.torch import where


# # 方法1
# def merge(nums1,nums2) :
#     nums1.extend(nums2)
#     nums1.sort()
#
# nums1 = [3, 6, 8]
# nums2 = [6, 2, 10]
# merge(nums1,nums2)
# print(nums1)
#
# # 逆序排序
# nums1.sort(reverse=True)
# # i是nums1的元素值
# for i in nums1:
#     print(i)


# 方法2 双指针
def merge(nums1, m, nums2, n):
    # 先把两个数组各自排序（关键！你之前就是缺这一步）
    # nums1[:m] = sorted(nums1[:m])
    # nums2.sort()

    # 标准双指针从后往前
    i = m - 1
    j = n - 1
    k = m + n - 1

    while i >= 0 and j >= 0:
        if nums1[i] > nums2[j]:
            nums1[k] = nums1[i]
            i -= 1
        else:
            nums1[k] = nums2[j]
            j -= 1
        k -= 1

    while j >= 0:
        nums1[k] = nums2[j]
        j -= 1
        k -= 1


# 测试
nums1 = [3, 6, 8, 0, 0, 0]
m = 3
nums2 = [2, 10, 11]
n = 3

merge(nums1, m, nums2, n)
print(nums1)  # [2, 3, 6, 6, 8, 10]
