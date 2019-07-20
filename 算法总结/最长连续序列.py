'''
给定一个未排序的整数数组，找出最长连续序列的长度。

要求算法的时间复杂度为 O(n)。

示例:

输入: [100, 4, 200, 1, 3, 2]
输出: 4
解释: 最长连续序列是 [1, 2, 3, 4]。它的长度为 4。

'''
#解1 集合
# 查询时间复杂度为O(1)  但是与要求不符合
def longestConsecutive(self, nums: List[int]) -> int:
    nums = set(nums)
    res = 0
    for num in nums:
        # 判断是否是第一个数字
        if num - 1 not in nums:
            tmp = 1
            while num + 1 in nums:
                num += 1
                tmp += 1
            res = max(res, tmp)
    return res

# 解2 字典
# 遍历数组，用字典（哈希）记录目前与该值可以组成的最长序列
def longestConsecutive(self, nums: List[int]) -> int:
    # 记录首尾值的最长长度
    lookup = {}
    res = 0
    for num in nums:
        if num not in lookup:
            # 判断左右是否可以连起来
            left = lookup[num - 1] if num - 1 in lookup else 0
            right = lookup[num + 1] if num + 1 in lookup else 0
            # 记录长度
            lookup[num] = left + right + 1
            # 把头尾都设置为最长长度
            lookup[num - left] = left + right + 1
            lookup[num + right] = left + right + 1
            res = max(res, left + right + 1)
    return res



