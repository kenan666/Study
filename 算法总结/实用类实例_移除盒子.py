'''
给出一些不同颜色的盒子，盒子的颜色由数字表示，即不同的数字表示不同的颜色。
你将经过若干轮操作去去掉盒子，直到所有的盒子都去掉为止。每一轮你可以移除具有相同颜色的连续 k 个盒子（k >= 1），
这样一轮之后你将得到 k*k 个积分。当你将所有盒子都去掉之后，求你能获得的最大积分和。

示例 1：

输入:
[1, 3, 2, 2, 2, 3, 4, 3, 1]
输出:
23

解释:

[1, 3, 2, 2, 2, 3, 4, 3, 1] 
----> [1, 3, 3, 4, 3, 1] (3*3=9 分) 
----> [1, 3, 3, 3, 1] (1*1=1 分) 
----> [1, 1] (3*3=9 分) 
----> [] (2*2=4 分) 

提示：盒子的总数 n 不会超过 100。

'''
#-------参考思路-------动态规划----------
'''
dp[i][j][k] 表示在 [i,j]部分能得到的最大得分
k表示boxes[i]左边有k个与之相等的数可以与它结合（可能原本有多余k个数，但是能和它合并一起消失的，只有k个）

如...X DFD X DFDF X SDF [X LSKDFJ X LSJDFLK X DLKFJ...]
dp[i][j][k]表示只考虑[]部分对分数的贡献，那么第一个X可能跟着前面K个X消失，也可能等着后面的X一起消失

1. 跟前面的k个一起消失的话 得分为 (k+1)**2 + helper(i+1,j,0)

2.1 跟后面的第二个X一起消失的话，[]中的“LSKDFJ” 部分独立拿分，X成为第二个X开头的子序的前导之一 k->1+k
    得分为helper(i+1,m-1,0)+helper(m,j,1+k)  m此时是第二个X的序号

2.2 跟后面的第三个X一起消失的话，[]中的“LSKDFJ X LSJDFLK” 部分独立拿分，X成为第三个X开头的子序的前导之一 k->1+k
    得分还是helper(i+1,m-1,0)+helper(m,j,1+k)  m此时是第三个X的序号

2.3 至于“LSKDFJ”与“LSJDFLK”部分分别独立拿分，再合并k+3个X拿分的情况，包含于2.1情况中
    因为helper(m,j,1+k) 可以递归，下一层的2.1情况就是前K个与第一个X第二个X和第三个X合并
    所以只用考虑[]中第一个X与第Y个X直接合并，中间部分作为子区间独立拿分的情况

几种情况取最高得分，并存入dp[i][j][k]
'''
def removeBoxes(boxes) :
    n = len(boxes)
    dp = [[[0]*n for _ in range(n)] for _ in range(n)]
    def helper(i,j,k):
        if i>j:
            return 0
        
        if dp[i][j][k]!=0:
            return dp[i][j][k]
        
        # 大段连续的部分肯定是放一起消失得分高，而不是单个消失
        while i<j and boxes[i]==boxes[i+1]:
            i+=1
            k+=1
                
        res = (k+1)**2 + helper(i+1,j,0)
        
        for m in range(i+1,j+1):
            if boxes[m]==boxes[i]:
                res = max(res, helper(i+1,m-1,0)+helper(m,j,1+k))
                
        dp[i][j][k] = res
        return dp[i][j][k]
    
    return helper(0,n-1,0)

#----------------------------------------------------------------------------
# --------------- 思路-------
'''
思路：

涉及子串的动态规划一般从子串两端进行递推，即(i,j)子串。 
分析如下： 
dp[i][j][k]表示从i到j子串并且右端存在与j相同的k个字符其获得的最大点数。 
有1，3，2，2，2，3，3 
    i                          j                                   dp[i][j][1]        
此时有两种可选操作： 
1、将j以及其后面的连续相同的串消除获得点数：dp[i][j-1][0]+(k+1)*(k+1) 
      1，3，2，2，2，4，3，1  ——>  dp[i][j][0]+2*2 

2、在子串内部寻找与右端相同的字符，将子串划分成两部分，先消除内部，再消除右端：dp[i][p][k+1]+dp[p+1][j-1][0] 
      1，3，3，1  ——>  dp[i][p][k+1] 
      2，2，2，4  ——>  dp[p+1][j-1][0] 

-----> dp[i][j][k]最大值为上面两种情况的最大值

'''
def removeBoxes(self, boxes):
        """
        :type boxes: List[int]
        :rtype: int
        """
        #涉及子串动态规划利用(i,j)进行地推   dp[i][j][k]表示从i到j子串并且右端存在与j相同的k个字符其获得的最大点数。
        n = len(boxes)
        dp = [[[0]*n for _ in range(n)]for _ in range(n)]
        return self.robot(boxes,dp,0,n-1,0)
    
def robot(self,boxes,dp,x,y,k):
    if x > y:
        return 0
    if dp[x][y][k] > 0:
        return dp[x][y][k]
    while x < y and boxes[y] == boxes[y-1]:
        y -= 1
        k += 1
        
    dp[x][y][k] = self.robot(boxes,dp,x,y-1,0) + (k+1)*(k+1)
    for i in range(x,y):
        if boxes[i] == boxes[y]:
            dp[x][y][k] = max(dp[x][y][k],self.robot(boxes,dp,x,i,k+1) + self.robot(boxes,dp,i+1,y-1,0))
    return dp[x][y][k]
