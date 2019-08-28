'''
给定一个非负整数数组和一个整数 m，你需要将这个数组分成 m 个非空的连续子数组。设计一个算法使得这 m 个子数组各自和的最大值最小。

注意:
数组长度 n 满足以下条件:

1 ≤ n ≤ 1000
1 ≤ m ≤ min(50, n)

示例:

输入:
nums = [7,2,5,10,8]
m = 2

输出:
18

解释:
一共有四种方法将nums分割为2个子数组。
其中最好的方式是将其分为[7,2,5] 和 [10,8]，
因为此时这两个子数组各自的和的最大值为18，在所有情况中最小。

'''
#--------参考解析--------------
'''
根据题意，可以得出，结果必定落在【max（nums）， sum（nums）】这个区间内，
因为左端点对应每个单独的元素构成一个子数组，右端点对应所有元素构成一个子数组。

然后可以利用二分查找法逐步缩小区间范围，当区间长度为1时，即找到了最终答案。

每次二分查找就是先算一个mid值，这个mid就是代表当前猜测的答案，然后模拟一下划分子数组的过程，可以得到用这个mid值会一共得到的子区间数cnt，
然后比较cnt和m的关系，来更新区间范围。

'''
def splitArray(self, nums, m):
    """
    :type nums: List[int]
    :type m: int
    :rtype: int
    """
    # max(nums), sum(nums)
    if len(nums) == m:
        return max(nums)
    
    lo, hi = max(nums), sum(nums)
    while(lo < hi):
        mid = (lo + hi) // 2 # 最大和
        
        #------以下在模拟划分子数组的过程
        temp, cnt = 0, 1
        for num in nums:
            temp += num
            # cnt += 1
            if temp > mid:#说明当前这个子数组的和已经超过了允许的最大值mid，需要把当前元素放在下一个子数组里
                temp = num
                cnt += 1
        # print temp, cnt, mid
        #------以上在模拟划分子数组的过程
        
        if cnt > m: #说明分出了比要求多的子数组，多切了几刀，说明mid应该加大，这样能使子数组的个数减少
            lo = mid + 1
        elif cnt <= m:
            hi = mid

    return lo


#------------最佳观光组合------------------
'''
给定正整数数组 A，A[i] 表示第 i 个观光景点的评分，并且两个景点 i 和 j 之间的距离为 j - i。

一对景点（i < j）组成的观光组合的得分为（A[i] + A[j] + i - j）：景点的评分之和减去它们两者之间的距离。

返回一对观光景点能取得的最高分。 

示例：

输入：[8,1,5,2,6]
输出：11
解释：i = 0, j = 2, A[i] + A[j] + i - j = 8 + 5 + 0 - 2 = 11

'''
#---------------参考题解-------------------
'''
1、已知题目要求 res = A[i] + A[j] + i - j （i < j） 的最大值，而对于输入中的每一个 A[j] 来说， 
它的值 A[j] 和它的下标 j 都是固定的，所以 A[j] - j 的值也是固定的。

2、因此，对于每个 A[j] 而言， 想要求 res 的最大值，也就是要求 A[i] + i （i < j） 的最大值，

3、所以不妨用一个变量 pre_max 记录当前元素 A[j] 之前的 A[i] + i 的最大值，

4、这样对于每个 A[j] 来说，都有 最大得分 = pre_max + A[j] - j，再从所有 A[j] 的最大得分里挑出最大值返回即可。

'''
def maxScoreSightseeingPair(self, A):
    """
    :type A: List[int]
    :rtype: int
    """
    res = 0
    pre_max = A[0] + 0 #初始值
    for j in range(1, len(A)):
        res = max(res, pre_max + A[j] - j) #判断能否刷新res
        pre_max = max(pre_max, A[j] + j) #判断能否刷新pre_max， 得到更大的A[i] + i
            
    return res

# 时间复杂度 O(n)
# 空间复杂度 O(1)


#------------------爱吃香蕉的珂珂----------------
'''
珂珂喜欢吃香蕉。这里有 N 堆香蕉，第 i 堆中有 piles[i] 根香蕉。警卫已经离开了，将在 H 小时后回来。

珂珂可以决定她吃香蕉的速度 K （单位：根/小时）。每个小时，她将会选择一堆香蕉，从中吃掉 K 根。
如果这堆香蕉少于 K 根，她将吃掉这堆的所有香蕉，然后这一小时内不会再吃更多的香蕉。  

珂珂喜欢慢慢吃，但仍然想在警卫回来前吃掉所有的香蕉。

返回她可以在 H 小时内吃掉所有香蕉的最小速度 K（K 为整数）。

 

示例 1：
输入: piles = [3,6,7,11], H = 8
输出: 4

示例 2：
输入: piles = [30,11,23,4,20], H = 5
输出: 30

示例 3：
输入: piles = [30,11,23,4,20], H = 6
输出: 23

'''
#-----------参考官方题解----------------

#----思路-----
'''
如果珂珂能以 K 的进食速度最终吃完所有的香蕉（在 H 小时内），那么她也可以用更快的速度吃完。

当珂珂能以 K 的进食速度吃完香蕉时，我们令 possible(K) 为 true，那么就存在 X 使得当 K >= X 时， possible(K) = True。

举个例子，当初始条件为 piles = [3, 6, 7, 11] 和 H = 8 时，
存在 X = 4 使得 possible(1) = possible(2) = possible(3) = False，且 possible(4) = possible(5) = ... = True。

'''

#---------算法-------------
'''
可以二分查找 possible(K) 的值来找到第一个使得 possible(X) 为 True 的 X：这将是我们的答案。我们的循环中，
不变量 possible(hi) 总为 True， lo 总小于等于答案。

为了找到 possible(K) 的值， (即珂珂是否能以 K 的进食速度在 H 小时内吃完所有的香蕉），模拟这一情景。
对于每一堆（大小 p > 0），我们可以推断出珂珂将在 Math.ceil(p / K) = ((p-1) // K) + 1 小时内吃完这一堆，
我们将每一堆的完成时间加在一起并与 H 进行比较。

'''
def minEatingSpeed(self, piles, H):
    def possible(K):
        return sum((p-1) / K + 1 for p in piles) <= H

    low, high = 1, max(piles)

    while low < high:
        mid = (low + high) / 2
        if not possible(mid):
            low = mid + 1
        else:
            high = mid

    return low

# 时间复杂度O(NlogW)
# 空间复杂度O(1)

#----------解法2----> 超时---值得考虑---

def minSpeed(piles, H):
    K = 1 # 吃的最少
    total = H+1 # 总共用时
    while total>H:
        total = 0
        for i in range(len(piles)):
            #---注解---
            a = piles[i]//K
            if (piles[i]%K)==0:
                total += a
            else:
                total = total+a+1
            #total = total+a if (piles[i]%K)==0 else total+a+1
        K = K+1
    return (K-1)

'''
注解 ： a 首先考虑 每小时 k 的时候，一堆吃一个小时 ，是否还有剩余，
        没有的话  总用时 total 则 加 a ，否则  需要  +1 小时吃完一堆
'''