'''
给定一个数组，它的第 i 个元素是一支给定股票第 i 天的价格。

如果你最多只允许完成一笔交易（即买入和卖出一支股票），设计一个算法来计算你所能获取的最大利润。

注意你不能在买入股票前卖出股票。

示例 1:

输入: [7,1,5,3,6,4]
输出: 5
解释: 在第 2 天（股票价格 = 1）的时候买入，在第 5 天（股票价格 = 6）的时候卖出，最大利润 = 6-1 = 5 。
     注意利润不能是 7-1 = 6, 因为卖出价格需要大于买入价格。
示例 2:

输入: [7,6,4,3,1]
输出: 0
解释: 在这种情况下, 没有交易完成, 所以最大利润为 0。

'''
# 解1  Kadane's Algorithm 参考维基百科
'''
Kadane算法
Kadane算法扫描一次整个数列的所有数值，在每一个扫描点计算以该点数值为结束点的子数列的最大和（正数和）。该子数列由两部分组成：
以前一个位置为结束点的最大子数列、该位置的数值。因为该算法用到了“最佳子结构”（以每个位置为终点的最大子数列都是基于其前一位置的最大子数列计算得出），
该算法可看成动态规划的一个例子。

'''

#------------------------------------------------------以下为Kadane算法的实现---------------------------------------------------
# 算法可用如下Python代码实现：
def max_subarray(A):
    max_ending_here = max_so_far = A[0]
    for x in A[1:]:
        max_ending_here = max(x, max_ending_here + x)
        max_so_far = max(max_so_far, max_ending_here)
    return max_so_far

# 该问题的一个变种是：如果数列中含有负数元素，允许返回长度为零的子数列。该问题可用如下代码解决：
def max_subarray(A):
    max_ending_here = max_so_far = 0
    for x in A:
        max_ending_here = max(0, max_ending_here + x)
        max_so_far = max(max_so_far, max_ending_here)
    return max_so_far
# 这种算法稍作修改就可以记录最大子数列的起始位置。Kadane算法时间复杂度为 O(n),空间复杂度为O(1)。
#-------------------------------------------------------------------------------------------------------------------------------

# 简单来说
'''
如果一个数组为[a1, a2, a3, a4, a5],

a5 - a1 = (a2 - a1) + (a3 - a2) + (a4 - a3) + (a5 - a4)

'''
def maxProfit(self, prices: List[int]) -> int:
    res = 0
    cur_max = 0
    for i in range(1, len(prices)):
        # 记录目前位置以i为结束的, 差值最大值
        cur_max += (prices[i] - prices[i-1])
        # 如果 cur_max 小于0 说明要改变起始的位置
        cur_max = max(0, cur_max)
        res = max(res, cur_max)
    return res

# 解2   
# 解2  动态规划   遍历数组,记录前面最小的价格,用当天价格减去最小价格,一定是这天可以获得最大利润
def maxProfit(self, prices: List[int]) -> int:
    if not prices: return 0
    res = 0
    cur_min = prices[0]
    for i in range(1, len(prices)):
        res = max(res, prices[i] - cur_min)
        cur_min = min(cur_min, prices[i])
    return res


#  相关问题
#  买卖股票的最佳时机2 
'''
给定一个数组，它的第 i 个元素是一支给定股票第 i 天的价格。

设计一个算法来计算你所能获取的最大利润。你可以尽可能地完成更多的交易（多次买卖一支股票）。

注意：你不能同时参与多笔交易（你必须在再次购买前出售掉之前的股票）。

示例 1:

输入: [7,1,5,3,6,4]
输出: 7
解释: 在第 2 天（股票价格 = 1）的时候买入，在第 3 天（股票价格 = 5）的时候卖出, 这笔交易所能获得利润 = 5-1 = 4 。
     随后，在第 4 天（股票价格 = 3）的时候买入，在第 5 天（股票价格 = 6）的时候卖出, 这笔交易所能获得利润 = 6-3 = 3 。
示例 2:

输入: [1,2,3,4,5]
输出: 4
解释: 在第 1 天（股票价格 = 1）的时候买入，在第 5 天 （股票价格 = 5）的时候卖出, 这笔交易所能获得利润 = 5-1 = 4 。
     注意你不能在第 1 天和第 2 天接连购买股票，之后再将它们卖出。
     因为这样属于同时参与了多笔交易，你必须在再次购买前出售掉之前的股票。
示例 3:

输入: [7,6,4,3,1]
输出: 0
解释: 在这种情况下, 没有交易完成, 所以最大利润为 0。

'''

