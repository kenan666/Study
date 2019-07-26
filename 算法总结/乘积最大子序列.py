'''
给定一个整数数组 nums ，找出一个序列中乘积最大的连续子序列（该序列至少包含一个数）。

示例 1:
输入: [2,3,-2,4]
输出: 6
解释: 子数组 [2,3] 有最大乘积 6。

示例 2:
输入: [-2,0,-1]
输出: 0
解释: 结果不能为 2, 因为 [-2,-1] 不是子数组。

'''
'''
由于负值最小值 * 负数可能会变成最大值，正值最大值 * 负数也可能会变成最小值，所以我们还要多一步骤保留最小值。 

设 A[i] 为以 i 截止之子序列最大积，得转移公式A[i] = max(A[i - 1] * j, j)

考虑最小值成负数，故写成 A[i] = max(A[i - 1] * j, j, minv * j) 其中minv = min(A[i - 1] * j, j, minv * j)。

'''
def maxProduct(self, nums: List[int]) -> int:
    if nums == []:
        return 0
    a = [0] * len(nums)
    a[0] = nums[0]
    minv = 0
    for i,j in enumerate(nums):
        if i > 0:
            a[i] = max(a[i-1] * j, j, minv * j)
            minv = min(a[i-1] * j, j, minv * j)
    return max(a)

