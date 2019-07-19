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
