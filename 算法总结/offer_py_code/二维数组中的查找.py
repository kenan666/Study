'''
在一个二维数组中，每一行都按照从左到右递增的顺序排序，每一列都按照从上到下递增的顺序排序。
请完成一个函数，输入这样的一个二维数组和一个整数，判断数组中是否含有该整数。

题目：二维数组中，每行从左到右递增，每列从上到下递增，给出一个数，判断它是否在数组中

思路：从左下角或者右上角开始比较
'''
def find_integer(matrix,num):

    if not matrix:
        return False

    rows,cols = len(matrix),len(matrix[0])
    row,col = rows - 1,0
    while row >= 0 and col <= cols - 1:
        if matrix[row][col] == num:
            return True
        elif matrix[row][col] > num:   #  左下角开始查找
            row -= 1
        else :
            col += 1
        '''
        右上角：
        elif matrix[row][col] > num:   
            row += 1
        else :
            col -= 1
        '''
    return False

# 双循环遍历
# 双循环比较简单---暴力法解决问题，依次寻找，直到找到 target 时间复杂度高
def findTarget(target,matrix):
    row,col = len(matrix),len(matrix[0])
    for i in range (row):
        for j in range(col):
            if matrix[i][j] == target:
                return True
    return False