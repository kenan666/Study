'''
给定一个整数数组 nums ，找到一个具有最大和的连续子数组（子数组最少包含一个元素），返回其最大和。

示例:

输入: [-2,1,-3,4,-1,2,1,-5,4],
输出: 6
解释: 连续子数组 [4,-1,2,1] 的和最大，为 6。

'''
'''
思路一: 动态规划

当前面的总和是负数的,加上去一定会使总和减小,不如从自己重新开始.

例如,[-2,1,-3,4]

1就不需要加前面-2,自己可以重新开始.

'''
def maxSubArray(self, nums: List[int]) -> int:
    n = len(nums)
    dp = [0] * n
    dp[0] = nums[0]
    res = nums[0]
    for i in range (1,n):
        dp[i] = max ( dp[i-1] + nums[i] ,nums[i])
        res = max(dp[i],res)
    return res


'''
sum(i,j) = sum(0,j) - sum(0,i)

我们只要记录前i总和最小值就可以了!

时间复杂度为 o(n)

'''
def maxSubArray(self, nums: List[int]) -> int:
    cur_sum = 0
    min_sum = 0
    res = float("-inf")
    for num in nums:
        cur_sum += num
        res = max(res,cur_sum - min_sum)
        min_sum = min(min_sum,cur_sum)
    return res


'''
动态规划算法小结

动态规划：   （1）动态规划常常适用于有重叠子问题[1]和最优子结构性质的问题，动态规划方法所耗时间往往远少于朴素解法。

            （2）动态规划背后的基本思想非常简单。大致上，若要解一个给定问题，我们需要解其不同部分（即子问题），再根据子问题的解以得出原问题的解。

            **************
            通常许多子问题非常相似，为此动态规划法试图仅仅解决每个子问题一次，从而减少计算量：一旦某个给定子问题的解已经算出，则将其记忆化存储，以便下次需要同一个子问题解之时直接查表。
            这种做法在重复子问题的数目关于输入的规模呈指数增长时特别有用。

***
动态规划在查找有很多重叠子问题的情况的最优解时有效。它将问题重新组合成子问题。
为了避免多次解决这些子问题，它们的结果都逐渐被计算并被保存，从简单的问题直到整个问题都被解决。因此，动态规划保存递归时的结果，因而不会在解决同样的问题时花费时间。

动态规划只能应用于有最优子结构的问题。最优子结构的意思是局部最优解能决定全局最优解（对有些问题这个要求并不能完全满足，故有时需要引入一定的近似）。
简单地说，问题能够分解成子问题来解决。

************适用情况****************
（1）最优子结构性质。如果问题的最优解所包含的子问题的解也是最优的，我们就称该问题具有最优子结构性质（即满足最优化原理）。最优子结构性质为动态规划算法解决问题提供了重要线索。

（2）无后效性。即子问题的解一旦确定，就不再改变，不受在这之后、包含它的更大的问题的求解决策影响。

（3）子问题重叠性质。子问题重叠性质是指在用递归算法自顶向下对问题进行求解时，每次产生的子问题并不总是新问题，有些子问题会被重复计算多次。
     动态规划算法正是利用了这种子问题的重叠性质，对每一个子问题只计算一次，然后将其计算结果保存在一个表格中，当再次需要计算已经计算过的子问题时，
     只是在表格中简单地查看一下结果，从而获得较高的效率。
'''


''' 
示例：
1 动态规划问题
动态规划算法和分治法类似，都是将带求解问题分解为若干个子问题，先求解子问题，然后从这些子问题的解得到原问题的答案。与分治法不同的是，动态规划要用一个表来记录所有已解决的子问题的答案。
不管该问题是否以后会被用到，只要它被计算过，就将其结果填入表中。在需要时从表中找出答案，避免大量重复计算，从而得到多项式时间算法。通常按一下几个步骤设计动态规划算法： 
（1）找出最优解性质，刻画最优解结构； 
（2）递归的定义最优值； 
（3）以自底向上的方式计算最优值； 
（4）根据计算最优值得到的信息，构造最优解。 
具体实例有：矩阵连乘，最长公共子序列，流水调度作业，0-1背包问题，最优二叉搜索树等。

2 最长公共子序列
2.1 原理
问题描述：给定两个序列 X = { x1, x2, …, xm }和Y = { y1, y2, …, yn }，找出X和Y的最长公共子序列。 
最优解：最长公共子序列的长度 m[ i ][ j ]以及相应的位置b[ i ][ j ]。 
递归定义最优值： 
这里写图片描述 
第一种情况：当 i = 0，或者 j = 0 时，长度为 0； 
第二种情况：当 xi = yi 时，表示长度等于子序列（去掉 i 位置元素后的序列）+1， 1 表示xi(或者 yi )；b[ i ][ j ] = 1 
第三种情况：当 xi ！= yi 时，表示两个不同子序列公共长度的最大值。 b[ i ][ j ]=2,b[ i ][ j ]=3

2.2 时间复杂度和空间复杂度
时间复杂度： 需要计算每个 c[ i ][ j ]的大小，所以时间为 mn； 
空间复杂度： 需要存储c[ i ][ j ]，所以空间为 mn。
'''
def LCS(i,j,X,b,out):   #得到最长子序列
    if i == -1 or j == -1:
        return
    if b[i][j] == 1:
        print i,j
        out.append(X[i])
        LCS(i-1,j-1,X,b,out)
    elif b[i][j] == 2:
        LCS(i-1,j,X,b,out)
    elif b[i][j] == 3:
        LCS(i,j-1,X,b,out)
    print out
    return out
def lcsLength(X,Y):  #计算最长子序列的长度，以及位置i,j 
    m = len(X)
    n = len(Y)
    c = {}
    c[-1] = {}
    b = {}
    for i in range(m):
        c[i] = {}
        c[i][-1] = 0
    for j in range(n):
        c[-1][j] = 0
    for k in range(m):
        b[k] = {}
    for i in range(m):        #外循环
        for j in range(n):    #内循环
            if X[i] == Y[j]:
                c[i][j] = c[i-1][j-1] + 1
                b[i][j] = 1
            elif c[i-1][j] >= c[i][j-1]:
                c[i][j] = c[i-1][j]
                b[i][j] = 2
            else:
                c[i][j] = c[i][j-1]
                b[i][j] = 3
            print i,j,c[i][j]
    print c[m-1][n-1]
    out = []
    out = LCS(m-1,n-1,X,b,out)
    print out[::-1]
X = raw_input().split()
Y = raw_input().split()
lcsLength(X, Y)