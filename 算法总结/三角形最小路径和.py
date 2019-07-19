'''
给定一个三角形，找出自顶向下的最小路径和。每一步只能移动到下一行中相邻的结点上。

例如，给定三角形：

[
     [2],
    [3,4],
   [6,5,7],
  [4,1,8,3]
]
自顶向下的最小路径和为 11（即，2 + 3 + 5 + 1 = 11）。

'''
#利用DFS深度优先遍历，从上到下扫描所有路径
def minimumTotal(self, triangle: List[List[int]]) -> int:
    self.res = float("inf")
    row = len(triangle)
    def helper(level,i,j,tmp):
        if level == row:
            self.res = min(self.res,tmp)
            return
        if 0 <= i <len(triangle[level]):
            helper(level + 1,i, i+1,tmp+triangle[level][i])
        if 0 <= j <len(triangle[level]):
            helper(level + 1,j, j+1,tmp+triangle[level][j])
    helper(0,-1,0,0)
    return self.res


# 动态规划方法  自底向上遍历  从倒数第二行开始依次遍历，最后triangle[0][0]就是想要的结果
def minimumTotal(self, triangle):
    
    if len(triangle) == 0:
        return 0
    row = len(triangle) - 2
    for row in range(row, -1, -1):
        for col in range(len(triangle[row])):
            triangle[row][col] += min(triangle[row+1][col],triangle[row+1][col+1])
    return triangle[0][0]
