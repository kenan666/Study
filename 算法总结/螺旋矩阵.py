'''
给定一个正整数 n，生成一个包含 1 到 n2 所有元素，且元素按顺时针顺序螺旋排列的正方形矩阵。

示例:

输入: 3
输出:
[
 [ 1, 2, 3 ],
 [ 8, 9, 4 ],
 [ 7, 6, 5 ]
]

'''
def generateMatrix(self, n: int) -> List[List[int]]:
    above_row = 0
    below_row = n - 1
    left_col = 0
    right_col = n - 1
    res = [ [0] * n for _ in range(n) ]
    num = 1
    while above_row <= below_row and left_col <= right_col:
        # 从左到右
        for i in range(left_col, right_col+1):
            res[above_row][i] = num
            num += 1
        # 上行加1
        above_row += 1
        # 从上到下
        for i in range(above_row, below_row+1):
            res[i][right_col] = num
            num += 1
        right_col -= 1
        # 从右到左
        for i in range(right_col, left_col-1, -1):
            res[below_row][i] = num
            num += 1
        below_row -= 1
        #从下到上
        for i in range(below_row, above_row-1, -1):
            res[i][left_col] = num
            num += 1
        left_col += 1
    return res
