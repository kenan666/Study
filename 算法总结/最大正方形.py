'''
在一个由 0 和 1 组成的二维矩阵内，找到只包含 1 的最大正方形，并返回其面积。

示例:
输入: 

1 0 1 0 0
1 0 1 1 1
1 1 1 1 1
1 0 0 1 0

输出: 4
'''
'''
申请一个长度为矩阵列数的一维数组dp, dp[j]代表以matrix[i][j]为结尾的正方形的边长, 于是当我们计算矩阵中以某个点为右下角的正方形边长时, 
就可以利用右上角已经计算过的变量直接获取相应的信息, 这里在使用dp时, 需要注意的一点是, 由于仅仅需要右上角的值, 
因此, 每次新的dp生成时, 都要向后移一位, 前面补0.

时间复杂度O(m*n)
空间复杂度O(n)
'''
def maximalSquare(self, matrix: List[List[str]]) -> int:
    if len(matrix) == 0: return 0
    m = len(matrix)
    n = len(matrix[0])

    dp = [0] * (n+1)
    res = 0
    for i in range(m):
        for j in range(n):
            if matrix[i][j] != '0': # 注意, 字符 '0' 在 bool 中是 True 的, 所以不能直接用 if matrix[i][j]
                edge = dp[j]
                k = 1
                while (k <= edge and matrix[i-k][j]!='0' and matrix[i][j-k]!='0'): # 利用之前已经求得的正方形基础上算当前正方形边长
                    k += 1
                dp[j] = k # 更新正方形边长
            else:
                dp[j] = 0
            res = max(res, dp[j]) # 更新 res
        dp = [0] + dp[0:-1] # dp 数组最前方加0, 其他元素后移, 最后一个元素再后面用不到, 舍去
    return res*res
