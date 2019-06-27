'''
给定一个非负整数数组，你最初位于数组的第一个位置。

数组中的每个元素代表你在该位置可以跳跃的最大长度。

你的目标是使用最少的跳跃次数到达数组的最后一个位置。

示例:

输入: [2,3,1,1,4]
输出: 2
解释: 跳到最后一个位置的最小跳跃数是 2。
     从下标为 0 跳到下标为 1 的位置，跳 1 步，然后跳 3 步到达数组的最后一个位置。

'''
#  动态规划
'''
动态方程为:dp[i] = min(dp[i], dp[j] + 1),j位置可以到达i 的位置
时间复杂度为 O(n^2)
'''
def jump(self, nums: List[int]) -> int:
    n = len ( nums )
    dp = [float("inf")] * n
    dp[0] = 0
    for i in range ( 1,len (nums)):
        for j in range (i):
            if nums[j] >= i-j:
                dp[i] = min(dp[i],dp[j]+1)
    return dp[-1]

# 贪心算法
'''
从一个位置跳到它能跳到的最远位置之间的都只需要一步!

所以,如果一开始都能跳到,后面再跳到的肯定步数要变多!
'''
def jump(self, nums: List[int]) -> int:
    n = len (nums)
    if n == 1:return0
    dp = [0] * n
    for i in range(n):
        for j in range (nums[i],0,-1):
            if i +j >= n-1 :returndp[i] + 1
            elif dp[i+j] == 0:
                dp[i+j] = dp[i] + 1
            else:
                break
    return False
