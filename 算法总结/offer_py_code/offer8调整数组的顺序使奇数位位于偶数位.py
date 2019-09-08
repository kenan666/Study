'''
题目：调整数组的顺序使奇数位于偶数前面

题一：输入一个整数数组，实现一个函数来调整该数组中数字的顺序，使得所有奇数位于数组的前半部分，所有偶数位于数组的后半部分。
'''
'''
解题思路：
使用两个指针，
1、第一个指针初始化指向数组的第一个数字，从前向后移动，遇到偶数就停下来；
2、第二个指针指向数组的最后一个数字，从后向前移动，遇到奇数就停下来，交换两个指针指向的元素，直到两个指针相遇。
'''
def reOrderArray(self,array):
    if array == None or len(array) == 0:
        return False

    pBegin = 0
    pEnd = len(array)-1

    while pBegin < pEnd:
        while pBegin < pEnd and not self.isEven(array[pBegin]):# isEven 函数--->奇偶判断函数 
            pBegin += 1
        while pBegin < pEnd and self.isEven(array[pEnd]):
            pEnd -= 1

        if pBegin < pEnd:  # 两两交换
            temp = array[pBegin]
            array[pBegin] = array[pEnd]
            array[pEnd] = temp

    return array
        