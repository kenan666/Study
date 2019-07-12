'''
给定 n 个非负整数，用来表示柱状图中各个柱子的高度。每个柱子彼此相邻，且宽度为 1 。

求在该柱状图中，能够勾勒出来的矩形的最大面积。

以上是柱状图的示例，其中每个柱子的宽度为 1，给定的高度为 [2,1,5,6,2,3]。

图中阴影部分为所能勾勒出的最大矩形面积，其面积为 10 个单位。

示例:

输入: [2,1,5,6,2,3]
输出: 10


'''
#  解1   暴力法检索
'''
首先，要想找到第 i 位置最大面积是什么？

是以i 为中心，向左找第一个小于 heights[i] 的位置 left_i；向右找第一个小于于 heights[i] 的位置 right_i，即最大面积为 heights[i] * (right_i - left_i -1)

时间复杂度为O(N^2)
'''
def largestRectangleArea(self, heights: List[int]) -> int:
    res = 0
    n = len(heights)
    for i in range(n):
        left_i = i
        right_i = i
        while left_i >= 0 and heights[left_i] >= heights[i]:
            left_i -= 1
        while right_i < n and heights[right_i] >= heights[i]:
            right_i += 1
        res = max(res, (right_i - left_i - 1) * heights[i])
    return res


#  解2 
'''
思路一：
当我们找 i 左边第一个小于 heights[i] 如果 heights[i-1] >= heights[i] 其实就是和 heights[i-1] 左边第一个小于 heights[i-1] 一样。依次类推，右边同理。

'''
def largestRectangleArea(self, heights: List[int]) -> int:
    if not heights:
        return 0
    n = len(heights)
    left_i = [0] * n
    right_i = [0] * n
    left_i[0] = -1
    right_i[-1] = n
    for i in range(1, n):
        tmp = i - 1
        while tmp >= 0 and heights[tmp] >= heights[i]:
            tmp = left_i[tmp]
        left_i[i] = tmp
    for i in range(n - 2, -1, -1):
        tmp = i + 1
        while tmp < n and heights[tmp] >= heights[i]:
            tmp = right_i[tmp]
        right_i[i] = tmp
    # print(left_i)
    # print(right_i)
    res = 0
    for i in range(n):
        res = max(res, (right_i[i] - left_i[i] - 1) * heights[i])
    return res

# 解3 栈
'''
思路二：栈
利用单调栈

维护一个单调递增的栈，就可以找到 left_i 和 right_i
'''
def largestRectangleArea(self, heights: List[int]) -> int:
    stack = []
    heights = [0] + heights + [0]
    res = 0
    for i in range(len(heights)):
        #print(stack)
        while stack and heights[stack[-1]] > heights[i]:
            tmp = stack.pop()
            res = max(res, (i - stack[-1] - 1) * heights[tmp])
        stack.append(i)
    return res
