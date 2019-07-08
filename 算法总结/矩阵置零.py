'''
给定一个 m x n 的矩阵，如果一个元素为 0，则将其所在行和列的所有元素都设为 0。请使用原地算法。

示例 1:

输入: 
[
  [1,1,1],
  [1,0,1],
  [1,1,1]
]
输出: 
[
  [1,0,1],
  [0,0,0],
  [1,0,1]
]
示例 2:

输入: 
[
  [0,1,2,0],
  [3,4,5,2],
  [1,3,1,5]
]
输出: 
[
  [0,0,0,0],
  [0,4,5,0],
  [0,3,1,0]
]

'''
# 思路1  两遍扫matrix,第一遍用集合记录哪些行,哪些列有0;第二遍置0
def setZeroes(self, matrix: List[List[int]]) -> None:
    # 分别将行，列全部扫描并置零
    row = len(matrix)
    col = len(matrix[0])
    row_zero = set()
    col_zero = set()
    for i in range(row):
        for j in range(col):
            if matrix[i][j] == 0:
                row_zero.add(i)
                col_zero.add(j)
    for i in range(row):
        for j in range(col):
            if i in row_zero or j in col_zero:
                matrix[i][j] = 0


# 思路2
'''
用matrix第一行和第一列记录该行该列是否有0,作为标志位

但是对于第一行,和第一列要设置一个标志位,为了防止自己这一行(一列)也有0的情况
'''
def setZeroes(self, matrix: List[List[int]]) -> None:
       
    row = len(matrix)
    col = len(matrix[0])
    row0_flag = False
    col0_flag = False
    # 找第一行是否有0
    for j in range(col):
        if matrix[0][j] == 0:
            row0_flag = True
            break
    # 第一列是否有0
    for i in range(row):
        if matrix[i][0] == 0:
            col0_flag = True
            break

    # 把第一行或者第一列作为 标志位
    for i in range(1, row):
        for j in range(1, col):
            if matrix[i][j] == 0:
                matrix[i][0] = matrix[0][j] = 0
    #print(matrix)
    # 置0
    for i in range(1, row):
        for j in range(1, col):
            if matrix[i][0] == 0 or matrix[0][j] == 0:
                matrix[i][j] = 0

    if row0_flag:
        for j in range(col):
            matrix[0][j] = 0
    if col0_flag:
        for i in range(row):
            matrix[i][0] = 0

# 简化
def setZeroes(self, matrix: List[List[int]]) -> None:
        
    flag_col = False
    row = len(matrix)
    col = len(matrix[0])
    for i in range(row):
        if matrix[i][0] == 0: flag_col = True
        for j in range(1,col):
            if matrix[i][j] == 0:
                matrix[i][0] = matrix[0][j] = 0
    
    for i in range(row - 1, -1, -1):
        for j in range(col - 1, 0, -1):
            if matrix[i][0] == 0 or matrix[0][j] == 0:
                matrix[i][j] = 0

        if flag_col == True: matrix[i][0] = 0