# 解1
'''
同一天可以先卖出,再买入(等于这天没有操作),比如 [1, 2, 3],我们可以第一天买入,第二天卖出得 2 - 1, 第二天再买入,第三天卖出得3 - 2,总共2,
相当于第二天不用操作也行.受上一题思路,如果存在数组为[a1, a2, a3] ,那么 a3 - a1 = (a2 - a1) + (a3 - a2),所以有

'''
def maxProfit(self, prices: List[int]) -> int:
    n = len(prices)
    if n == 0: return 0
    res = 0
    for i in range(1, n):
        res += max(0, prices[i] - prices[i-1])
    return res

# 解2 动态规划
def maxProfit(self, prices: List[int]) -> int:
    if not prices: return 0
    buy = -prices[0]
    sell = 0
    for p in prices[1:]:
        buy = max(buy, sell - p)
        sell = max(sell, p + buy)
    return sell


# 买卖股票的最佳时机3
'''
给定一个数组，它的第 i 个元素是一支给定的股票在第 i 天的价格。

设计一个算法来计算你所能获取的最大利润。你最多可以完成 两笔 交易。

注意: 你不能同时参与多笔交易（你必须在再次购买前出售掉之前的股票）。

示例 1:

输入: [3,3,5,0,0,3,1,4]
输出: 6
解释: 在第 4 天（股票价格 = 0）的时候买入，在第 6 天（股票价格 = 3）的时候卖出，这笔交易所能获得利润 = 3-0 = 3 。
     随后，在第 7 天（股票价格 = 1）的时候买入，在第 8 天 （股票价格 = 4）的时候卖出，这笔交易所能获得利润 = 4-1 = 3 。
示例 2:

输入: [1,2,3,4,5]
输出: 4
解释: 在第 1 天（股票价格 = 1）的时候买入，在第 5 天 （股票价格 = 5）的时候卖出, 这笔交易所能获得利润 = 5-1 = 4 。   
     注意你不能在第 1 天和第 2 天接连购买股票，之后再将它们卖出。   
     因为这样属于同时参与了多笔交易，你必须在再次购买前出售掉之前的股票。
示例 3:

输入: [7,6,4,3,1] 
输出: 0 
解释: 在这个情况下, 没有交易完成, 所以最大利润为 0。

'''
# 动态规划   大佬阶梯解题思路
#  1
# dp[k][i]到第i天经过k次交易得到最大的利润.动态方程: dp[k][i] = max(dp[k][i], dp[k-1][j-1] + prices[i] - prices[j]) 0 <=j <= i
def maxProfit(self, prices: List[int]) -> int:
    if not prices: return 0
    n = len(prices)
    dp = [[0] * n for _ in range(3)]
    for k in range(1, 3):
        for i in range(1, n):
            dp[k][i] = max(prices[i] - prices[0], dp[k][i-1])
            for j in range(1, i + 1):
                dp[k][i] = max(dp[k][i],  dp[k - 1][j - 1] + prices[i] - prices[j])
    #print(dp)
    return dp[-1][-1]

'''
测试用例过不了, 看了大佬的题解, 有一个小技巧技术 把dp[k-1][j-1] - prices[j]看成一个整体, 
因为j独立与i,可以减少最内侧的循环.换句话说,就是先求dp[k-1][j-1] - prices[j]最大值, 再求+ prices[i]的最大值,

'''
def maxProfit(self, prices):
    if not prices: return 0
    n = len(prices)
    dp = [[0] * n for _ in range(3)]
    for k in range(1, 3):
        for i in range(1, n):
            # 处理边界情况 j == 0
            pre_max = -prices[0]
            for j in range(1, i + 1):
                pre_max = max(pre_max, dp[k - 1][j - 1] - prices[j])
            dp[k][i] = max(dp[k][i - 1], prices[i] + pre_max)
    return dp[-1][-1]

# 此时。时间复杂度为O(n^2)

# 进一步改写
def maxProfit(self, prices):
    if not prices: return 0
    n = len(prices)
    dp = [[0] * n for _ in range(3)]
    for k in range(1, 3):
        pre_max = -prices[0]
        for i in range(1, n):
            pre_max = max(pre_max, dp[k - 1][i - 1] - prices[i])
            dp[k][i] = max(dp[k][i - 1], prices[i] + pre_max)
    return dp[-1][-1]
    
# 此时时间复杂度为O(n)